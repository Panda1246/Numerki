import math


def Horner_value(x, values, lenght):
    final_value = 0
    for i in range(lenght):
        final_value = final_value * x + values[i]
    return final_value


def function_1(x, coffecients, length):
    return Horner_value(x, coffecients, length)


def function_2(x):
    return x - 3


def function_3(x):
    return math.cos(x)


def function_4(x):
    return math.fabs(x)


def function_5(x):
    return 2 * math.cos(x * x)


def value(x, function):
    if function == '1':
        return function_1(x, [1, -4, 0, 8, -23], 5)
    elif function == '2':
        return function_2(x)
    elif function == '3':
        return function_3(x)
    elif function == '4':
        return function_4(x)
    elif function == '5':
        return function_5(x)


def nodes(a, b, n):
    x = [0] * n
    x[0] = float(a)
    float(n)
    for i in range(n - 1):
        x[i + 1] = float(x[i]) + float(b - a) / float(n - 1)
    return x


def divided_diff(x, y):
    n = len(y)
    coef = [0] * n
    coef[0] = y[0]
    for j in range(1, n):
        for i in range(n - 1, j - 1, -1):
            y[i] = (y[i] - y[i - 1]) / (x[i] - x[i - j])
            coef[j] = y[j]
    return coef


def newton_interpolation(x, y, xi):
    n = len(x)
    coef = divided_diff(x, y)
    result = coef[0]
    temp = 1
    for i in range(1, n):
        temp *= (xi - x[i - 1])
        result += coef[i] * temp
    return result


def choice(a, b, n, function, x1):
    nodes_x = nodes(a, b, n)
    nodes_y = [value(x, function) for x in nodes_x]
    return newton_interpolation(nodes_x, nodes_y, x1)
