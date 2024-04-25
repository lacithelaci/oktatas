f = open("naplo.txt", encoding="utf-8")
lista = []
lista2 = []
lista3 = []
i2 = " "
for i in f:
    lista2 = []
    if i[0] == "#":
        honap = i.strip().split()
        h1 = honap[1]
        nap = honap[2]
    else:
        sor = i.strip().split()

        vnev = sor[0]
        knev = sor[1]
        hiany = sor[2]
        lista2.append(h1)
        lista2.append(nap)
        lista2.append(vnev)
        lista2.append(knev)
        lista2.append(hiany)
        lista.append(lista2)
print("2. feladat")
print((f"A naplóban {len(lista)} bejegyzés van. \n3. feladat"))
lista2 = [i[4] for i in lista]
igazolt = 0
igazolatlan = 0
for i in lista2:
    for y in i:
        if y == "X":
            igazolt += 1
        elif y == "I":
            igazolatlan += 1
print(f"Az igazolt hiányzások száma {igazolt}, az igazolatlanoké {igazolatlan} óra. ")


def hetnapja(honap, nap):
    napnev = ["vasarnap", "hetfo", "kedd", "szerda", "csutortok", "pentek", "szombat"]
    napszam = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 335]
    napsorszam = (napszam[honap - 1] + nap) % 7
    hetnapja = napnev[napsorszam]
    return hetnapja


print("5. feladat")
honap = input("hónap sorszáma=")
nap = int(input("A nap sorszáma="))
print(f"Azon a napon {hetnapja(2, 3)} volt. \n6. feladat")
kedd = input("A nap neve=")
ora = int(input("Az óra sorszáma="))
db = 0
for i in lista:
    if (hetnapja(int(i[0]), int(i[1]))) == kedd:
        a = i[4]
        if (a[ora - 1]) == "X" or (a[ora - 1]) == "I":
            db += 1
print(f"Ekkor összesen {db} óra hiányzás történt. \n7. feladat")


def hianyzas(a):
    db = 0
    for i in a:
        if i == "X" or i == "I":
            db += 1
    return db


def nev(a, b):
    return f"{a} {b}"


szotar = {}
for i in lista:
    szotar[nev(i[2], i[3])] = szotar.get(nev(i[2], i[3]), 0) + hianyzas(i[4])
masz = 0
for i in szotar.values():
    if masz < i:
        masz = i
lista = []
for index, i in szotar.items():
    if i == masz:
        lista.append(index)
print(f"A legtöbbet hiányzó tanulók:",end=" ")
for i in lista:
    print(i,end=" ")
