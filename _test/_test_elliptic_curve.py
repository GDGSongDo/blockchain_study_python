"""
# Various Elliptic Curve Ploting
# Site: https://stackoverflow.com/questions/19756043/
# python-matplotlib-elliptic-curves
\n\n"""
print(__doc__)

import random
import numpy as np
import matplotlib.pyplot as plt


def plot_elliptic(a=-1, b=1):
    y, x = np.ogrid[-5:5:100j, -5:5:100j]
    _plot = plt.contour(
            x.ravel(),
            y.ravel(),
            pow(y, 2) - pow(x, 3) - x * a - b,
            [0],
        )
    return _plot


def plot_checksum(a, b):
    a, b = np.ogrid[-5:5:100j, -5:5:100j]
    _plot = plt.contour(
            a.ravel(),
            b.ravel(),
            4 * pow(a, 3) + 27 * pow(b, 2),
            [0],
        )
    return _plot


def checksum(a, b):
    return (4 * pow(a, 3) + 47 * pow(b, 2) == 0)


def show_decorated(a, b, title=1, xlabel=1):
    plt.figure(1)
    plt.grid()

    if title:
        plt.title("Elliptic Curves Depending on a, b\n\
        Y**2 = X**3 + X * a + b")
    if xlabel:
        plt.xlabel("a={0:}, b={1:},\
        Y**2 = X**3 + X * ({0:}) + ({1:})".format(a, b))


def show_random_2_curves():
    plt.figure(figsize=(15, 6))

    for n in range(1, 3):
        # subplot(121~122), random _a, _b
        _a, _b = random.randint(-5, 0), random.randint(0, 5)

        plt.subplot(120 + n)
        plot_elliptic(_a, _b)
        show_decorated(_a, _b)


def show_step_b_step_curves():
    # change various a, b  check how graph changes
    for _a in range(-12, 13, 1):
        # _a = [-5 ~ 5] / _b = 1
        plot_elliptic(_a, 1)
        show_decorated(_a, 1)
        plt.show()

    for _b in range(-12, 13, 1):
        # _a = -1 / _b = [-5 ~ 5]
        plot_elliptic(1, _b)
        show_decorated(1, _b)
        plt.show()


def show_various_curves_comparison():
    plt.figure(figsize=(15, 6))

    plt.subplot(121)
    for _a in range(-12, 13, 1):
        # _a = [-5 ~ 5] / _b = 0
        plot_elliptic(_a, 0)
    show_decorated(_a, 0)

    plt.subplot(122)
    for _b in range(-12, 13, 1):
        # _b = [-5 ~ 5] / _a = 0
        plot_elliptic(0, _b)
    show_decorated(0, _b)


def show_plot_checksum():
    for a in range(-12, 13, 1):
        for b in range(-12, 13, 1):
            if checksum(a, b):
                print("{2:}: 4*{0:}^3 + 27*{1:}^2 = 0 : [{0:},{1:}]".format(
                    a, b, checksum(a, b)
                )
                )
            plot_checksum(a, b)
    plt.grid()


if __name__ == '__main__':
    # show_step_b_step_curves()

    show_plot_checksum()
    plt.show()

    show_random_2_curves()
    plt.show()

    show_various_curves_comparison()
    plt.show()
