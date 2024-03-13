import math
import sys

import matplotlib.pyplot as plt
import numpy as np



def function_1(x):
    return (x ** 4) - 4 * (x ** 3) + 8 * (x ** 2) - 23


def function_2(x):
    return 2 * np.sin(x) * x ** 2


def function_3(x):
    return np.cos(x)


def function_4(x):
    return (3 ** x) - 3


def function_5(x):
    return 2 * np.cos(x * x)


def value(x, function):
    if function == '1':
        return function_1(x)
    elif function == '2':
        return function_2(x)
    elif function == '3':
        return function_3(x)
    elif function == '4':
        return function_4(x)
    elif function == '5':
        return function_5(x)


def bisection(a, b, function, iteration, epsilon=None):
    if value(a, function) * value(b, function) >= 0:
        return "You have not assumed right a and b"
    else:
        i = 0
        while  i < iteration:
            x = (a + b) / 2
            value_of_a = value(a, function)
            value_of_b = value(b, function)
            value_of_x = value(x, function)
            if value_of_x == 0:
                return x, i

            # Check if the root is in the left half
            elif value_of_x * value_of_b < 0:
                a = x
            # Check if the root is in the right half
            elif value_of_x * value_of_a < 0:
                b = x
            i += 1

        return x, i


def second_method(x1, x2, function, iteration, epsilon=None):
    f1 = value(x1, function)
    f2 = value(x2, function)
    for i in range(0, iteration):
        # Float limitations
        if f1 - f2 == 0.0:
            return x0, i

        x0 = x1 - f1 * (x1 - x2) / (f1 - f2)
        f0 = value(x0, function)
        if f0 == 0.0:
            return x0, i
        else:
            x2 = x1
            f2 = f1
            x1 = x0
            f1 = f0
    return x0, i + 1


def draw_plot(function, calculatedValue):
    x = np.linspace(-5, 5, 100)
    y = value(x, function)
    fig, ax = plt.subplots()
    ax.plot(x, y)
    #plt.plot(np.array(calculatedValue), np.array(value(calculatedValue, function)), 'o')
    ax.set_xlim(-5, 5)
    ax.set_ylim(-2, 2)
    ax.grid(True, which="both")
    ax.set_aspect('equal')
    ax.axhline(y=0, color='k')
    ax.axvline(x=0, color='k')
    plt.show()
