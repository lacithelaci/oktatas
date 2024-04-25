class Feherjek:
    def __init__(self, rov, jel, ce, hi, ox, n, s):
        self.rov = rov
        self.jel = jel
        self.ce = int(ce)
        self.hi = int(hi)
        self.ox = int(ox)
        self.n = int(n)
        self.s = int(s)

    def __repr__(self):
        return f"{self.rov} {self.jel} {self.ce} {self.hi} {self.ox} {self.n} {self.s}"

    def relativ(self):
        return self.ce * 12 + self.hi * 5 + self.ox * 16 + self.n * 14 + self.s * 32


lista = []
f = open("aminosav.txt")
for i in f:
    i = i.strip()
    i2 = f.readline().strip()
    i3 = f.readline().strip()
    i4 = f.readline().strip()
    i5 = f.readline().strip()
    i6 = f.readline().strip()
    i7 = f.readline().strip()
    lista.append(Feherjek(i, i2, i3, i4, i5, i6, i7))
print("2-3. feladat")
f = open("eredmeny.txt", "w")
for i in sorted(lista, key=lambda i: i.relativ()):
    print(f"{i.rov} {i.relativ()}")
    f.write(f"{i.rov} {i.relativ()}\n")
f = open("bsa.txt")
szo = ""
for i in f:
    i = i.strip()
    szo += i
szohossz = len(szo)
szotar = {"H": ((szohossz) - 1) * 2, "O": (szohossz) - 1}
print("4. feladat")
f = open("eredmeny.txt", "a")
for i in szo:
    szotar[i] = szotar.get(i, 0) + 1
for index, i in szotar.items():
    if index in "CHONS":
        print(f"{index} {i}", end=" ")
        f.write(f"{index} {i} ")
db = 0
helye = 0
masz = 0
hely = 0
for i in szo:
    db += 1
    helye += 1
    if i == "Y" or i == "W" or i == "F":
        db = 0
    if masz < db:
        masz = db
        hely = helye
print(f"\n5. feladat\nKezdet helye: {hely - masz} Vég helye: {hely} Leghosszabb lánc db: {masz}\n6. feladat")
elozo = ""
jelenlegi = ""
ceszam = 0
for i in szo:
    jelenlegi = i
    if i == "C":
        ceszam += 1

    if jelenlegi == "A" or jelenlegi == "V":
        if elozo == "R":
            break
    elozo = jelenlegi
print(f"A hasítás során keletkező első fehérjelánc részletben {ceszam} Cisztein (C) található!")
