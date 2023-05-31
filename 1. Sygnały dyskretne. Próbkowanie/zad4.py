import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
from scipy.io import wavfile

plt.figure()

fs, signal = wavfile.read('witam.wav')
t = np.linspace(0, len(signal) / fs, len(signal))

y = np.random.randn(len(signal))
plt.subplot(4, 1, 1)
plt.plot(t, signal)
plt.xlabel('Czas [s.]')
plt.ylabel('signal [n]')
plt.title("Oryginalnie zarejestrowany sygnał")

y1 = np.flip(signal)
plt.subplot(4, 1, 2)
plt.plot(t, y1)
plt.xlabel('Czas [s.]')
plt.ylabel('signal [n]')
plt.title("Sygnał odwrócony w czasie")

y = y / 34.200009
r = np.mean(signal ** 2) / np.mean(y ** 2)
plt.subplot(4, 1, 3)
plt.plot(t, y)
plt.xlabel('Czas [s.]')
plt.ylabel('signal [n]')
plt.title("Szum gaussowski")

z = y + signal
plt.subplot(4, 1, 4)
plt.plot(t, z)
plt.xlabel('Czas [s.]')
plt.ylabel('signal [n]')
plt.title("Superpozycja sygnału mowy z sygnałem szumu gaussowskiego")

plt.tight_layout()
plt.show()

# Play the sound
sd.play(signal, fs)
sd.wait()

# Play the inverted sound
sd.play(y1, fs)
sd.wait()

# Play the noise
sd.play(y, fs)
sd.wait()

# Play the combined signal
sd.play(z, fs)
sd.wait()
