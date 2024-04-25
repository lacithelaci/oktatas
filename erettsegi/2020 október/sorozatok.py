class Sorozat:
    def __init__(self, kiadas, cim, resz, ido, latta):
        self.kiadas = kiadas
        self.cim = cim
        self.resz = resz
        self.ido = int(ido)
        self.latta = int(latta)

    def __repr__(self):
        return f"{self.kiadas} {self.cim} {self.resz} {self.ido} {self.latta}"

    def ev(self):
        a = self.kiadas
        a = a[0:4]
        return int(a)

    def honap(self):
        return int(self.kiadas[5:7])

    def nap(self):
        return int(self.kiadas[8:10])


def perc(a):
    c = a // (60 * 24)
    b = int((a / 60 - c * 24))
    a = a % 60
    return f"Sorozatnézéssel {c} napot {b} órát és {a} percet töltött. "


f = open("lista.txt")
lista = []
for i in f:
    i = i.strip()
    i2 = f.readline().strip()
    i3 = f.readline().strip()
    i4 = f.readline().strip()
    i5 = f.readline().strip()
    lista.append(Sorozat(i, i2, i3, i4, i5))
lista2 = [i.kiadas for i in lista if i.kiadas != "NI"]
print(f"2. feladat\nA listában {len(lista2)} db vetítési dátummal rendelkező epizód van. ")
lista3 = [i.ido for i in lista if i.latta == 1]
lista4 = [i.ido for i in lista]
print(f"3. feladat\nA listában lévő epizódok {(len(lista3) / len(lista4) * 100):.2f}%-át látta. ")
print("4. feladat")
a = sum(lista3)
print(perc(a))
print("5. feladat")

a = input("Adjon meg egy dátumot! Dátum= ")
for i in lista:
    if a > i.kiadas:
        if i.latta == 0:
            print(f"{i.resz} {i.cim}")
print("7. feladat")


def Hetnapja(ev, ho, nap):
    napok = ["v", "h", "k", "sze", "cs", "p", "szo"]
    honapok = [0, 3, 2, 5, 0, 3, 5, 1, 4, 6, 2, 4]
    if ho < 3:
        ev = ev - 1
    hetnapja = napok[(ev + ev // 4 - ev // 100 + ev // 400 + honapok[ho - 1] + nap) % 7]
    return hetnapja


a = input("Adja meg a hét egy napját (például cs)! Nap=  ")
szotar = set()
for i in lista:
    if i.kiadas != "NI":
        if Hetnapja(i.ev(), i.honap(), i.nap()) == a:
            szotar.add(i.cim)
for i in szotar:
    if szotar != "":
        print(i)
xd = open("summa.txt", "w", encoding="UTF-8")
cimek = set()
for i in lista:
    cimek.add(i.cim)
for i in cimek:
    osszido = 0
    db = 0
    for j in lista:
        if i == j.cim:
            osszido += int(j.ido)
            db += 1
    xd.write(f"{i} {osszido} {db}\n")
