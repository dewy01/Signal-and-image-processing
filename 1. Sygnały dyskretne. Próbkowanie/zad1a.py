import numpy as np
import matplotlib.pyplot as plt

def kronecker_delta(x, value):
    return np.where(x == value, 1, 0)

x = np.linspace(-10, 50, 61)
y1 = kronecker_delta(x, 0)
y2 = kronecker_delta(x, 40)

plt.stem(x, y1, use_line_collection=True, label='Impuls jednostkowy')
plt.stem(x, y2, use_line_collection=True, label='Przesunięty impuls')
plt.axis([-10, 50, 0, 1.2])
plt.title("Impuls jednostkowy i przesunięty o 40 próbek")
plt.xlabel("Numer próbki")
plt.ylabel("Wartość próbki")
plt.legend()
plt.show()
