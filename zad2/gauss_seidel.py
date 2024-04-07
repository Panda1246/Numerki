def sprawdzenie_przekatnej(A):
    for i in range(len(A)):
        suma = 0
        for j in range(len(A)):
            if i != j:
                suma += A[i][j]
        if abs(A[i][i]) < suma:
            return False
    return True


def przestaw_wiersze(macierz, b):
    n = len(macierz)

    for i in range(n):
        suma_wiersza = sum(abs(macierz[i][j]) for j in range(n) if i != j)
        if macierz[i][i] < suma_wiersza:
            for j in range(i+1,n):
                suma_wiersza_j = sum(abs(macierz[j][k]) for k in range(n) if j != k)
                if macierz[j][i] >= suma_wiersza_j:
                    macierz[i], macierz[j], b[i],b[j] = macierz[j], macierz[i],b[j],b[i]
                    break
            else:
                return 1, macierz, b
    return 0, macierz, b


def gauss_seidel(A, b, tol, max_iteration):
    if not sprawdzenie_przekatnej(A):
        wynik = przestaw_wiersze(A,b)
        if wynik[0] == 1:
            print("Przekatna nie jest dominująca i nie da sie jej ustawic")
        else:
            A = wynik[1]
            b = wynik[2]
    n = len(b)
    x0 = [0] * n
    x = x0.copy()
    for iteration in range(max_iteration):
        x_old = x.copy()
        for i in range(n):
            sum_ = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - sum_) / A[i][i]
        if all(abs(x[i] - x_old[i]) < tol for i in range(n)):
            return x, iteration
    return x, iteration + 1
