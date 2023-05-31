import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 100, 200)
y = np.sqrt(0.5) * np.random.randn(200)
plt.plot(x, y)
average = np.mean(y)
standard_deviation = np.std(y)
variance = np.var(y)
plt.title("Szum Gaussowski (200 próbek) dla średniej: {:.4f} i wariancji: {:.4f}".format(average, variance))
plt.xlabel("t (ms)")
plt.ylabel("U (V)")
plt.figure(figsize=(6, 5))
plt.show()
