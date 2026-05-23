import random
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi


# Функція
def f(x):
    return x ** 2


def main():
    # Межі інтегрування
    a = 0
    b = 2

    # Побудова графіка
    x = np.linspace(-0.5, 2.5, 400)
    y = f(x)

    fig, ax = plt.subplots()

    ax.plot(x, y, 'r', linewidth=2)

    ix = np.linspace(a, b)
    iy = f(ix)

    ax.fill_between(ix, iy, color='gray', alpha=0.3)

    ax.set_xlim([x[0], x[-1]])
    ax.set_ylim([0, max(y) + 0.1])

    ax.set_xlabel('x')
    ax.set_ylabel('f(x)')

    ax.axvline(x=a, color='gray', linestyle='--')
    ax.axvline(x=b, color='gray', linestyle='--')

    ax.set_title('Графік інтегрування f(x) = x^2 від 0 до 2')

    plt.grid()
    plt.show()

    # Метод Монте-Карло
    N = 100000

    inside_points = 0

    # Максимальна висота графіка
    y_max = f(b)

    for _ in range(N):
        random_x = random.uniform(a, b)
        random_y = random.uniform(0, y_max)

        if random_y <= f(random_x):
            inside_points += 1

    # Площа прямокутника
    rectangle_area = (b - a) * y_max

    # Наближене значення інтеграла
    monte_carlo_result = (inside_points / N) * rectangle_area

    print("Метод Монте-Карло:")
    print(monte_carlo_result)

    # Перевірка через scipy.quad
    quad_result, error = spi.quad(f, a, b)

    print("\nПеревірка через scipy.quad:")
    print("Інтеграл:", quad_result)
    print("Похибка:", error)

    # Аналітичне значення
    analytic_result = (b ** 3) / 3 - (a ** 3) / 3

    print("\nАналітичний результат:")
    print(analytic_result)


if __name__ == "__main__":
    main()