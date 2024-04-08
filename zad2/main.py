import gauss_seidel as gs

file = open(r"data.txt", "r")
file = file.read()
sections = file.split('\n\n')

while True:
    print('Dostepne rownania:')
    for i, section in enumerate(sections):
        print(f'{i+1}:')
        print(section)
        print('')
    choice = int(input('Choose a system: \n'))


    coeffs_lines = sections[choice-1].split('\n')
    A = []
    b = []
    for line in coeffs_lines:
        coeffs = line.split('|')[0].split()
        const = float(line.split('|')[1])

        A.append([float(c) for c in coeffs])
        b.append(const)
    max_iter =int(input("Podaj maksymalna liczbe iteracji: "))
    tol = float(input("Podaj dokladnosc: "))
    try:
        x = gs.gauss_seidel(A, b, tol, max_iter)
        print(f'Wynik: {x[0]}\nliczba iteracji: {x[1]}')
    except ValueError as e:
        print(e)
    input("Kontynuwać?")
