import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy.io import wavfile

fpass = 2000
fs = 8000
f = fs / 2
fn = fpass / f
rzad = 3
zafalowanie = 1
tlumienie = 20

plt.figure()
plt.subplot(2, 1, 1)
b, a = signal.cheby1(rzad, zafalowanie, fn, "low")
w, h = signal.freqz(b, a)
f1 = w * f / np.pi
plt.plot(f1, 20 * np.log10(np.abs(h)))
plt.axis([0, f, -200, 10])
plt.subplot(2, 1, 2)
plt.plot(f1, np.unwrap(np.angle(h)))

plt.figure()
fs, m = wavfile.read("sound.wav")
m = np.array(m).T
length = len(m)
duration = length / fs
t = np.arange(0, length)
mf = signal.lfilter(b, a, m)
plt.subplot(2, 1, 1)
plt.plot(t, m)
plt.subplot(2, 1, 2)
plt.plot(t, mf)

plt.figure()
pmowa, xpmowa = signal.periodogram(m, fs, window=None, nfft=8192)
xpmowa = xpmowa / 1000
pmowa = 10 * np.log10(pmowa)

pmowafiltr, xpmowafiltr = signal.periodogram(mf, fs, window=None, nfft=8192)
xpmowafiltr = xpmowafiltr / 1000
pmowafiltr = 10 * np.log10(pmowafiltr)

plt.subplot(2, 1, 1)
plt.plot(xpmowa, pmowa)
plt.subplot(2, 1, 2)
plt.plot(xpmowafiltr, pmowafiltr)

plt.figure()
plt.subplot(2, 1, 1)
f, t, Sxx = signal.spectrogram(m, fs, window='hamming', nperseg=1024, noverlap=120)
plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='auto')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')
plt.subplot(2, 1, 2)
f, t, Sxx = signal.spectrogram(mf, fs, window='hamming', nperseg=1024, noverlap=120)
plt.pcolormesh(t, f, 10 * np.log10(Sxx), shading='auto')
plt.ylabel('Frequency [Hz]')
plt.xlabel('Time [sec]')

plt.show()
