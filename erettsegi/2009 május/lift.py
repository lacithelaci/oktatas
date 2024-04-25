class Lift:
    def __init__(self, ora, perc, ms, csapat, honnan, hova):
        self.ora = int(ora)
        self.perc = int(perc)
        self.ms = int(ms)
        self.csapat = int(csapat)
        self.honnan = int(honnan)
        self.hova = int(hova)

    def __repr__(self):
        return f"{self.ora} {self.perc} {self.ms} {self.csapat} {self.honnan} {self.hova}"


f = open("igeny.txt")
szintszam = f.readline()
csapatszam = f.readline()
igenyszam = f.readline()
lista = []
for i in f:
    i = i.strip().split()
    lista.append(Lift(*i))
print(f"2. feladat Kérem a lift indulási helyét!")
szint = int(input("Kérem az indulás szintjét"))
print("3. feladat")
helyszin = ""
for i in lista:
    helyszin = i.hova
print(f"A lift a {helyszin}. szinten áll az utolsó igény teljesítése után.\n4. feladat")
maszimum = szint

minimum = szint

for i in lista:
    if maszimum < i.hova:
        maszimum = i.hova
    if maszimum < i.honnan:
        maszimum = i.honnan
    if minimum > i.hova:
        minimum = i.hova
    if minimum > i.honnan:
        minimum = i.honnan
print(f"{minimum} volt a legalacsonyabb és {maszimum} a legmagasabb sorszámú szin\n5. feladat")
fel = 0
kezdet = 0
veg = 0
ures = 0
for i in lista:
    kezdet = i.honnan
    if i.honnan < i.hova:
        fel += 1
    if kezdet < veg:
        ures += 1
    veg = i.hova

print(f"{fel}-szer kellett a liftnek felfelé indulnia utassal\n{ures}-szer utas nélkül")
print("6. feladat")
osszes = set(i for i in range(1, int(csapatszam) + 1))
resztvevok = set(i.csapat for i in lista)
print("Nem vették igénybe", osszes.difference(resztvevok))
print("7. feladat")
csapat = int(input("Kérek egy csapatot"))
vetett = False
elozo = ""
elso = ""
db = 0
bizonyitek1 = 0
bizonyitek2 = 0
for i in lista:
    if i.csapat == 3:
        elozo = i.honnan
        if db != 0:
            if elozo != elso:
                vetett = True
                bizonyitek1 = elozo
                bizonyitek2 = elso
        db += 1
        elso = i.hova
if not vetett:
    print("Nem bizonyítható szabálytalanság")
else:
    print(f"{elso}-{elozo} szint közötti utat tették meg gyalog")
