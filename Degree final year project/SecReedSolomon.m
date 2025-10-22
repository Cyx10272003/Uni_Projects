%% Proposed Reed Solomon Network coding scheme with NOMA
clear; clc; close all;
set(0,'DefaultFigureVisible','on');

%% Parameters
snr_dB    = 0:5:30; % SNR Range
d         = numel(snr_dB);
numFrames = 300; %frames per SNR
M         = 4; % QPSK
gfExp     = 8; 
RS_n      = 255; RS_k = 223; % RS block length/message length
anPower   = 0.05;     % Artificial noise power
Kbits     = RS_k * 8; % bits per RS block

%% Preallocate Metrics
berPropU1   = zeros(1,d);
berPropU2   = zeros(1,d);
berGenU1    = zeros(1,d);
berGenU2    = zeros(1,d);
thruPropU1  = zeros(1,d);
thruPropU2  = zeros(1,d);
thruGenU1   = zeros(1,d);
thruGenU2   = zeros(1,d);

%% Simulation Loop
for idx = 1:d
    snr       = snr_dB(idx);
    errsProp  = [0, 0];
    errsGen   = [0, 0];

    for f = 1:numFrames
        %% Generate Random Bits
        u1 = randi([0 1], Kbits, 1);
        u2 = randi([0 1], Kbits, 1);

        %% RS Encoding
        sym1    = bi2de(reshape(u1,8,[]).','left-msb').';
        sym2    = bi2de(reshape(u2,8,[]).','left-msb').';
        rsEnc1  = rsenc(gf(sym1,gfExp), RS_n, RS_k);
        rsEnc2  = rsenc(gf(sym2,gfExp), RS_n, RS_k);
        bits1   = de2bi(rsEnc1.x,8,'left-msb').'; bits1 = bits1(:);
        bits2   = de2bi(rsEnc2.x,8,'left-msb').'; bits2 = bits2(:);

        %% QPSK Mapping
        idx1    = bits1(1:2:end)*2 + bits1(2:2:end);
        idx2    = bits2(1:2:end)*2 + bits2(2:2:end);
        s1      = pskmod(idx1, M, pi/4, 'gray');
        s2      = pskmod(idx2, M, pi/4, 'gray');

        %% Dynamic Power Allocation
        p1 = abs(randn)^2;
        p2 = abs(randn)^2;
        alpha_dyn = p2/(p1+p2);
        beta_dyn  = p1/(p1+p2);

        %% Artificial Noise
        v = (randn(size(s1)) + 1j*randn(size(s1))) / sqrt(2);
        v = v ./ norm(v);
        AN = sqrt(anPower) * v;

        %% Transmit Signal
        tx = sqrt((1-anPower)*alpha_dyn)*s1 + sqrt((1-anPower)*beta_dyn)*s2 + AN;

        %% Channel
        h   = (randn(size(tx))+1j*randn(size(tx)))/sqrt(2);
        rx  = awgn(h.*tx, snr, 'measured');
        eq  = rx ./ h;

        %% Decode User 1
        hard1     = pskdemod(eq, M, pi/4, 'gray');
        bits1_hat = reshape(de2bi(hard1,2,'left-msb').',[],1);
        sym1_hat  = bi2de(reshape(bits1_hat,8,[]).','left-msb').';
        rs_in1    = reshape(gf(sym1_hat,gfExp), RS_n, []).';
        rs_out1   = rsdec(rs_in1, RS_n, RS_k);
        u1hat     = reshape(de2bi(rs_out1(1,:).x,8,'left-msb').',[],1);

        %% SIC & Decode User 2
        se1       = pskmod(hard1, M, pi/4, 'gray');
        rem       = eq - sqrt((1-anPower)*alpha_dyn)*se1;
        hard2     = pskdemod(rem/sqrt((1-anPower)*beta_dyn), M, pi/4, 'gray');
        bits2_hat = reshape(de2bi(hard2,2,'left-msb').',[],1);
        sym2_hat  = bi2de(reshape(bits2_hat,8,[]).','left-msb').';
        rs_in2    = reshape(gf(sym2_hat,gfExp), RS_n, []).';
        rs_out2   = rsdec(rs_in2, RS_n, RS_k);
        u2hat     = reshape(de2bi(rs_out2(1,:).x,8,'left-msb').',[],1);
        errsProp = errsProp + [sum(u1hat~=u1), sum(u2hat~=u2)];

        %% Uncoded baseline
        idxG1     = u1(1:2:end)*2 + u1(2:2:end);
        idxG2     = u2(1:2:end)*2 + u2(2:2:end);
        sg1       = pskmod(idxG1, M, pi/4, 'gray');
        sg2       = pskmod(idxG2, M, pi/4, 'gray');
        txG       = sqrt(alpha_dyn)*sg1 + sqrt(beta_dyn)*sg2;
        hG        = (randn(size(txG))+1j*randn(size(txG)))/sqrt(2);
        eqG       = awgn(hG.*txG, snr,'measured')./hG;
        dec1G     = reshape(de2bi(pskdemod(eqG,M,pi/4,'gray'),2,'left-msb').',[],1);
        dec2G     = reshape(de2bi(pskdemod((eqG-sqrt(alpha_dyn)*sg1)/sqrt(beta_dyn),M,pi/4,'gray'),2,'left-msb').',[],1);
        errsGen   = errsGen + [sum(dec1G~=u1), sum(dec2G~=u2)];
    end

    %% Metrics
    berPropU1(idx) = errsProp(1)/(Kbits*numFrames);
    berPropU2(idx) = errsProp(2)/(Kbits*numFrames);
    berGenU1(idx)  = errsGen(1)/(Kbits*numFrames);
    berGenU2(idx)  = errsGen(2)/(Kbits*numFrames);
    thruPropU1(idx)= (RS_k/RS_n)*(1-berPropU1(idx));
    thruPropU2(idx)= (RS_k/RS_n)*(1-berPropU2(idx));
    thruGenU1(idx) = 0.5*(1-berGenU1(idx));
    thruGenU2(idx) = 0.5*(1-berGenU2(idx));
end

%% Plot Results
figure;
subplot(1,2,1);
semilogy(snr_dB, berPropU1, '-o', snr_dB, berPropU2, '-s', ...
         snr_dB, berGenU1, '--^', snr_dB, berGenU2, '--d', 'LineWidth', 2);
grid on; title('Proposed ReedSolommon Coded network coding scheme'); xlabel('SNR (dB)'); ylabel('BER');
legend('Prop U1','Prop U2','Conv U1','Conv U2','Location','southwest');

subplot(1,2,2);
plot(snr_dB, thruPropU1, '-o', snr_dB, thruPropU2, '-s', ...
     snr_dB, thruGenU1, '--^', snr_dB, thruGenU2, '--d','LineWidth', 2);
grid on; title('Proposed ReedSolommon Coded network coding scheme'); xlabel('SNR (dB)'); ylabel('Throughput');
legend('Prop U1','Prop U2','Conv U1','Conv U2','Location','southeast');


