import numpy as np
import matplotlib.pyplot as plt

f1 = 1
t1 = 1
Fs1 = 32
P1 = 2 * Fs1 * t1 // 20
x1 = np.linspace(0, t1 - 1 / Fs1, t1 * Fs1)
xFFT1 = np.arange(Fs1 * t1 // P1) / t1
y1 = np.sin(2 * np.pi * x1 * f1)
Y1 = np.fft.fft(y1)
Y1_l = Y1[:Fs1 * t1 // P1]
Y1_m = np.abs(Y1_l) / (Fs1 * t1 / 2)

Fs2 = 32
t2 = 160
P2 = 2 * Fs2 * t2 // 100 # Podziałka
x2 = np.linspace(0, t2 - 1 / Fs2, t2 * Fs2)

y2_1 = np.cos(2 * np.pi * x2 / Fs2 + np.pi / 4)
y2_2 = 0.5 * np.cos(4 * np.pi * x2 / Fs2)
y2_3 = 0.25 * np.cos(8 * np.pi * x2 / Fs2 + np.pi / 2)
y2 = y2_1 + y2_2 + y2_3

xFFT2 = np.arange(Fs2 * t2 // P2) / t2
Y2 = np.fft.fft(y2)
Y2_l = Y2[:Fs2 * t2 // P2]
Y2_m = np.abs(Y2_l) / (Fs2 * t2 / 2)

plt.figure(figsize=(9, 6))

plt.subplot(3, 2, 1)
plt.plot(x1, y1)
plt.title("Funkcja zadania 3_1 oryginał")
plt.xlabel("t (sek)")
plt.ylabel("U (V)")
plt.axis([0, 1 - 1 / Fs1, -1.2, 1.2])

plt.subplot(3, 2, 2)
plt.plot(x2, y2)
plt.title("Funkcja zadania 3_2 oryginał")
plt.xlabel("t (sek)")
plt.ylabel("U (V)")
plt.axis([0, 159, -2, 2])

plt.subplot(3, 2, 3)
plt.stem(xFFT1, Y1_m)
plt.title("Funkcja zadania 3_1 po fft")
plt.xlabel("f (Hz)")
plt.ylabel("U (V)")
plt.axis([0, 9, -0.2, 1.2])

plt.subplot(3, 2, 4)
plt.stem(xFFT2, Y2_m)
plt.title("Funkcja zadania 3_2 po fft")
plt.xlabel("f (Hz)")
plt.ylabel("U (V)")
plt.axis([0, 0.3, -0.2, 1.2])

Y1_odw = np.fft.ifft(Y1)
Y2_odw = np.fft.ifft(Y2)
x_odw1 = np.arange(Fs1 * t1)
x_odw2 = np.arange(Fs2 * t2)
plt.subplot(3, 2, 5)
plt.plot(x_odw1, Y1_odw)
plt.title("Funkcja zadania 3_1 odtworzona")
plt.xlabel("nr próbki")
plt.ylabel("U (V)")
plt.axis([0, 31, -1.2, 1.2])

plt.subplot(3, 2, 6)
plt.plot(x_odw2, Y2_odw)
plt.title("Funkcja zadania 3_2 odtworzona")
plt.xlabel("nr próbki")
plt.ylabel("U (V)")
plt.axis([0, 5000, -2, 2])

plt.tight_layout()
plt.show()