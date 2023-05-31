import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile
import soundfile as sf


def my_env(y, a):
    N = len(y)
    env = np.zeros(N)
    env[0] = y[0]
    for i in range(1, N):
        env[i] = a * env[i-1] + (1 - a) * y[i] * y[i]
    return env

f = 1000
Fs = 8000
t = 5
x = np.arange(0, t+1/Fs, 1/Fs)
Fs_audio, y_audio = wavfile.read("sound.wav")
y_audio = 10 * y_audio[:int(Fs*t)+1].astype(float)

y_gauss = np.random.randn(Fs*t+1)
y_sin_s = np.sin(2 * np.pi * x * f)
y_sin_m = np.cos(2 * np.pi * x * f * x * x)

y_a999 = my_env(y_audio, 0.999)
y_g999 = my_env(y_gauss, 0.999)
y_s999 = my_env(y_sin_s, 0.999)
y_m999 = my_env(y_sin_m, 0.999)

y_a990 = my_env(y_audio, 0.990)
y_g990 = my_env(y_gauss, 0.990)
y_s990 = my_env(y_sin_s, 0.990)
y_m990 = my_env(y_sin_m, 0.990)

y_a500 = my_env(y_audio, 0.500)
y_g500 = my_env(y_gauss, 0.500)
y_s500 = my_env(y_sin_s, 0.500)
y_m500 = my_env(y_sin_m, 0.500)

y_a001 = my_env(y_audio, 0.001)
y_g001 = my_env(y_gauss, 0.001)
y_s001 = my_env(y_sin_s, 0.001)
y_m001 = my_env(y_sin_m, 0.001)

fig = plt.figure(figsize=(9, 7))

# First set of plots
ax1 = fig.add_subplot(421)
ax1.plot(x, y_audio)
ax1.set(title="Ścieżka audio", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[-4, 4])

ax2 = fig.add_subplot(422)
ax2.plot(x, y_a999)
ax2.set(title="Ścieżka audio - obwiednica mocy α=0.999", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[0, 1])

ax3 = fig.add_subplot(423)
ax3.plot(x, y_gauss)
ax3.set(title="Szum gaussowski", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[-5, 5])

ax4 = fig.add_subplot(424)
ax4.plot(x, y_g999)
ax4.set(title="Szum gaussowski - obwiednica mocy α=0.999", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[0, 1.5])

ax5 = fig.add_subplot(425)
ax5.plot(x, y_sin_s)
ax5.set(title="Sinus stały", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 0.05], ylim=[-1.5, 1.5])

ax6 = fig.add_subplot(426)
ax6.plot(x, y_s999)
ax6.set(title="Sinus stały - obwiednica mocy α=0.999", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[0, 0.6])

ax7 = fig.add_subplot(427)
ax7.plot(x, y_sin_m)
ax7.set(title="Sinus zmienny", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 1], ylim=[-1.5, 1.5])

ax8 = fig.add_subplot(428)
ax8.plot(x, y_m999)
ax8.set(title="Sinus zmienny - obwiednica mocy α=0.999", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[0.4, 1.1])

plt.tight_layout()
plt.show()

fig2 = plt.figure(figsize=(9, 7))

# Second set of plots
ax1 = fig2.add_subplot(421)
ax1.plot(x, y_audio)
ax1.set(title="Ścieżka audio", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[-4, 4])

ax2 = fig2.add_subplot(422)
ax2.plot(x, y_a990)
ax2.set(title="Ścieżka audio - obwiednica mocy α=0.990", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[-0.5, 2.5])

ax3 = fig2.add_subplot(423)
ax3.plot(x, y_gauss)
ax3.set(title="Szum gaussowski", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[-5, 5])

ax4 = fig2.add_subplot(424)
ax4.plot(x, y_g990)
ax4.set(title="Szum gaussowski - obwiednica mocy α=0.990", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[0, 1.5])

