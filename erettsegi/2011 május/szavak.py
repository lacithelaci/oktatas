lista = []
f = open("szoveg.txt")
for i in f:
    i = i.strip()
    lista.append(i)
print("1. feladat")
bekert_szo = input("Kérek egy szót")


def mgh(a):
    van = False
    for i in "aeoiu":
        if i in a:
            van = True
    return van


if mgh(bekert_szo):
    print("Van benne magánhangzó.")
else:
    print("Nincs benne magánhangzó.")
print("2. feladat")
leghosszabb = ""
for i in sorted(lista, key=lambda i: len(i)):
    leghosszabb = i
print(f"A leghosszabb szó: {leghosszabb}\n{len(leghosszabb)} karakterből áll\n3. feladat")


def melyik(a):
    mgh = 0
    msh = 0
    for i in a:
        for y in "aeoiu":
            if y == i:
                mgh += 1
    msh = len(a) - mgh
    return mgh > msh


mgh = 0
msh = 0
for i in lista:
    if melyik(i):
        mgh += 1
    else:
        msh += 1
print(f"{mgh}/{len(lista)} : {(mgh / len(lista)):.2f}% ")
print("4. feladat")
otkaratkter = []
for i in lista:
    if len(i) == 5:
        otkaratkter.append(i)
szoreszlet = input("Kérek egy szórészletet")
for i in otkaratkter:
    if i[1:4] == szoreszlet:
        print(i)
print("5. feladat")


def harom(a):
    return a[1:4]


elozo = ""
jelenlegi = ""
f = open("letra.txt", "w", encoding="utf-8")
db = 0
for i in sorted(otkaratkter, key=lambda i: harom(i)):
    jelenlegi = i
    if db >= 1:
        f.write(f"{elozo}\n")
        if harom(jelenlegi) != harom(elozo):
            f.write(f"\n")
    db += 1
    elozo = jelenlegi
