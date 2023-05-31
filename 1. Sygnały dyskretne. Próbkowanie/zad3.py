import numpy as np
import matplotlib.pyplot as plt

f = 1000
a = 1
fs_values = [8000, 2000, 1100]
t = 0.007

fig, axs = plt.subplots(3, 1, figsize=(6, 10))

for i, fs in enumerate(fs_values):
    x = np.arange(0, t, 1 / fs)
    y = a * np.sin(2 * np.pi * f * x)
    axs[i].plot(x, y, '*-')
    axs[i].axis([0, t, -1.5, 1.5])
    axs[i].set_title("fs = {}Hz, f = {}Hz".format(fs, f))
    axs[i].set_ylabel("Amplituda [V]")
    axs[i].set_xlabel("Czas [sek.]")

plt.tight_layout()
plt.show()
