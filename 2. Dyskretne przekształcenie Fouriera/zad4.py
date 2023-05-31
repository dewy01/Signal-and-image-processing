import numpy as np
import matplotlib.pyplot as plt

Fs = 64
f = 1 / Fs
x = np.arange(Fs + 1)
y = np.exp(1j * (2 * np.pi * f * x - np.pi / 3))
Y = np.fft.fft(y[:64]) / Fs

plt.figure(figsize=(9, 6))

plt.subplot(3, 2, 1)
plt.stem(x, np.real(y))
plt.title("Wartość rzeczywista funkcji y")
plt.xlabel("t (s)")
plt.ylabel("U (v)")
plt.axis([0, 64, -1.2, 1.2])

plt.subplot(3, 2, 2)
plt.stem(x, np.imag(y))
plt.title("Wartość urojona funkcji y")
plt.xlabel("t (s)")
plt.ylabel("U (v)")
plt.axis([0, 64, -1.2, 1.2])

plt.subplot(3, 2, 3)
plt.stem(x[:64] / 64, np.real(Y))
plt.title("Wartość rzeczywista transformaty fft(y)")
plt.xlabel("f (Hz)")
plt.ylabel("U (v)")
plt.axis([0, 1 / 4, -1.2, 1.2])

plt.subplot(3, 2, 4)
plt.stem(x[:64] / 64, np.imag(Y))
plt.title("Wartość urojona transformaty fft(y)")
plt.xlabel("f (Hz)")
plt.ylabel("U (v)")
plt.axis([0, 1 / 4, -1.2, 1.2])

plt.subplot(3, 2, 5)
plt.stem(x[:64] / 64, np.abs(Y))
plt.title("Wartość bezwzględna transformaty fft(y)")
plt.xlabel("f (Hz)")
plt.ylabel("U (v)")
plt.axis([0, 1 / 4, -1.2, 1.2])

plt.subplot(3, 2, 6)
plt.stem(x[:64] / 64, np.angle(Y))
plt.title("Wartość kątowa transformaty fft(y)")
plt.xlabel("f (Hz)")
plt.ylabel("fi (rad)")
plt.axis([0, 1 / 4, -4, 4])
plt.yticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi], ['-pi', '-pi/2', '0', 'pi/2', 'pi'])

plt.tight_layout()
plt.show()