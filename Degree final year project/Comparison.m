%% Comparison of BER and Throughput: Convolutional vs Reed-Solomon Coded NOMA
clear; clc; close all;

%% SNR range
snr_dB = [5 10 15 20 25 30];

%% BER data 
ber_conv_u1 = [0.405 0.302 0.264 0.280 0.257 0.235];
ber_conv_u2 = [0.460 0.363 0.241 0.150 0.129 0.119];
ber_rs_u1   = [0.285 0.245 0.250 0.253 0.264 0.252];
ber_rs_u2   = [0.290 0.230 0.171 0.147 0.127 0.113];

%% Throughput data 
thru_conv_u1 = [0.297 0.348 0.367 0.360 0.371 0.382];
thru_conv_u2 = [0.269 0.318 0.379 0.425 0.435 0.440];
thru_rs_u1   = [0.626 0.660 0.656 0.653 0.643 0.654];
thru_rs_u2   = [0.621 0.673 0.725 0.746 0.763 0.775];

%% Plot BER comparison
figure;
subplot(1,2,1);
semilogy(snr_dB, ber_conv_u1, '-o', snr_dB, ber_conv_u2, '-s', ...
         snr_dB, ber_rs_u1, '--^', snr_dB, ber_rs_u2, '--d', 'LineWidth', 2);
grid on; xlabel('SNR (dB)'); ylabel('BER'); title('BER vs SNR performance for proposed Conv-coded and RS-coded NOMA network scheme');
legend('Conv U1', 'Conv U2', 'RS U1', 'RS U2', 'Location', 'southwest');

%% Plot Throughput comparison
figure;
subplot(1,2,2);
plot(snr_dB, thru_conv_u1, '-o', snr_dB, thru_conv_u2, '-s', ...
     snr_dB, thru_rs_u1, '--^', snr_dB, thru_rs_u2, '--d', 'LineWidth', 2);
grid on; xlabel('SNR (dB)'); ylabel('Throughput'); title('Throughput vs SNR performance for proposed Conv-coded and RS-coded NOMA network scheme');
legend('Conv U1', 'Conv U2', 'RS U1', 'RS U2', 'Location', 'southeast');
