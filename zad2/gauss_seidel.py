def gauss_seidel_iteration(A, b, max_iter=1000):
    n = len(b)
    x0 = [0] * n
    x = x0.copy()
    for _ in range(max_iter):
        x_old = x.copy()
        for i in range(n):
            sum_ = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - sum_) / A[i][i]
        # Zakończ jeśli osiągnięto maksymalną liczbę iteracji
    return x



def gauss_seidel_precision(A, b, tol=1e-6):
    n = len(b)
    x0 = [0] * n
    x = x0.copy()
    while True:
        x_old = x.copy()
        for i in range(n):
            sum_ = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - sum_) / A[i][i]
        if all(abs(x[i] - x_old[i]) < tol for i in range(n)):
            return x
    raise ValueError("Metoda Gaussa-Seidela nie zbiega się w danej liczbie iteracji.")