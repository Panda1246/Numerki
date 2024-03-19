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
        if mt.value(przedzial_a,jakaFunkcja)*mt.value(przedzial_b,jakaFunkcja) < 0:
            wybor = input("\n 1 - ilosc literacji; 2 - dokladnosc \n")
            if wybor == '1':
                argument = int(input("\n Podaj liczbe iteracji\n"))
            else:
                argument = float(input("\n Podaj epsilon\n"))
            punkty_x = []
            punkty_y = []
            wynik = mt.choose_your_method(przedzial_a, przedzial_b, jakaFunkcja, argument, wybor)
            print("\n Bisekcja: " + str(wynik[0][0])+" liczba iteracji: "+str(wynik[0][1]))
            print("\n Sieczne: " + str(wynik[1][0])+" liczba iteracji: "+str(wynik[1][1]))
            var = (przedzial_b - przedzial_a) / 1000
            for i in range(1000):
                przedzial_a += var
                punkty_x.append(przedzial_a)
                punkty_y.append(mt.value(przedzial_a, jakaFunkcja))
            plt.plot(punkty_x, punkty_y)
            plt.scatter(wynik[0][0], mt.value(wynik[0][0], jakaFunkcja), color='red', label='Bisekcja')
            plt.scatter(wynik[1][0], mt.value(wynik[1][0], jakaFunkcja), color='blue', label='Sieczne')
            plt.grid(visible=True)
            plt.legend()
            plt.show()
        else:
            print("Brak miejsca zerowego w danym przedziale\n")
