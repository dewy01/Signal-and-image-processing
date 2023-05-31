import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
from scipy.signal import spectrogram

f = 1000
f_max = 2000
Fs = 8000
t = 2
x = np.arange(0, t, 1/Fs)
xSong = np.arange(0, t, 1/44100)
sin = np.sin(2*np.pi*x*f)
sqr = np.sign(sin)
tri = np.abs(2*(x*f - np.floor(0.5 + x*f))) - 1
saw = 2*(x*f - np.floor(x*f + 0.5))
chi = np.sin(2*np.pi*x*f + np.pi*x*f*(f_max - f)/t)
noi = np.random.randn(int(t*Fs)+1)
Fs_mow, mow = wavfile.read("sound.wav")
mow = mow[:16001]
Fs_son, son = wavfile.read("song.wav")
son = son[:44100*2]

plt.figure(figsize=(12, 6))

plt.subplot(2, 4, 1)
frequencies, times, amplitudes = spectrogram(mow, fs=8000, window='hamming', nperseg=1024, noverlap=120)
plt.pcolormesh(times, frequencies/1000, 10 * np.log10(amplitudes))
plt.colorbar(label='dB')
plt.title("Sygnał mowy")
plt.xlabel("czas [s]")
plt.ylabel("częstotliwość [kHz]")

plt.subplot(2, 4, 2)
frequencies, times, amplitudes = spectrogram(son, fs=44100, window='hamming', nperseg=1024, noverlap=120)
plt.pcolormesh(times, frequencies/1000, 10 * np.log10(amplitudes))
plt.colorbar(label='dB')
plt.title("Sygnał muzyki")
plt.xlabel("czas [s]")
plt.ylabel("częstotliwość [kHz]")

plt.subplot(2, 4, 3)
frequencies, times, amplitudes = spectrogram(sin, fs=8000, window='hamming', nperseg=1024, noverlap=120)
plt.pcolormesh(times, frequencies/1000, 10 * np.log10(amplitudes))
plt.colorbar(label='dB')
plt.title("Sygnał sinusoidalny o stałej częstotliwości")
plt.xlabel("czas [s]")
plt.ylabel("częstotliwość [kHz]")

plt.subplot(2, 4, 4)
frequencies, times, amplitudes = spectrogram(sqr, fs=8000, window='hamming', nperseg=1024, noverlap=120)
plt.pcolormesh(times, frequencies/1000, 10 * np.log10(amplitudes))
plt.colorbar(label='dB')
plt.title("Sygnał prostokątny")
plt.xlabel("czas [s]")
plt.ylabel("częstotliwość [kHz]")

plt.subplot(2, 4, 5)
frequencies, times, amplitudes = spectrogram(tri, fs=8000, window='hamming', nperseg=1024, noverlap=120)
plt.pcolormesh(times, frequencies/1000, 10 * np.log10(amplitudes))
plt.colorbar(label='dB')
plt.title("Sygnał trójkątny")
plt.xlabel("czas [s]")
plt.ylabel("częstotliwość [kHz]")

plt.subplot(2, 4, 6)
frequencies, times, amplitudes = spectrogram(saw, fs=8000, window='hamming', nperseg=1024, noverlap=120)
plt.pcolormesh(times, frequencies/1000, 10 * np.log10(amplitudes))
plt.colorbar(label='dB')
plt.title("Sygnał piłokształtny")
plt.xlabel("czas [s]")
plt.ylabel("częstotliwość [kHz]")

plt.subplot(2, 4, 7)
frequencies, times, amplitudes = spectrogram(chi, fs=8000, window='hamming', nperseg=1024, noverlap=120)
plt.pcolormesh(times, frequencies/1000, 10 * np.log10(amplitudes))
plt.colorbar(label='dB')
plt.title("Sygnał sinusoidalny o zmiennej częstotliwości")
plt.xlabel("czas [s]")
plt.ylabel("częstotliwość [kHz]")

plt.subplot(2, 4, 8)
frequencies, times, amplitudes = spectrogram(noi, fs=8000, window='hamming', nperseg=1024, noverlap=120)
plt.pcolormesh(times, frequencies/1000, 10 * np.log10(amplitudes))
plt.colorbar(label='dB')
plt.title("Sygnał szumu")
plt.xlabel("czas [s]")
plt.ylabel("częstotliwość [kHz]")

plt.tight_layout()
plt.show()
