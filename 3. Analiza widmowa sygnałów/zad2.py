import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import square, sawtooth, chirp
from scipy.io import wavfile

# Clear figure
plt.close('all')

f = 1000
f_max = 2000
Fs = 8000
t = 2
x = np.arange(0, t, 1 / Fs)
xSong = np.arange(0, t, 1 / 44100)
sin = np.sin(2 * np.pi * x * f)
sqr = square(2 * np.pi * x * f)
tri = sawtooth(2 * np.pi * x * f, 0.5)
saw = sawtooth(2 * np.pi * x * f)
chi = chirp(x, f, t, f_max)
noi = np.random.randn(t * Fs + 1)
Fs_audio, mow = wavfile.read("sound.wav")
mow = mow[:t * Fs + 1]
Fs_song, son = wavfile.read("song.wav")
son = son[:int(t * 44100) + 1]

plt.figure(figsize=(9, 7))

plt.subplot(4, 2, 1)
plt.stem(x, sin, use_line_collection=True)
plt.title("Sygnał sinusoidalny 1kHz")
plt.xlabel("t (sek)")
plt.ylabel("U (V)")
plt.axis([0, 0.02, -1.2, 1.2])

plt.subplot(4, 2, 2)
plt.stem(x, sqr, use_line_collection=True)
plt.title("Sygnał prostokątny 1kHz")
plt.xlabel("t (sek)")
plt.ylabel("U (V)")
plt.axis([0, 0.02, -1.2, 1.2])

plt.subplot(4, 2, 3)
plt.stem(x, tri, use_line_collection=True)
plt.title("Sygnał trójkątny 1kHz")
plt.xlabel("t (sek)")
plt.ylabel("U (V)")
plt.axis([0, 0.02, -1.2, 1.2])

plt.subplot(4, 2, 4)
plt.stem(x, saw, use_line_collection=True)
plt.title("Sygnał piłokształtny 1kHz")
plt.xlabel("t (sek)")
plt.ylabel("U (V)")
plt.axis([0, 0.02, -1.2, 1.2])

plt.subplot(4, 2, 5)
plt.plot(x, chi)
plt.title("Sygnał sinusoidalny narastający 1-2kHz")
plt.xlabel("t (sek)")
plt.ylabel("U (V)")
plt.axis([0, 0.02, -1.2, 1.2])

plt.subplot(4, 2, 6)
plt.plot(x, noi)
plt.title("Szum")
plt.xlabel("t (sek)")
plt.ylabel("U (V)")
plt.axis([0, 0.02, -4, 4])

plt.subplot(4, 2, 7)
plt.plot(x, mow)
plt.title("Sygnał mowy")
plt.xlabel("t (sek)")
plt.ylabel("U (V)")
plt.axis([0, 2, -1.2, 1.2])

plt.subplot(4, 2, 8)
plt.plot(xSong, son)
plt.title("Sygnał muzyki")
plt.xlabel("t (sek)")
plt.ylabel("U (V)")
plt.axis([0, 2, -1.2, 1.2])

plt.tight_layout()

# Calculate periodograms
psin, xpsin = plt.psd(sin[:Fs * t], NFFT=8192, Fs=Fs)
psqr, xpsqr = plt.psd(sqr[:Fs * t], NFFT=8192, Fs=Fs)
ptri, xptri = plt.psd(tri[:Fs * t], NFFT=8192, Fs=Fs)
psaw, xpsaw = plt.psd(saw[:Fs * t], NFFT=8192, Fs=Fs)
pchi, xpchi = plt.psd(chi[:Fs * t], NFFT=8192, Fs=Fs)
pnoi, xpnoi = plt.psd(noi[:Fs * t], NFFT=8192, Fs=Fs)
pmow, xpmow = plt.psd(mow[:Fs * t], NFFT=8192, Fs=Fs)
pson, xpson = plt.psd(son[:int(44100 * t)], NFFT=65536, Fs=44100)

xpsin = xpsin / 1000
xpsqr = xpsqr / 1000
xptri = xptri / 1000
xpsaw = xpsaw / 1000
xpchi = xpchi / 1000
xpnoi = xpnoi / 1000
xpmow = xpmow / 1000
xpson = xpson / 1000

psin = 10 * np.log10(psin)
psqr = 10 * np.log10(psqr)
ptri = 10 * np.log10(ptri)
psaw = 10 * np.log10(psaw)
pchi = 10 * np.log10(pchi)
pnoi = 10 * np.log10(pnoi)
pmow = 10 * np.log10(pmow)
pson = 10 * np.log10(pson)

plt.figure(figsize=(9, 7))

plt.subplot(4, 2, 1)
plt.plot(xpsin, psin)
plt.title("Gęstość mocy sygnału sinusoidalnego 1kHz")
plt.xlabel("f (kHz)")
plt.ylabel("dB")
plt.axis([0, Fs / 2000, -110, 10])

plt.subplot(4, 2, 2)
plt.plot(xpsqr, psqr)
plt.title("Gęstość mocy sygnału prostokątnego 1kHz")
plt.xlabel("f (kHz)")
plt.ylabel("dB")
plt.axis([0, Fs / 2000, -80, 10])

plt.subplot(4, 2, 3)
plt.plot(xptri, ptri)
plt.title("Gęstość mocy sygnału trójkątnego 1kHz")
plt.xlabel("f (kHz)")
plt.ylabel("dB")
plt.axis([0, Fs / 2000, -110, 10])

plt.subplot(4, 2, 4)
plt.plot(xpsaw, psaw)
plt.title("Gęstość mocy sygnału piłokształtnego 1kHz")
plt.xlabel("f (kHz)")
plt.ylabel("dB")
plt.axis([0, Fs / 2000, -110, 10])

plt.subplot(4, 2, 5)
plt.plot(xpchi, pchi)
plt.title("Gęstość mocy sygnału sinusoidalnego narastającego 1-2kHz")
plt.xlabel("f (kHz)")
plt.ylabel("dB")
plt.axis([0, Fs / 2000, -150, 0])

plt.subplot(4, 2, 6)
plt.plot(xpnoi, pnoi)
plt.title("Gęstość mocy szumu")
plt.xlabel("f (kHz)")
plt.ylabel("dB")
plt.axis([0, Fs / 2000, -80, -10])

plt.subplot(4, 2, 7)
plt.plot(xpmow, pmow)
plt.title("Gęstość mocy sygnału mowy")
plt.xlabel("f (kHz)")
plt.ylabel("dB")
plt.axis([0, Fs / 2000, -130, -20])

plt.subplot(4, 2, 8)
plt.plot(xpson, pson)
plt.title("Gęstość mocy sygnału muzyki")
plt.xlabel("f (kHz)")
plt.ylabel("dB")
plt.axis([0, 44100 / 2000, -150, 0])

plt.tight_layout()
plt.show()
