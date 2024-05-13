import math_helper as mt


czy_dziala = True
while czy_dziala:

    jakaFunkcja = input("Jaka funkcje wybierasz? \n "
                        "1 - 8x + 3 \n "
                        "2 - sin(x) - 2cos(x-5) \n "
                        "3 - 1 + x - 2x^2\n "
                        "4 - |x - 5| \n "
                        "5 - cos(x) / x \n "
                        "q - wyjście\n")
    if jakaFunkcja == 'Q' or jakaFunkcja == 'q':
        czy_dziala = False
    else:
        przedzial_a = float(input("\n Podaj poczatek przedzialu "))
        przedzial_b = float(input("\n Podaj koniec przedzialu "))
        dokladnosc = float(input("\n Podaj dokladnosc "))
        mt.final_function(przedzial_a,przedzial_b,  dokladnosc, jakaFunkcja)
        input()