ax5 = fig2.add_subplot(425)
ax5.plot(x, y_sin_s)
ax5.set(title="Sinus stały", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 0.05], ylim=[-1.5, 1.5])

ax6 = fig2.add_subplot(426)
ax6.plot(x, y_s990)
ax6.set(title="Sinus stały - obwiednica mocy α=0.990", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[0, 0.6])

ax7 = fig2.add_subplot(427)
ax7.plot(x, y_sin_m)
ax7.set(title="Sinus zmienny", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 1], ylim=[-1.5, 1.5])

ax8 = fig2.add_subplot(428)
ax8.plot(x, y_m990)
ax8.set(title="Sinus zmienny - obwiednica mocy α=0.990", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[-0.1, 1.1])

plt.tight_layout()
plt.show()

fig3 = plt.figure(figsize=(9, 7))

# Third set of plots
ax1 = fig3.add_subplot(421)
ax1.plot(x, y_audio)
ax1.set(title="Ścieżka audio", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[-4, 4])

ax2 = fig3.add_subplot(422)
ax2.plot(x, y_a500)
ax2.set(title="Ścieżka audio - obwiednica mocy α=0.500", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[-0.5, 12])

ax3 = fig3.add_subplot(423)
ax3.plot(x, y_gauss)
ax3.set(title="Szum gaussowski", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[-5, 5])

ax4 = fig3.add_subplot(424)
ax4.plot(x, y_g500)
ax4.set(title="Szum gaussowski - obwiednica mocy α=0.500", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[-0.5, 12])

ax5 = fig3.add_subplot(425)
ax5.plot(x, y_sin_s)
ax5.set(title="Sinus stały", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 0.05], ylim=[-1.5, 1.5])

ax6 = fig3.add_subplot(426)
ax6.plot(x, y_s500)
ax6.set(title="Sinus stały - obwiednica mocy α=0.500", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[0, 1])

ax7 = fig3.add_subplot(427)
ax7.plot(x, y_sin_m)
ax7.set(title="Sinus zmienny", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 1], ylim=[-1.5, 1.5])

ax8 = fig3.add_subplot(428)
ax8.plot(x, y_m500)
ax8.set(title="Sinus zmienny - obwiednica mocy α=0.500", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[-0.1, 1.1])

plt.tight_layout()
plt.show()

fig4 = plt.figure(figsize=(9, 7))

# Fourth set of plots
ax1 = fig4.add_subplot(421)
ax1.plot(x, y_audio)
ax1.set(title="Ścieżka audio", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[-4, 4])

ax2 = fig4.add_subplot(422)
ax2.plot(x, y_a001)
ax2.set(title="Ścieżka audio - obwiednica mocy α=0.001", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[-0.5, 20])

ax3 = fig4.add_subplot(423)
ax3.plot(x, y_gauss)
ax3.set(title="Szum gaussowski", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[-5, 5])

ax4 = fig4.add_subplot(424)
ax4.plot(x, y_g001)
ax4.set(title="Szum gaussowski - obwiednica mocy α=0.001", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[-0.5, 20])

ax5 = fig4.add_subplot(425)
ax5.plot(x, y_sin_s)
ax5.set(title="Sinus stały", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 0.05], ylim=[-1.5, 1.5])

ax6 = fig4.add_subplot(426)
ax6.plot(x, y_s001)
ax6.set(title="Sinus stały - obwiednica mocy α=0.001", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[0, 0.2])

ax7 = fig4.add_subplot(427)
ax7.plot(x, y_sin_m)
ax7.set(title="Sinus zmienny", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 1], ylim=[-1.5, 1.5])

ax8 = fig4.add_subplot(428)
ax8.plot(x, y_m001)
ax8.set(title="Sinus zmienny - obwiednica mocy α=0.001", xlabel="t (sek)", ylabel="U (V)", xlim=[0, 5], ylim=[-0.1, 1.1])

plt.tight_layout()
plt.show()
