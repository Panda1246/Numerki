#x^2 - 8x + 3
import math

def function_1(x):
    return x**4 - 4 * x**3 + 8 * x**2 - 23


def function_2(x):
    return 2 * math.sin(x) * x**2


def function_3(x):
    return math.cos(x)

def function_4(x):
    return 3**x - 3


def function_5(x):
    return 2*math.cos(x*x)
# x
# values
# length


def value(x, function):
    if function =='1':
        return function_1(x)
    elif function =='2':
        return function_2(x)
    elif function =='3':
        return function_3(x)
    elif function =='4':
        return function_4(x)
    elif function =='5':
        return function_5(x)
def bisection_for_iteration(a, b, function, iteration):
    x = (a + b / 2)
    for i in range(iteration):
        value_of_x = value(x, function)
        value_of_b = value(b, function)
        if value_of_x == 0:
            return x, i
        elif (value_of_b < 0 and value_of_x<0) or (value_of_b > 0 and value_of_x>0):
            b = x
        else:
            a=x
        x = (a + b / 2)
    return x, i+1
'''
def bisection(a, b, wspolczynniki, eps):
    x = (a + b / 2)
    previous_x = None
    while Horner_value(x, wspolczynniki, len(wspolczynniki)) != 0 or stop_flag == True:
        stop_flag = False
        value_of_b = Horner_value(b, wspolczynniki, len(wspolczynniki))
        value_of_x = Horner_value(x, wspolczynniki, len(wspolczynniki))
        if (value_of_b < 0 & value_of_x < 0) | (value_of_b > 0 & value_of_x > 0):
            b = x
        else:
            a = x
        x = (a + b / 2)
        if previous_x is not None:
            if break_statement(eps, x, previous_x) is True:
                stop_flag = True
        elif previous_x is None:
            previous_x = x
    return x

'''
def break_statement(eps, x, xi):
    if math.fabs(x - xi) < eps:
        return True
    else:
        return False

