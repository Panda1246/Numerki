

file = open(r"data.txt", "r")
matrix = []
rowna_sie=[]
przyklad = []
for i in file:
    print(i)
    line=[]

    if i == "\n":
        przyklad.append(rowna_sie)
        rowna_sie=[]
        matrix.append(przyklad)
        przyklad=[]
    else:
        for j in i.split():
            if j.isdigit():
                line.append(float(j))
            else:
                var = ""
                for k in j:
                    if k == "|":
                        line.append(float(var))
                        var = ""
                    else:
                        var += str(k)
                rowna_sie.append(float(var))
        przyklad.append(line)

for i in matrix:

    print(i)