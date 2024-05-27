import math_helper as mt
import matplotlib.pyplot as plt
import numpy as np

czy_dziala = True
while czy_dziala:

    jakaFunkcja = input("Jaka funkcje wybierasz? \n "
                        "1 - 8x + 3 \n "
                        "2 - |x - 5| \n "
                        "3 - 1 + x - 2x^2\n "
                        "4 - cos(x) / x \n "
                        "5 - sin(x) - 2cos(x-5) \n "
                        "q - wyjście\n")
    if jakaFunkcja == 'Q' or jakaFunkcja == 'q':
        czy_dziala = False

    else:
        func = mt.function(jakaFunkcja)

        a = float(input("Podaj początek przedziału aproksymacji: "))
        b = float(input("Podaj koniec przedziału aproksymacji: "))
        degree = int(input("Podaj stopień wielomianu aproksymacyjnego: "))
        num_nodes = degree

        x = np.linspace(a, b, num_nodes)
        y, dy = func(x)

        z, coefficients = mt.hermite_interpolation_coefficients(x, y, dy)

        x_dense = np.linspace(a, b, 500)
        y_dense = np.array([mt.horner_scheme(coefficients, xi, z) for xi in x_dense])
        y_true = func(x_dense)
        error = np.abs(y_true - y_dense)
        print(f"Średni błąd aproksymacji: {np.mean(error[0])}")
        #print(f"Maksymalny błąd aproksymacji: {np.max(error)}")
        print(f"Wzór otrzymanego wielomianu aproksymacyjnego:\n{mt.polynomial_to_string(coefficients, degree)}")

        plt.plot(x_dense, y_true[0], label="Funkcja oryginalna")
        plt.plot(x_dense, y_dense, label="Aproksymacja Hermite'a")
        # plt.scatter(x, y, color='red', zorder=5, label="Punkty interpolacyjne")
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title("Aproksymacja wielomianami Hermite'a")
        plt.legend()
        plt.show()
        input()
