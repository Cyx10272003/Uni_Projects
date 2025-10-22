%% Proposed Convolutional Network coding scheme with NOMA
clear; clc; close all;
set(0,'DefaultFigureVisible','on');

%% Parameters
snr_dB    = 0:5:30; % SNR Range
d         = numel(snr_dB);
numFrames = 300; %frames per SNR
M         = 4;   % QPSK                      
convRate  = 1/2; % Convolutional code rate
trellis   = poly2trellis(7,[171 133]); % K=7, rate=1/2
tbl       = 34; % traceback depth for Viterbi
anPower   = 0.05; %% Artificial Noise 

%% Preallocate Metrics
berPropU1  = zeros(1,d); berPropU2  = zeros(1,d);
berBaseU1  = zeros(1,d); berBaseU2  = zeros(1,d);
thruPropU1 = zeros(1,d); thruPropU2 = zeros(1,d);
thruBaseU1 = zeros(1,d); thruBaseU2 = zeros(1,d);

%% Simulation Loop
for idx = 1:d
    snr      = snr_dB(idx);
    noiseVar = 1/(2*10^(snr/10));
    errsProp = [0 0];
    errsBase = [0 0];

    for f = 1:numFrames
        K = 1000;

        %% Bit Generation (coded)
        u1 = randi([0 1],K,1);
        u2 = randi([0 1],K,1);
        c1 = convenc(u1, trellis);
        c2 = convenc(u2, trellis);

        % QPSK modulation
        idx1 = reshape(c1,2,[]).' * [2;1];
        s1   = pskmod(idx1, M, pi/4, 'gray');
        idx2 = reshape(c2,2,[]).' * [2;1];
        s2   = pskmod(idx2, M, pi/4, 'gray');
        symLen = numel(s1);

        % Channel-aware dynamic power allocation
        p1 = abs(randn)^2; p2 = abs(randn)^2;
        alpha_dyn = p2 / (p1 + p2);
        beta_dyn  = p1 / (p1 + p2);

        % Artificial Noise
        v = (randn(size(s1)) + 1j*randn(size(s1))) / sqrt(2);
        v = v ./ norm(v);
        AN = sqrt(anPower) * v;
        scale = sqrt(1 - anPower);
        txProp = scale * (sqrt(alpha_dyn)*s1 + sqrt(beta_dyn)*s2) + AN;

        %% Generate uncoded random bits
        baseU1 = randi([0 1], K, 1);
        baseU2 = randi([0 1], K, 1);

        % QPSK demolulation
        idxBase1 = reshape(baseU1, 2, []).' * [2;1];
        idxBase2 = reshape(baseU2, 2, []).' * [2;1];
        sBase1   = pskmod(idxBase1, M, pi/4, 'gray');
        sBase2   = pskmod(idxBase2, M, pi/4, 'gray');

        alpha0 = 0.2; beta0 = 0.8;
        txBase = sqrt(alpha0)*sBase1 + sqrt(beta0)*sBase2;

        %% Channels
        hProp = (randn(symLen,1) + 1j*randn(symLen,1))/sqrt(2);
        rxProp = awgn(hProp.*txProp, snr, 'measured');
        eqProp = rxProp ./ hProp;

        hBase = (randn(length(txBase),1) + 1j*randn(length(txBase),1))/sqrt(2);
        rxBase = awgn(hBase .* txBase, snr, 'measured');
        eqBase = rxBase ./ hBase;

        %% Proposed Decoding
        % User 1
        llr1 = pskdemod(eqProp, M, pi/4, 'gray', 'OutputType','approxllr','NoiseVariance',noiseVar);
        r1   = vitdec(llr1, trellis, tbl, 'trunc', 'unquant'); r1 = r1(1:K);

        % SIC and User 2
        c1hat = convenc(r1, trellis);
        idx1e = reshape(c1hat,2,[]).' * [2;1];
        se1   = pskmod(idx1e, M, pi/4, 'gray');
        rem2  = eqProp - scale*sqrt(alpha_dyn)*se1;
        llr2  = pskdemod(rem2/(scale*sqrt(beta_dyn)), M, pi/4, 'gray', 'OutputType','approxllr','NoiseVariance',noiseVar);
        r2    = vitdec(llr2, trellis, tbl, 'trunc', 'unquant'); r2 = r2(1:K);
        errsProp = errsProp + [sum(r1 ~= u1), sum(r2 ~= u2)];

        %% Conventional Decoding
        % User 1
        sym1 = pskdemod(eqBase, M, pi/4, 'gray');
        bits1 = de2bi(sym1,2,'left-msb').'; bits1 = bits1(:);
        r1b = bits1(1:K);

        % SIC and User 2
        se1b = pskmod(sym1, M, pi/4, 'gray');
        remB = eqBase - sqrt(alpha0)*se1b;
        sym2 = pskdemod(remB/sqrt(beta0), M, pi/4, 'gray');
        bits2 = de2bi(sym2,2,'left-msb').'; bits2 = bits2(:);
        r2b = bits2(1:K);

        errsBase = errsBase + [sum(r1b ~= baseU1), sum(r2b ~= baseU2)];
    end

    %% BER and Throughput Metrics
    berPropU1(idx) = errsProp(1)/(K*numFrames);
    berPropU2(idx) = errsProp(2)/(K*numFrames);
    berBaseU1(idx) = errsBase(1)/(K*numFrames);
    berBaseU2(idx) = errsBase(2)/(K*numFrames);

    thruPropU1(idx) = convRate * (1 - berPropU1(idx));
    thruPropU2(idx) = convRate * (1 - berPropU2(idx));
    thruBaseU1(idx) = 1 * (1 - berBaseU1(idx));
    thruBaseU2(idx) = 1 * (1 - berBaseU2(idx));
end

%% Plotting
figure;
subplot(1,2,1);
semilogy(snr_dB, berPropU1, '-o', snr_dB, berPropU2, '-s', ...
         snr_dB, berBaseU1, '--^', snr_dB, berBaseU2, '--d', ...
         'LineWidth', 2);
grid on; title('Proposed convolutional coded network coding scheme with NOMA'); xlabel('SNR (dB)'); ylabel('BER');
legend('Prop U1','Prop U2','Conv U1','Conv U2','Location','southwest');

subplot(1,2,2);
plot(snr_dB, thruPropU1, '-o', snr_dB, thruPropU2, '-s', ...
     snr_dB, thruBaseU1, '--^', snr_dB, thruBaseU2, '--d', ...
     'LineWidth', 2);
grid on; title('Proposed convolutional coded network coding scheme with NOMA'); xlabel('SNR (dB)'); ylabel('Throughput');
legend('Prop U1','Prop U2','Conv U1','Conv U2','Location','southeast');

