import numpy as np
import matplotlib.pyplot as plt

f = 1
T = 1
Fs = 32
x = np.linspace(0, T - 1 / Fs, T * Fs)
xGraph = np.linspace(0, T, T * Fs + 1)
xFFT = np.linspace(0, Fs - 1, Fs)
y = np.sin(2 * np.pi * x * f)
yGraph = np.sin(2 * np.pi * xGraph * f)
Y = np.fft.fft(y)

rel = np.real(y)
relGraph = np.real(yGraph)
im = np.imag(y)
imGraph = np.imag(yGraph)
modulo = np.abs(y)
angl = np.angle(y)

relY = np.real(Y) / (Fs / 2)
imY = np.imag(Y) / (Fs / 2)
moduloY = np.abs(Y) / (Fs / 2)
anglY = np.angle(Y)

plt.figure(figsize=(9, 6))

plt.subplot(3, 2, 1)
plt.stem(xGraph, relGraph)
plt.title("Real")
plt.xlabel("t (sek)")
plt.ylabel("U (V)")
plt.axis([0, T, -1.2, 1.2])

plt.subplot(3, 2, 2)
plt.stem(xGraph, imGraph)
plt.title("Imaginary")
plt.xlabel("t (sek)")
plt.ylabel("U (V)")
plt.axis([0, T, -1.2, 1.2])

plt.subplot(3, 2, 3)
plt.stem(xFFT, relY)
plt.title("FFT Real")
plt.xlabel("nr próbki")
plt.ylabel("Amplituda")
plt.axis([0, Fs, -0.1, 0.1])

plt.subplot(3, 2, 4)
plt.stem(xFFT, imY)
plt.title("FFT Imaginary")
plt.xlabel("nr próbki")
plt.ylabel("Amplituda")
plt.axis([0, Fs, -1.2, 1.2])

plt.subplot(3, 2, 5)
plt.stem(xFFT, moduloY)
plt.title("FFT Absolute")
plt.xlabel("nr próbki")
plt.ylabel("Amplituda")
plt.axis([0, Fs, -0.1, 1.2])

plt.subplot(3, 2, 6)
plt.stem(xFFT, anglY)
plt.yticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
['-pi', '-pi/2', '0', 'pi/2', 'pi'])
plt.title("FFT Angle")
plt.xlabel("nr próbki")
plt.ylabel("Przesunięcie fazowe")
plt.axis([0, Fs, -np.pi - 0.5, np.pi + 0.5])

plt.tight_layout()
plt.show()