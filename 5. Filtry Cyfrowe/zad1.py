import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import freqz, tf2zpk
from numpy.polynomial import Polynomial

def funkcja(x, a, b):
    y = np.zeros(len(x))
    y[0] = b[0] * x[0]
    y[1] = b[0] * x[1] + b[1] * x[0] - a[1] * y[0]
    n = 2
    while n < len(x):
        y[n] = b[0] * x[n] + b[1] * x[n-1] + b[2] * x[n-2] - a[1] * y[n-1] - a[2] * y[n-2]
        n += 1
    return y

def printPlot(x, y, sORp, tl, xl, yl, ax):
    if sORp == 's':
        plt.stem(x, y)
    elif sORp == 'p':
        plt.plot(x, y)
    else:
        return
    plt.title(tl)
    plt.xlabel(xl)
    plt.ylabel(yl)
    plt.axis(ax)

b = [0.1, 0.2, 0.3]
a = [1.0, 0.9, 0.1]
N = 64
impuls = np.zeros(N)
impuls[1] = 1
odpImpuls = funkcja(impuls, a, b)
odpWbud = np.convolve(impuls, b, mode='full')

plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
printPlot(np.arange(1, N+1), odpImpuls, 's', "Odpowiedź impulsowa filtru naszą funkcją", "Nr. próbki", "Amplituda", [0, N+1, -0.25, 0.25])
plt.subplot(2, 1, 2)
printPlot(np.arange(1, N+1), odpWbud[:N], 's', "Odpowiedź impulsowa filtru wbudowaną funkcją", "Nr. próbki", "Amplituda", [0, N+1, -0.25, 0.25])

w, h = freqz(b, a)
modH = np.abs(h)
f_zn = w / np.pi

plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
printPlot(f_zn, 10 * np.log10(modH), 'p', "Charakterystyka amplitudowa filtru", "Częstotliwość znormalizowana", "Magnituda", [0, 1, -8, 0.5])
plt.subplot(2, 1, 2)
printPlot(f_zn, np.unwrap(np.angle(h)) / np.pi, 'p', "Charakterystyka fazowa filtru", "Częstotliwość znormalizowana", "Radiany", [0, 1, -1.2, 1.2])

z, biegun, _ = tf2zpk(b, a)
p = Polynomial.fromroots(np.ones(1000))

plt.figure(figsize=(8, 6))
plt.scatter(np.real(z), np.imag(z), color='blue')
plt.scatter(np.real(biegun), np.imag(biegun), marker='x')
plt.plot(p.coef.real, p.coef.imag, color='red')
plt.title("Wykres biegunów i zer filtru")
plt.xlabel("Część rzeczywista")
plt.ylabel("Część urojona")
plt.legend(["Zero", "Biegun"])
plt.grid(True)
plt.show()

x = np.random.randn(N)
yd = funkcja(x, a, b)
X = np.fft.fft(x)
modX = np.abs(X)
Y = np.fft.fft(yd)
modY = np.abs(Y)

plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.plot(x)
plt.title("Szum gaussowski")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([1, N, -3, 3])
plt.subplot(2, 1, 2)
plt.plot(yd)
plt.title("Przefiltrowany szum gaussowski")
plt.xlabel("Nr. próbki")
plt.ylabel("Amplituda")
plt.axis([1, N, -3, 3])
plt.show()

plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.plot(modX * 2 / N)
plt.title("Widmo szumu gaussowskiego")
plt.xlabel("Nr. pasma częstotliwościowego")
plt.ylabel("Amplituda")
plt.axis([1, 32, 0, 0.8])
plt.subplot(2, 1, 2)
plt.plot(modY * 2 / N)
plt.title("Widmo przefiltrowanego szumu gaussowskiego")
plt.xlabel("Nr. pasma częstotliwościowego")
plt.ylabel("Amplituda")
plt.axis([1, 32, 0, 0.8])
plt.show()
