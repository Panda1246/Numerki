import math_helper as mt

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
        jakieOgraniczenie = input("\n Warunek konca: \n 1 - liczba iteracji \n 2 - Wariant A\n")
        if jakieOgraniczenie == '1':
            liczbaIteracji = int(input("\n Podaj liczbe iteracji\n"))
            wynik = mt.bisection_for_iteration(przedzial_a, przedzial_b, jakaFunkcja, liczbaIteracji)
            print("Wynik bisekcja: ", wynik[0], " x: ", wynik[1], " iteracja: ", wynik[2])
            wynik =  mt.secant_method_iteration(przedzial_a, przedzial_b, jakaFunkcja, liczbaIteracji)
            print("Wynik metoda siecznych: ", wynik[0], " x: ", wynik[1], " iteracja: ", wynik[2])
        if jakieOgraniczenie == '2':
            epsilon = float(input("\n Podaj epsilon\n"))
            wynik = mt.bisection_for_variant(przedzial_a, przedzial_b, jakaFunkcja, epsilon)
            print("Wynik  bisekcja: ", wynik[0], " x: ", wynik[1], " iteracja: ", wynik[2])
            wynik = mt.secant_method_variant(przedzial_a, przedzial_b, jakaFunkcja, epsilon)
            print("Wynik metoda siecznych: ", wynik[0], " x: ", wynik[1], " iteracja: ", wynik[2])




