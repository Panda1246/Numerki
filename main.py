# wpisywanie wspolczynnikow
lenght = int(input("Podaj najwyzsza potege wielomianu"))
values = []

for i in range(lenght + 1):
    values.append(int(input("Podaj wspolczynnik do x^" + str(i))))

# wpisanie x
x = int(input("Podaj wartosc x"))


def Horner_value(x, values, lenght):
    final_value = 0
    for i in range(lenght):
        final_value = final_value * x + values[i]
    return final_value


def bisekcja(a, b, wspolczynniki):
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


print(Horner_value(x, values, len(values)))
