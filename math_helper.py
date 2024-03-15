import math


def function_1(x):
    return (x ** 4) - (4 * (x ** 3)) + (8 * (x ** 2)) - 23


def function_2(x):
    return 2 * math.sin(x) * x ** 2


def function_3(x):
    return math.cos(x)


def function_4(x):
    return 3 ** x - 3


def function_5(x):
    return 2 * math.cos(x * x)


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


def bisection(a, b, function, eps, iteration):
    x = (a + b) / 2.0
    previous_x = a
    i = 0
    while math.fabs(x - previous_x) >= eps and i < iteration:
        value_of_b = value(b, function)
        value_of_x = value(x, function)
        if (value_of_b < 0.0 and value_of_x < 0.0) | (value_of_b > 0.0 and value_of_x > 0.0):
            b = x
        else:
            a = x
        previous_x = x
        x = (a + b) / 2
        i += 1
    return x, i


def secant_method(a, b, function, eps, iteration):
    value_of_a = value(a, function)
    value_of_b = value(b, function)
    x = a - value_of_a * ((a - b) / (value_of_a - value_of_b))
    i = 0
    while True:
        b = a
        a = x
        value_of_a = value(a, function)
        value_of_b = value(b, function)
        previous_x = x
        x = a - value_of_a * ((a - b) / (value_of_a - value_of_b))
        i += 1
        if math.fabs(x - previous_x) <= eps and i < iteration:
            return x, i
