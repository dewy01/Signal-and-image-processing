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
mow = mow[:int(t*Fs)+1]
Fs_son, son = wavfile.read("song.wav")
son = son[:int(t*44100)+1]

plt.figure(figsize=(12, 6))

plt.subplot(2, 4, 1)
plt.specgram(mow, NFFT=1024, Fs=Fs, window=np.hamming(1024), noverlap=120)
plt.title("Sygnał mowy")
plt.xlabel("czas [s]")
plt.ylabel("częstotliwość [kHz]")

plt.subplot(2, 4, 2)
plt.specgram(son, NFFT=1024, Fs=44100, window=np.hamming(1024), noverlap=120)
plt.title("Sygnał muzyki")
plt.xlabel("czas [s]")
plt.ylabel("częstotliwość [kHz]")

plt.subplot(2, 4, 3)
plt.specgram(sin, NFFT=1024, Fs=Fs, window=np.hamming(1024), noverlap=120)
plt.title("Sygnał sinusoidalny o stałej częstotliwości")
plt.xlabel("czas [s]")
plt.ylabel("częstotliwość [kHz]")

plt.subplot(2, 4, 4)
plt.specgram(sqr, NFFT=1024, Fs=Fs, window=np.hamming(1024), noverlap=120)
plt.title("Sygnał prostokątny")
plt.xlabel("czas [s]")
plt.ylabel("częstotliwość [kHz]")

plt.subplot(2, 4, 5)
plt.specgram(tri, NFFT=1024, Fs=Fs, window=np.hamming(1024), noverlap=120)
plt.title("Sygnał trójkątny")
plt.xlabel("czas [s]")
plt.ylabel("częstotliwość [kHz]")

plt.subplot(2, 4, 6)
plt.specgram(saw, NFFT=1024, Fs=Fs, window=np.hamming(1024), noverlap=120)
plt.title("Sygnał piłokształtny")
plt.xlabel("czas [s]")
plt.ylabel("częstotliwość [kHz]")

plt.subplot(2, 4, 7)
plt.specgram(chi, NFFT=1024, Fs=Fs, window=np.hamming(1024), noverlap=120)
plt.title("Sygnał sinusoidalny o zmiennej częstotliwości")
plt.xlabel("czas [s]")
plt.ylabel("częstotliwość [kHz]")

plt.subplot(2, 4, 8)
plt.specgram(noi, NFFT=1024, Fs=Fs, window=np.hamming(1024), noverlap=120)
plt.title("Sygnał szumu")
plt.xlabel("czas [s]")
plt.ylabel("częstotliwość [kHz]")

plt.tight_layout()
plt.show()
