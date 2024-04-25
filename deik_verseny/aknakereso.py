def hany_bomba_van_a_kornyezetbe(lista, sor, oszlop):
    sorok_szama = len(lista)
    oszlopok_szama = len(lista[0])
    db = 0
    for x in range(max(0, sor - 1), min(sor + 2, sorok_szama)):
        for y in range(max(0, oszlop - 1), min(oszlop + 2, oszlopok_szama)):
            if lista[x][y] == "*":
                db += 1
    return db


def csere(lista):
    seged = []
    ures = ""
    for i in range(len(lista)):
        ures = ""
        for y in range(len(lista[0])):
            if lista[i][y] != "*":
                ures += str(hany_bomba_van_a_kornyezetbe(lista, i, y))
            else:
                ures += "*"
        seged.append(ures)
    return seged


db = 0
while True:
    db+=1
    sor_oszlop = input().split()
    if sor_oszlop[0] == "0" and sor_oszlop[1] == "0":
        break
    sor = int(sor_oszlop[0])
    oszlop = int(sor_oszlop[1])
    lista = []
    for _ in range(sor):
        lista.append(input())
    print(f"Tábla #{db}.")
    for i in csere(lista):
        print(i)
