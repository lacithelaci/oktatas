class Utca:
    def __init__(self, ora, perc, ms, megtett, varos):
        self.ora = int(ora)
        self.perc = int(perc)
        self.ms = int(ms)
        self.megtett = int(megtett)
        self.varos = varos

    def __repr__(self):
        return f"{self.ora} {self.perc} {self.ms} {self.megtett} {self.varos}"

    def ms1(self):
        return self.ora * 3600 + self.perc * 60 + self.ms

    def utveg(self):
        return self.ms1() + self.megtett

    def oop(self):
        return f"{self.ora} {self.perc} {self.ms}"

    def metersec(self):
        return 1000 / self.megtett

    def vissza(self):
        a = self.utveg()
        ora = a // 3600
        perc = a // 60 - ora * 60
        ms = a - (ora * 3600 + perc * 60)
        return f"{ora} {perc} {ms}"


lista = []
f = open("forgalom.txt")
elso_sor = f.readline()
for i in f:
    i = i.strip().split()
    lista.append(Utca(*i))
print("2. feladat")
a = 4
for index, i in enumerate(lista):
    if index == a - 1:
        print(i.varos)
print("3. feladat")
lista2 = [i for i in lista if i.varos == "A"]
print(f"{lista2[-1].ms1() - lista2[-2].ms1()} ms különbséggel")
halmaz = set()
print("4. feladat")
for i in lista:
    halmaz.add(i.ora)
f = 0
a = 0
for y in halmaz:
    f = 0
    a = 0
    for i in lista:
        if i.ora == y:
            if i.varos == "A":
                a += 1
            else:
                f += 1
    print(f"{y} {a} {f}")
lista3 = []
szamlalo = 0
print("5. feladat")
for i in sorted(lista, key=lambda i: i.megtett, reverse=False):
    lista3.append(i)
    szamlalo += 1
    if szamlalo == 10:
        break
for i in sorted(lista3, key=lambda i: i.metersec(), reverse=True):
    print(f"{i.oop()} {i.varos} {(i.metersec()):.1f}")
print("6. feladat\nFájlba írás elkészült")
kiirando = 0
elozo = 0
jelenlegi = 0
xd = open("also.txt", "w", encoding="utf-8")
for i in lista:
    jelenlegi = i.utveg()
    if jelenlegi >= elozo:
        kiirando = i.vissza()
    elozo = jelenlegi
    xd.write(f"{kiirando}\n")
