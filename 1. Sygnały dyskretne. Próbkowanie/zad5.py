import numpy as np
import sounddevice as sd

Fs = 8192 # próbkowanie
time = 18 # sekundy
C5 = 523.25
D5 = 587.33
E5 = 659.26
F5 = 698.46
G5 = 783.99

t4 = np.linspace(0, 0.5, int(0.5 * Fs))

y1 = np.sin(2 * np.pi * G5 * t4)
y2 = np.sin(2 * np.pi * E5 * t4)
y3 = np.sin(2 * np.pi * F5 * t4)
y4 = np.sin(2 * np.pi * D5 * t4)
y5 = np.sin(2 * np.pi * C5 * t4)

y7_1 = np.sin(2 * np.pi * G5 * t4)
y7_2 = np.sin(2 * np.pi * C5 * t4)
y8 = np.zeros_like(t4)

yAll_1 = np.concatenate((y1, y2, y2, y3, y4, y4, y5, y7_1, y8))
yAll_2 = np.concatenate((y1, y2, y2, y3, y4, y4, y5, y7_2, y8))
yAll = np.concatenate((yAll_1, yAll_2, yAll_1, yAll_2))

#Play the sound
sd.play(yAll, Fs)
sd.wait()