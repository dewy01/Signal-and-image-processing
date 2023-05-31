import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 5, 200)
y1 = np.sin(2*np.pi*x)
y2 = np.sign(np.sin(2*np.pi*x))
y3 = np.sign(np.sin(2*np.pi*x))

plt.figure(figsize=(8, 8))
plt.subplot(3, 1, 1)
plt.plot(x, y1)
plt.title("Przebieg periodyczny sygnału sinusoidalnego", fontsize=14)
plt.xlabel("t (ms)")
plt.ylabel("U (V)")
plt.axis([0, 5, -1.2, 1.2])

plt.subplot(3, 1, 2)
plt.plot(x, y2)
plt.title("Przebieg periodyczny sygnału piłokształtnego", fontsize=14)
plt.xlabel("t (ms)")
plt.ylabel("U (V)")
plt.axis([0, 5, -1.2, 1.2])

plt.subplot(3, 1, 3)
plt.plot(x, y3)
plt.title("Przebieg periodyczny sygnału prostokątnego", fontsize=14)
plt.xlabel("t (ms)")
plt.ylabel("U (V)")
plt.axis([0, 5, -1.2, 1.2])

plt.tight_layout()
plt.show()
