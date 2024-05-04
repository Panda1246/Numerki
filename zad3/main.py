import Newton as mt
import matplotlib.pyplot as plt

czy_dziala = True
while czy_dziala:

    jakaFunkcja = input("Jaka funkcje wybierasz? \n "
                        "1 - wielomian: y=x^{4}-4x^{3}+8x^{2}-23; \n "
                        "2 - x - 3 \n "
                        "3 - cos(x) \n "
                        "4 - |x| \n "
                        "5 - 2cos(x^2) \n "
                        "q - wyjście\n")
    if jakaFunkcja == 'Q' or jakaFunkcja == 'q':
        czy_dziala = False
    else:
        przedzial_a = float(input("\n Podaj poczatek przedzialu "))
        przedzial_b = float(input("\n Podaj koniec przedzialu "))
        liczba_wezlow = int(input("\n Podaj liczbe wezlow "))
        var = (przedzial_b - przedzial_a) / 1000
        punkty_x_funkcja =[]
        punkty_y_funkcja =[]
        punkty_y_interpolowana =[]
        przedzial_a_kopia = przedzial_a
        for i in range(1000):
            przedzial_a_kopia += var
            punkty_x_funkcja.append(przedzial_a_kopia)
            punkty_y_funkcja.append(mt.value(przedzial_a_kopia, jakaFunkcja))
            punkty_y_interpolowana.append(mt.choice(przedzial_a, przedzial_b, liczba_wezlow, jakaFunkcja, przedzial_a_kopia))
        plt.plot(punkty_x_funkcja, punkty_y_funkcja)
        plt.plot(punkty_x_funkcja, punkty_y_interpolowana, color = 'red')
        plt.scatter(mt.nodes(przedzial_a, przedzial_b, liczba_wezlow), [mt.value(x, jakaFunkcja) for x in mt.nodes(przedzial_a, przedzial_b, liczba_wezlow)], color = 'black')
        plt.grid(visible=True)
        plt.legend(['funkcja', 'interpolacja', 'wezly'])
        plt.show()

