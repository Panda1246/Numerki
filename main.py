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
        punkty_x=[]
        punkty_y=[]
        wynik = mt.bisection(przedzial_a, przedzial_b, jakaFunkcja, epsilon, liczbaIteracji)
        print("Wynik bisekcja: ", wynik[0], "Liczba iteracji: ", wynik[1])
        wynik = mt.secant_method(przedzial_a, przedzial_b, jakaFunkcja, epsilon, liczbaIteracji)
        print("Wynik metoda siecznych: ", wynik[0], "Liczba iteracji: ", wynik[1])
        var=(przedzial_b-przedzial_a)/1000
        for i in range(1000):
            punkty_x.append(var)
            punkty_y.append(mt.value(var,jakaFunkcja))
            var+=var
        plt.plot(punkty_x, punkty_y)
        plt.show()



