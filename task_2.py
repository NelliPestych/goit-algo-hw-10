import numpy as np

# Визначення функції
def f(x):
    return x ** 2

# Межі інтегрування
a, b = 0, 2
n = 100000  # Кількість випадкових точок

# Генерація випадкових точок
x_random = np.random.uniform(a, b, n)
y_random = f(x_random)

# Обчислення інтегралу
integral_mc = (b - a) * np.mean(y_random)
print(f"Інтеграл (Монте-Карло): {integral_mc}")

# Аналітичне обчислення для перевірки
import scipy.integrate as spi

result, error = spi.quad(f, a, b)
print(f"Інтеграл (аналітичний): {result}")
