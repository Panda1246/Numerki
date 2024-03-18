import math

def Horner_value(x, values, lenght):
    final_value = 0
    for i in range(lenght):
        final_value = final_value * x + values[i]
    return final_value
def function_1(x, coffecients, length):
    return Horner_value(x, coffecients, length)


def function_2(x):
    return 2 * math.sin(x) * (x * x)


def function_3(x):
    return math.cos(x)


def function_4(x):
    return 3 ** x - 3


def function_5(x):
    return 2 * math.cos(x * x)


def value(x, function):
    if function == '1':
        return function_1(x, [1,-4,0,8,-23], 5)
    elif function == '2':
        return function_2(x)
    elif function == '3':
        return function_3(x)
    elif function == '4':
        return function_4(x)
    elif function == '5':
        return function_5(x)


def bisection_iteration(a, b, function, iteration):
    x = (a + b) / 2.0
    i = 0
    while i < iteration:
        value_of_b = value(b, function)
        value_of_x = value(x, function)
       # if math.fabs(value_of_x) <= 0.000001:
        #    return x, i
        if (value_of_b < 0.0 and value_of_x < 0.0) | (value_of_b > 0.0 and value_of_x > 0.0):
            b = x
        else:
            a = x
        x = (a + b) / 2
        i += 1
    return x, i


def bisection_accuracy(a, b, function, eps):
    x = (a + b) / 2.0
    previous_x = a
    i = 0
    while math.fabs(x - previous_x) >= eps:
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


def secant_method_iteration(a, b, function, iteration):
    i = 0
    while True:
        value_of_a = value(a, function)
        value_of_b = value(b, function)
        try:
            x = a - value_of_a * ((a - b) / (value_of_a - value_of_b))
        except:
            print("\nDivision by zero\n")
            return x, i

        if  i == iteration:
            return x, i
        b = a
        a = x
        i += 1


def secant_method_accuracy(a, b, function, eps):
    value_of_a = value(a, function)
    value_of_b = value(b, function)
    x = a - value_of_a * ((a - b) / (value_of_a - value_of_b))
    i = 1
    while True:
        b = a
        a = x
        value_of_a = value(a, function)
        value_of_b = value(b, function)
        previous_x = x
        try:
            x = a - value_of_a * ((a - b) / (value_of_a - value_of_b))
        except:
            print("\nDivision by zero\n")
            return x, i
        if math.fabs(x - previous_x) <= eps:
            return x, i
        i += 1


def choose_your_method(a, b, function, eps_or_iteration, method):
    if method == '1':
        return bisection_iteration(a, b, function, eps_or_iteration), secant_method_iteration(a, b, function,
                                                                                              eps_or_iteration)
    elif method == '2':
        return bisection_accuracy(a, b, function, eps_or_iteration), secant_method_accuracy(a, b, function,
                                                                                            eps_or_iteration)
