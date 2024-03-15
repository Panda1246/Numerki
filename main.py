import math_helper as mt
import matplotlib.pyplot as plt

czy_dziala = True
while czy_dziala:

    jakaFunkcja = input("Jaka funkcje wybierasz? \n "
                        "1 - wielomian: y=x^{4}-4x^{3}+8x^{2}-23; \n "
                        "2 - 2sin(x) * x^2 \n "
                        "3 - cos(x) \n "
                        "4 - 3^x -3 \n "
                        "5 - 2cos(x^2) \n "
                        "q - wyjście\n")
    if jakaFunkcja == 'Q' or jakaFunkcja == 'q':
        czy_dziala = False
    else:
        przedzial_a = float(input("\n Podaj poczatek przedzialu "))
        przedzial_b = float(input("\n Podaj koniec przedzialu "))
        liczbaIteracji = int(input("\n Podaj liczbe iteracji\n"))
        epsilon = float(input("\n Podaj epsilon\n"))
        punkty_x = []
        punkty_y = []
        wynik_bisekcja = mt.bisection(przedzial_a, przedzial_b, jakaFunkcja, epsilon, liczbaIteracji)
        print("Wynik bisekcja: ", wynik_bisekcja[0], "Liczba iteracji: ", wynik_bisekcja[1])
        wynik_sieczne = mt.secant_method(przedzial_a, przedzial_b, jakaFunkcja, epsilon, liczbaIteracji)
        print("Wynik metoda siecznych: ", wynik_sieczne[0], "Liczba iteracji: ", wynik_sieczne[1])
        var = (przedzial_b - przedzial_a) / 1000
        for i in range(1000):
            przedzial_a += var
            punkty_x.append(przedzial_a)
            punkty_y.append(mt.value(przedzial_a, jakaFunkcja))
        plt.plot(punkty_x, punkty_y)
        plt.scatter(wynik_bisekcja[0], 0, color='red', label='Bisekcja')
        plt.scatter(wynik_sieczne[0], 0, color='blue', label='Sieczne')
        plt.legend()
        plt.show()
