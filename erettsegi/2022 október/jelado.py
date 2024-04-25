import math


class Jel:
    def __init__(self, ora, perc, ms, x, y):
        self.ora = int(ora)
        self.perc = int(perc)
        self.ms = int(ms)
        self.x = int(x)
        self.y = int(y)

    def __repr__(self):
        return f"{self.ora} {self.perc} {self.ms} {self.x} {self.y}"

    def msbe(self):
        return self.ora * 3600 + self.perc * 60 + self.ms


def eltelt(a, b):
    return a - b


def vissza(a):
    ora = a // 3600
    perc = (a - ora * 3600) // 60
    ms = a - (ora * 3600 + perc * 60)
    return f"{ora}:{perc}:{ms}"


f = open("jel.txt")
lista = []
for i in f:
    i = i.strip().split()
    lista.append(Jel(*i))
ssz = 0

print("2. feladat")
sorszama = int(input("Adja meg a jel sorszámát!"))
for i in lista:
    ssz += 1
    if ssz == sorszama:
        print(f"x={i.x} y={i.y}")

print("4. feladat")
print(f"Időtartam: {vissza(eltelt(lista[-1].msbe(), lista[0].msbe()))}")
print("5. feladat")
iksz = [i.x for i in lista]
ipsz = [i.y for i in lista]
print(f"Bal alsó: {min(iksz)} {min(ipsz)}, jobb felső: {max(iksz)} {max(ipsz)} ")
print("6. feladat")
szum = 0
for i in range(0, len(lista) - 1):
    szum += math.sqrt((lista[i + 1].x - lista[i].x) ** 2 + (lista[i + 1].y - lista[i].y) ** 2)
print(f"Elmozdulás: {(szum):.3f} egység ")
f = open("kimaradt.txt", "w", encoding="utf-8")
elozo_ido = 0
jelenlegi_ido = 0
szamlalo = 0
elozo_x = 0
jelenlegi_x = 0
elozo_y = 0
jelenlegi_y = 0
volt_ido = 0
volt_koor = 0
volt1 = False
volt2 = False
for i in lista:
    jelenlegi_x = i.x
    jelenlegi_y = i.y
    jelenlegi_ido = i.msbe()
    szamlalo += 1
    if szamlalo > 1:
        if jelenlegi_ido - elozo_ido > 5 * 60:
            volt_ido = (jelenlegi_ido - elozo_ido) // (5 * 60 + 1)

            volt1 = True
        if (jelenlegi_x - elozo_x).__abs__() > 10 or (jelenlegi_y - elozo_y).__abs__() > 10:
            volt2 = True
            if (jelenlegi_x - elozo_x).__abs__() > (jelenlegi_y - elozo_y).__abs__():
                volt_koor = (jelenlegi_x - elozo_x).__abs__() // 11
            else:
                volt_koor = (jelenlegi_y - elozo_y).__abs__() // 11

        if volt1 and volt2:
            if volt_ido >= volt_koor:
                f.write(f"{vissza(jelenlegi_ido).replace(':', ' ')} időeltérés {volt_ido}\n")
            else:
                f.write(f"{vissza(jelenlegi_ido).replace(':', ' ')} koordináta-eltérés {volt_koor}\n")
        elif volt1:
            f.write(f"{vissza(jelenlegi_ido).replace(':', ' ')} időeltérés {volt_ido}\n")
        elif volt2:
            f.write(f"{vissza(jelenlegi_ido).replace(':', ' ')} koordináta-eltérés {volt_koor}\n")

    elozo_x = jelenlegi_x
    elozo_y = jelenlegi_y
    elozo_ido = jelenlegi_ido
    volt1 = False
    volt2 = False
