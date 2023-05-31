import numpy as np
import matplotlib.pyplot as plt

N = 64
x = np.arange(0, N)
y1 = np.sin(2 * np.pi * x / N)
y2 = np.exp(-x / 10)
Y1 = np.fft.fft(y1, N)
Y2 = np.fft.fft(y2, N)
G1 = Y1 * Y2

plt.figure(figsize=(12, 10))
plt.subplot(3, 2, 1)
plt.plot(x, y1)
plt.title("x1[n]")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 63, -1.2, 1.2])

plt.subplot(3, 2, 2)
plt.plot(x, y2)
plt.title("h[n]")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 63, -0.2, 1.2])

plt.subplot(3, 2, 3)
plt.stem(x, np.abs(Y1))
plt.title("fft(x1[n])")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 63, 0, 40])

plt.subplot(3, 2, 4)
plt.stem(x, np.abs(Y2))
plt.title("fft(h[n])")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 63, 0, 12])

plt.subplot(3, 2, 5)
plt.plot(x, np.fft.ifft(G1, N))
plt.title("ifft(G)")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 63, -10, 10])

G2 = np.convolve(y1, y2)
plt.subplot(3, 2, 6)
plt.plot(x, G2[:N])
plt.title("splot x1[n]*h[n]")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 63, -10, 10])

plt.tight_layout()
plt.show()

plt.figure(figsize=(8, 6))
plt.plot(x, np.fft.ifft(G1, N), label="ifft(X1*H)")
plt.plot(x, G2[:N], label="conv(x1, h)")
plt.legend()
plt.title("Porównanie splotu i wymnożonej odwrotnej transformaty x1[n] i h[n]")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 63, -10, 10])
plt.show()
