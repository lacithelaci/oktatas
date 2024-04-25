f = open("verseny.txt")
elso_sor = f.readline()
lista = []
for i in f:
    i = i.strip()
    lista.append(i)
print("2. feladat")

halmaz = set()
for index, i in enumerate(lista):
    a = ""
    b = ""
    for y in i:
        a = y
        if b == a and a == "+" and b == "+":
            halmaz.add(index + 1)
        b = a
print(f"Az egymast kovetoen tobbszor talalo versenyzok:", end=" ")
for i in halmaz:
    print(i, end=" ")
print("\n3. feladat")
lista2 = [int(len(i)) for i in lista]
masz = max(lista2)
for index, i in enumerate(lista):

    if len(i) == masz:
        print(f"A legtobb lovest leado versenyzo rajtszama: {index + 1}")


def loertek(sor):
    aktpont = 20
    ertek = 0
    for i in range(len(sor)):
        if aktpont > 0 and sor[i] == "-":
            aktpont = aktpont - 1
        else:
            ertek = ertek + aktpont
    loertek = ertek
    return loertek


print("5. feladat")
sorszam = 2
db = 0
db2 = 0
masz = 0
talalt = []
c = ""
for index, i in enumerate(lista):
    a = ""
    b = ""
    if index == sorszam - 1:
        for index2, y in enumerate(i):
            if y == "+":
                db += 1
                talalt.append(index2 + 1)
            if b == a and a == "+":

                db2 += 1
            else:
                db2 = 0
            a = y
            if db2 > masz:
                masz = db2

            b = a
        c = loertek(i)
print("5a. feladat: Celt ero lovesek:", *talalt)
print("5b. feladat: Az eltalalt korongok szama:", db)
print("5c. feladat: A leghosszabb hibatlan sorozat hossza: ", db2)
print(f"5d. feladat: A versenyzo pontszama:", c)


class Verseny:
    def __init__(self, sorszam, pontszam):
        self.sorszam = int(sorszam)
        self.pontszam = int(pontszam)

    def __repr__(self):
        return f"{self.sorszam} {self.pontszam}"


vegeredmeny = []
for index, i in enumerate(lista):
    vegeredmeny.append(Verseny(index + 1, loertek(i)))
hely = 0
jelenlegi = -1
elozo = -2
db = 0
xd = open("sorrend.txt", "w")
for i in sorted(vegeredmeny, key=lambda i: i.pontszam, reverse=True):
    db = 0
    jelenlegi = i.pontszam
    if elozo != jelenlegi:
        hely += 1
    else:
        db += 1

    xd.write(f"{hely}\t{i.sorszam}\t{i.pontszam}\n")
    hely = db + hely
    elozo = jelenlegi
