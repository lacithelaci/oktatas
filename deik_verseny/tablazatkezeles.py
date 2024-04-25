lista = [0 for i in range(0, 101)]
db = 0
bekert = int(input())
while True:
    seged = []
    a = input()
    a = a.split()
    if a[0] == "VALUE":
        lista[db] = int(a[1])
    elif a[0] == "ADD":
        if "$" in a[1] and "$" in a[2]:
            lista[db] = lista[int(a[1][1:])] + lista[int(a[2][1:])]
        if "$" in a[1]:
            lista[db] = lista[int(a[1][1:])] + int(a[2])
        elif "$" in a[2]:
            lista[db] = lista[int(a[2][1:])] + int(a[1])
        else:
            lista[db] = int(a[2]) + int(a[1])
    elif a[0] == "SUB":
        if "$" in a[1] and "$" in a[2]:
            lista[db] = lista[int(a[1][1:])] - lista[int(a[2][1:])]
        if "$" in a[1]:
            lista[db] = lista[int(a[1][1:])] - int(a[2])
        elif "$" in a[2]:
            lista[db] = lista[int(a[2][1:])] - int(a[1])
        else:
            lista[db] = int(a[2]) - int(a[1])
    else:
        if "$" in a[1] and "$" in a[2]:
            lista[db] = lista[int(a[1][1:])] * lista[int(a[2][1:])]
        if "$" in a[1]:
            lista[db] = lista[int(a[1][1:])] * int(a[2])
        elif "$" in a[2]:
            lista[db] = lista[int(a[2][1:])] * int(a[1])
        else:
            lista[db] = int(a[2]) * int(a[1])

    db += 1
    if db == bekert:
        break

lista = [i for i in lista if i != 0]
for i in lista:
    print(i)
