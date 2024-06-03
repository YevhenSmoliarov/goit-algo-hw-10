#1. Візуалізація функції та області інтегрування
import matplotlib.pyplot as plt
import numpy as np

# Визначення функції та межі інтегрування
def f(x):
    return x ** 2

a = 0  # Нижня межа
b = 2  # Верхня межа

# Створення діапазону значень для x
x = np.linspace(-0.5, 2.5, 400)
y = f(x)

# Створення графіка
fig, ax = plt.subplots()

# Малювання функції
ax.plot(x, y, 'r', linewidth=2)

# Заповнення області під кривою
ix = np.linspace(a, b)
iy = f(ix)
ax.fill_between(ix, iy, color='gray', alpha=0.3)

# Налаштування графіка
ax.set_xlim([x[0], x[-1]])
ax.set_ylim([0, max(y) + 0.1])
ax.set_xlabel('x')
ax.set_ylabel('f(x)')

# Додавання меж інтегрування та назви графіка
ax.axvline(x=a, color='gray', linestyle='--')
ax.axvline(x=b, color='gray', linestyle='--')
ax.set_title('Графік інтегрування f(x) = x^2 від ' + str(a) + ' до ' + str(b))
plt.grid()
plt.show()

#2. Обчислення інтегралу методом Монте-Карло
import random

def monte_carlo_integration(func, a, b, num_samples=10000):
    total_sum = 0
    for _ in range(num_samples):
        x = random.uniform(a, b)
        total_sum += func(x)
    return (b - a) * total_sum / num_samples

# Використання методу Монте-Карло для обчислення інтегралу
num_samples = 10000
monte_carlo_result = monte_carlo_integration(f, a, b, num_samples)
print(f"Інтеграл методом Монте-Карло: {monte_carlo_result}")

#3. Перевірка результату за допомогою функції quad з SciPy
import scipy.integrate as spi

# Обчислення інтеграла за допомогою функції quad
result, error = spi.quad(f, a, b)
print("Інтеграл за допомогою quad: ", result)

#4. Порівняння та висновки
print(f"Інтеграл методом Монте-Карло: {monte_carlo_result}")
print(f"Інтеграл за допомогою quad: {result}")