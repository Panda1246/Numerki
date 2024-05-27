import math
import numpy as np


def Horner_value(x, values, lenght):
    final_value = 0
    for i in range(lenght):
        final_value = final_value * x + values[i]
    return final_value


def function_1(x):
    return (8 * x) + 3, np.ones_like(x) * 8

def function_2(x):
    return np.abs(x - 5), (x-5)/np.abs(x-5)


def function_3(x):
    return Horner_value(x, [-2, 1, 1], 3), Horner_value(x, [-4, 1], 2)


def function_4(x):
    return np.cos(x) / x, (-x*np.sin(x)-np.cos(x))/x**2


def function_5(x):
    return np.sin(x) - 2 * np.cos(x - 5), np.cos(x) + 2*np.sin(x-5)

def horner_scheme(coefficients, x, z):
    n = len(coefficients)
    result = coefficients[-1]
    for i in range(n - 2, -1, -1):
        result = result * (x - z[i]) + coefficients[i]
    return result
def function( fun):
    if fun == '1':
        return function_1
    elif fun == '2':
        return function_2
    elif fun == '3':
        return function_3
    elif fun == '4':
        return function_4
    elif fun == '5':
        return function_5
def hermite_interpolation_coefficients(x, y, dy):
    n = len(x)
    z = np.zeros(2 * n)
    Q = np.zeros((2 * n, 2 * n))

    for i in range(n):
        z[2 * i] = z[2 * i + 1] = x[i]
        Q[2 * i, 0] = Q[2 * i + 1, 0] = y[i]
        Q[2 * i + 1, 1] = dy[i]

        if i != 0:
            Q[2 * i, 1] = (Q[2 * i, 0] - Q[2 * i - 1, 0]) / (z[2 * i] - z[2 * i - 1])

    for i in range(2, 2 * n):
        for j in range(2, i + 1):
            Q[i, j] = (Q[i, j - 1] - Q[i - 1, j - 1]) / (z[i] - z[i - j])

    return z, Q.diagonal()


def polynomial_to_string(coefficients, degree):
    result = f"{coefficients[0]:.2f}"
    for i in range(1, degree+1):
        # if coefficients[i]==0:
        #     continue
        # else:
        result += f" + {coefficients[i]:.2f}x^{i}"
    return result