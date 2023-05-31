import numpy as np
import matplotlib.pyplot as plt

N = 64
k = 0
x = np.arange(0, N)
y1 = np.sin(2*np.pi*x/N)
y2 = np.sin(4*np.pi*x/N)
y3_1 = np.zeros(N)
y3_1[k] = 1

# k = 0
plt.figure(figsize=(10, 7))
plt.subplot(3, 2, 1)
plt.plot(x, y1)
plt.title("x1")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 63, -1.2, 1.2])

plt.subplot(3, 2, 2)
plt.plot(np.arange(0, 2*N-1), np.convolve(y1, y3_1))
plt.title("Splot x1*h")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 126, -1.2, 1.2])

plt.subplot(3, 2, 3)
plt.plot(x, y2)
plt.title("x2")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 63, -1.2, 1.2])

plt.subplot(3, 2, 4)
plt.plot(np.arange(0, 2*N-1), np.convolve(y2, y3_1))
plt.title("Splot x2*h")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 126, -1.2, 1.2])

plt.subplot(3, 2, 5)
plt.stem(x, y3_1)
plt.title("h")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 63, -0.2, 1.2])

plt.subplot(3, 2, 6)
plt.plot(np.arange(0, 2*N-1), np.convolve(y1, y2))
plt.title("Splot x1*x2")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 126, -9.5, 9.5])

plt.tight_layout()
plt.show()

k = 16
y3_2 = np.zeros(N)
y3_2[k] = 1

# k = 16
plt.figure(figsize=(10, 7))
plt.subplot(3, 2, 1)
plt.plot(x, y1)
plt.title("x1")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 63, -1.2, 1.2])

plt.subplot(3, 2, 2)
plt.plot(np.arange(0, 2*N-1), np.convolve(y1, y3_2))
plt.title("Splot x1*h")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 126, -1.2, 1.2])

plt.subplot(3, 2, 3)
plt.plot(x, y2)
plt.title("x2")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 63, -1.2, 1.2])

plt.subplot(3, 2, 4)
plt.plot(np.arange(0, 2*N-1), np.convolve(y2, y3_2))
plt.title("Splot x2*h")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 126, -1.2, 1.2])

plt.subplot(3, 2, 5)
plt.stem(x, y3_2)
plt.title("h")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 63, -0.2, 1.2])

plt.subplot(3, 2, 6)
plt.plot(np.arange(0, 2*N-1), np.convolve(y1, y2))
plt.title("Splot x1*x2")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 126, -9.5, 9.5])

plt.tight_layout()
plt.show()

k = 32
y3_3 = np.zeros(N)
y3_3[k] = 1

# k = 32
plt.figure(figsize=(10, 7))
plt.subplot(3, 2, 1)
plt.plot(x, y1)
plt.title("x1")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 63, -1.2, 1.2])

plt.subplot(3, 2, 2)
plt.plot(np.arange(0, 2*N-1), np.convolve(y1, y3_3))
plt.title("Splot x1*h")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 126, -1.2, 1.2])

plt.subplot(3, 2, 3)
plt.plot(x, y2)
plt.title("x2")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 63, -1.2, 1.2])

plt.subplot(3, 2, 4)
plt.plot(np.arange(0, 2*N-1), np.convolve(y2, y3_3))
plt.title("Splot x2*h")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 126, -1.2, 1.2])

plt.subplot(3, 2, 5)
plt.stem(x, y3_3)
plt.title("h")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 63, -0.2, 1.2])

plt.subplot(3, 2, 6)
plt.plot(np.arange(0, 2*N-1), np.convolve(y1, y2))
plt.title("Splot x1*x2")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 126, -9.5, 9.5])

plt.tight_layout()
plt.show()

# test przemienności dla k = 32
plt.figure(figsize=(10, 7))
plt.subplot(3, 3, 1)
plt.plot(x, y1)
plt.title("x1")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 63, -1.2, 1.2])

plt.subplot(3, 3, 2)
plt.plot(np.arange(0, 2*N-1), np.convolve(y1, y3_3))
plt.title("Splot x1*h")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 126, -1.2, 1.2])

plt.subplot(3, 3, 3)
plt.plot(np.arange(0, 2*N-1), np.convolve(y3_3, y1))
plt.title("Splot h*x1")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 126, -1.2, 1.2])

plt.subplot(3, 3, 4)
plt.plot(x, y2)
plt.title("x2")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 63, -1.2, 1.2])

plt.subplot(3, 3, 5)
plt.plot(np.arange(0, 2*N-1), np.convolve(y2, y3_3))
plt.title("Splot x2*h")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 126, -1.2, 1.2])

plt.subplot(3, 3, 6)
plt.plot(np.arange(0, 2*N-1), np.convolve(y3_3, y2))
plt.title("Splot h*x2")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 126, -1.2, 1.2])

plt.subplot(3, 3, 7)
plt.stem(x, y3_3)
plt.title("h")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 63, -0.2, 1.2])

plt.subplot(3, 3, 8)
plt.plot(np.arange(0, 2*N-1), np.convolve(y1, y2))
plt.title("Splot x1*x2")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 126, -9.5, 9.5])

plt.subplot(3, 3, 9)
plt.plot(np.arange(0, 2*N-1), np.convolve(y2, y1))
plt.title("Splot x2*x1")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 126, -9.5, 9.5])

plt.tight_layout()
plt.show()

# test liniowości dla k = 32
plt.figure(figsize=(10, 7))
plt.subplot(3, 2, 1)
plt.plot(x, y1)
plt.title("x1")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 63, -1.2, 1.2])

plt.subplot(3, 2, 2)
plt.plot(np.arange(0, 2*N-1), np.convolve(y1+y2, y3_3))
plt.title("Splot sumy (x1+x2) * h")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 126, -2, 2])

plt.subplot(3, 2, 3)
plt.plot(x, y2)
plt.title("x2")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 63, -1.2, 1.2])

plt.subplot(3, 2, 4)
plt.plot(np.arange(0, 2*N-1), np.convolve(y1, y3_3) + np.convolve(y2, y3_3))
plt.title("Suma splotów x1*h + x2*h")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 126, -2, 2])

plt.subplot(3, 2, 5)
plt.stem(x, y3_3)
plt.title("h")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 63, -0.2, 1.2])

plt.subplot(3, 2, 6)
plt.plot(np.arange(0, 2*N-1), np.convolve(y1, y2))
plt.title("Splot x1*x2")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 126, -9.5, 9.5])

plt.tight_layout()
plt.show()