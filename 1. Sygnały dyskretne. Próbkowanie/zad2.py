import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd

A = 1  # amplituda
f = 440  # częstotliwość dźwięku
fi = 0  # przesunięcie fazowe
Fs = 8192  # próbkowanie
t = 0.5  # sekundy

x = np.linspace(0, t, int(t * Fs))
y = A * np.sin(2 * np.pi * f * x + fi)

fig = plt.figure(figsize=(9, 6))
p1 = plt.subplot(2, 1, 1)
plt.plot(x, y)
plt.axis([0, 0.02, -3, 3])
plt.title("Sygnał sinusoidalny dla A=1V f=440Hz fi=0ms Fs=8192Hz")
plt.xlabel("t (ms)")
plt.ylabel("U (V)")

# Dla amplitudy
p2 = plt.subplot(2, 1, 2)
A_values = [0.5, 1.3, 2.3]
for i, A_value in enumerate(A_values):
    y_A = A_value * np.sin(2 * np.pi * f * x + fi)
    plt.plot(x, y_A, label=f"A={A_value}V")
plt.axis([0, 0.02, -3, 3])
plt.legend()
plt.xlabel("t (ms)")
plt.ylabel("U (V)")

plt.tight_layout()
plt.show()

# Play the sound
y_all = np.concatenate([y, np.zeros_like(x), y_A, np.zeros_like(x)])
sd.play(y_all, Fs)
sd.wait()

# Play individual sounds
Fs_values = [1000, 10000, 100000]
for Fs_value in Fs_values:
    x_fs = np.linspace(0, t, int(t * Fs_value))
    y_fs = A * np.sin(2 * np.pi * f * x_fs + fi)
    sd.play(y_fs, Fs_value)
    sd.wait()
