import math_helper as mt

czy_dziala = True
while czy_dziala:
    jakaFunkcja = input("Jaka funkcje wybierasz? \n "
                        "1 - wielomian: y=x^{4}-4x^{3}+8x^{2}-23; \n "
                        "2 - 2sin(x) + x^2 \n "
                        "3 - cos(x) \n "
                        "4 - 3^x -3 \n "
                        "5 - x^2 * 2cos(x) \n "
                        "q - wyjście\n")
    if jakaFunkcja == 'Q' or jakaFunkcja == 'q':
        czy_dziala = False
    else:
        jakieOgraniczenie = input("\n Warunek konca: \n 1 - liczba iteracji \n 2 - Wariant A\n")
        if jakieOgraniczenie == '1':
            liczbaIteracji = int(input("\n Podaj liczbe iteracji\n"))
        if jakieOgraniczenie == '2':
            epsilon = float(input("\n Podaj epsilon\n"))
        przedzial_a = float(input("\n Podaj poczatek przedzialu "))
        przedzial_b = float(input("\n Podaj koniec przedzialu "))

        if jakaFunkcja == '1':
            pass

        if jakaFunkcja == '2':
            pass
        if jakaFunkcja == '3':
            pass
        if jakaFunkcja == '4':
            pass
        if jakaFunkcja == '5':
            pass
