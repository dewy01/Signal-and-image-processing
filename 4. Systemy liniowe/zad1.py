import numpy as np
import matplotlib.pyplot as plt

N = 32
x = np.arange(0, N)
y1 = np.sin(2*np.pi*x/(N-1))
y2 = np.ones(N)

# a
S1 = 2*(y1 + y2)
S2 = 2*y1 + 2*y2

# b
S3 = (y1 + y2) + 1
S4 = (y1 + 1) + (y2 + 1)

# c
S5 = np.zeros(N-1)
S6 = np.zeros(N-1)
for i in range(N-1):
    S5[i] = (y1[i+1] + y2[i+1]) - (y1[i] + y2[i])
    S6[i] = (y1[i+1] - y1[i]) + (y2[i+1] - y2[i])

plt.figure(figsize=(12, 8))

# Plot 1
plt.subplot(2, 2, 1)
plt.stem(x, y1)
plt.title("x1[n]")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 31, -1.2, 1.2])

# Plot 2
plt.subplot(2, 2, 2)
plt.stem(x, y2)
plt.title("x2[n]")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 31, 0, 2])

# Plot 3
plt.subplot(2, 2, 3)
plt.stem(x, S1)
plt.title("S{x1[n]+x2[n]}")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 31, -0.2, 4.2])

# Plot 4
plt.subplot(2, 2, 4)
plt.stem(x, S2)
plt.title("S{x1[n]}+S{x2[n]}")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 31, -0.2, 4.2])

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))

# Plot 5
plt.subplot(2, 2, 1)
plt.stem(x, y1)
plt.title("x1[n]")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 31, -1.2, 1.2])

# Plot 6
plt.subplot(2, 2, 2)
plt.stem(x, y2)
plt.title("x2[n]")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 31, 0, 2])

# Plot 7
plt.subplot(2, 2, 3)
plt.stem(x, S3)
plt.title("S{x1[n]+x2[n]}")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 31, 0.8, 4.2])

# Plot 8
plt.subplot(2, 2, 4)
plt.stem(x, S4)
plt.title("S{x1[n]}+S{x2[n]}")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 31, 0.8, 4.2])

plt.tight_layout()
plt.show()

plt.figure(figsize=(12, 8))

# Plot 9
plt.subplot(2, 2, 1)
plt.stem(x, y1)
plt.title("x1[n]")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 31, -1.2, 1.2])

# Plot 10
plt.subplot(2, 2, 2)
plt.stem(x, y2)
plt.title("x2[n]")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 31, 0, 2])

# Plot 11
plt.subplot(2, 2, 3)
plt.stem(np.arange(0, N-1), S5)
plt.title("S{x1[n]+x2[n]}")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 31, -0.5, 0.5])

# Plot 12
plt.subplot(2, 2, 4)
plt.stem(np.arange(0, N-1), S6)
plt.title("S{x1[n]}+S{x2[n]}")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([0, 31, -0.5, 0.5])

plt.tight_layout()
plt.show()