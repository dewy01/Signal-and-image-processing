import numpy as np
import matplotlib.pyplot as plt

Fs = 32
t = 160
P = 2 * Fs * t // 100 # Podziałka fft
x = np.linspace(0, t - 1 / Fs, t * Fs)

y1 = np.cos(2 * np.pi * x / Fs + np.pi / 4)
y2 = 0.5 * np.cos(4 * np.pi * x / Fs)
y3 = 0.25 * np.cos(8 * np.pi * x / Fs + np.pi / 2)
y4 = y1 + y2 + y3

Y1 = np.fft.fft(y1)
Y2 = np.fft.fft(y2)
Y3 = np.fft.fft(y3)
Y4 = np.fft.fft(y4)

Y1_l = Y1[:Fs * t // P]
Y2_l = Y2[:Fs * t // P]
Y3_l = Y3[:Fs * t // P]
Y4_l = Y4[:Fs * t // P]

Y1_m = np.abs(Y1_l) / (Fs * t / 2)
Y2_m = np.abs(Y2_l) / (Fs * t / 2)
Y3_m = np.abs(Y3_l) / (Fs * t / 2)
Y4_m = np.abs(Y4_l) / (Fs * t / 2)

xFFT = np.arange(Fs * t // P) / t

plt.figure(figsize=(9, 6))

plt.subplot(4, 2, 1)
plt.plot(x, y1)
plt.title("y1")
plt.xlabel("t (sek)")
plt.ylabel("U (V)")
plt.axis([0, 159, -1.1, 1.1])

plt.subplot(4, 2, 2)
plt.stem(xFFT, Y1_m)
plt.title("Y1")
plt.xlabel("f (Hz)")
plt.ylabel("Amplituda")
plt.axis([0, 0.3, -0.1, 1.1])

plt.subplot(4, 2, 3)
plt.plot(x, y2)
plt.title("y2")
plt.xlabel("t (sek)")
plt.ylabel("U (V)")
plt.axis([0, 159, -0.6, 0.6])

plt.subplot(4, 2, 4)
plt.stem(xFFT, Y2_m)
plt.title("Y2")
plt.xlabel("f (Hz)")
plt.ylabel("Amplituda")
plt.axis([0, 0.3, -0.1, 1.1])

plt.subplot(4, 2, 5)
plt.plot(x, y3)
plt.title("y3")
plt.xlabel("t (sek)")
plt.ylabel("U (V)")
plt.axis([0, 159, -0.3, 0.3])

plt.subplot(4, 2, 6)
plt.stem(xFFT, Y3_m)
plt.title("Y3")
plt.xlabel("f (Hz)")
plt.ylabel("Amplituda")
plt.axis([0, 0.3, -0.1, 1.1])

plt.subplot(4, 2, 7)
plt.plot(x, y4)
plt.title("y4")
plt.xlabel("t (sek)")
plt.ylabel("U (V)")

plt.subplot(4, 2, 8)
plt.stem(xFFT, Y4_m)
plt.title("Y4")
plt.xlabel("f (Hz)")
plt.ylabel("Amplituda")
plt.axis([0, 0.3, -0.1, 1.1])

Y1_a = np.angle(Y1)
Y2_a = np.angle(Y2)
Y3_a = np.angle(Y3)
Y4_a = np.angle(Y4)
Y1_a = Y1_a[:Fs * t // P]
Y2_a = Y2_a[:Fs * t // P]
Y3_a = Y3_a[:Fs * t // P]
Y4_a = Y4_a[:Fs * t // P]

plt.figure(figsize=(9, 6))

plt.subplot(2, 2, 1)
plt.stem(xFFT, Y1_a)
plt.yticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
['-pi', '-pi/2', '0', 'pi/2', 'pi'])
plt.title("Kąt Y1")
plt.xlabel("f (Hz)")
plt.ylabel("fi (rad)")
plt.axis([0, 0.3, -4, 4])

plt.subplot(2, 2, 2)
plt.stem(xFFT, Y2_a)
plt.yticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
['-pi', '-pi/2', '0', 'pi/2', 'pi'])
plt.title("Kąt Y2")
plt.xlabel("f (Hz)")
plt.ylabel("fi (rad)")
plt.axis([0, 0.3, -4, 4])

plt.subplot(2, 2, 3)
plt.stem(xFFT, Y3_a)
plt.yticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
['-pi', '-pi/2', '0', 'pi/2', 'pi'])
plt.title("Kąt Y3")
plt.xlabel("f (Hz)")
plt.ylabel("fi (rad)")
plt.axis([0, 0.3, -4, 4])

plt.subplot(2, 2, 4)
plt.stem(xFFT, Y4_a)
plt.yticks([-np.pi, -np.pi / 2, 0, np.pi / 2, np.pi],
['-pi', '-pi/2', '0', 'pi/2', 'pi'])
plt.title("Kąt Y4")
plt.xlabel("f (Hz)")
plt.ylabel("fi (rad)")
plt.axis([0, 0.3, -4, 4])

plt.tight_layout()
plt.show()