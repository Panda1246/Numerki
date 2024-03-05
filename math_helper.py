import math
#x^2 - 8x + 3

# x
# values
# length
def Horner_value(x, values, length):
    final_value = 0
    for i in range(length):
        final_value = final_value * x + values[i]
    return final_value


def bisection(a, b, wspolczynniki):
    x = (a + b / 2)
    while Horner_value(x, wspolczynniki, len(wspolczynniki)) != 0:
        value_of_b = Horner_value(b, wspolczynniki, len(wspolczynniki))
        value_of_x = Horner_value(x, wspolczynniki, len(wspolczynniki))
        if (value_of_b < 0 & value_of_x < 0) | (value_of_b > 0 & value_of_x > 0):
            b = x
        else:
            a = x
        x = (a + b / 2)

    return x

def function_1(x):
    return x**4 - 4 * x**3 + 8 * x**2 - 23

def function_2(x):
    return

def function_5(x):
    return x**2 * 2 * math.cos(x)

