class Ado:
    def __init__(self, adoszam, utca, hazszam, adozas, terulet):
        self.adoszam = int(adoszam)
        self.utca = utca
        self.hazszam = hazszam
        self.adozas = adozas
        self.terulet = int(terulet)

    def __repr__(self):
        return f"{self.adoszam} {self.utca} {self.hazszam} {self.adozas} {self.terulet}"


lista = []
f = open("utca.txt")
elso_sor = f.readline()
elso_sor = elso_sor.split()
for i in f:
    i = i.strip().split(" ")
    lista.append(Ado(*i))
print(f"2. feladat. \nA mintában {len(lista)} telek szerepel.\n3. feladat ")
van = False
bekert = int(input("Egy tulajdonos adószáma:"))
for i in lista:
    if bekert == i.adoszam:
        print(f"{i.utca} utca {i.hazszam}")
        van = True
if not van:
    print(f"Nem szerepel az adatállományban.")
print("5. feladat")


def ado(adosav, adoterulet, ado):
    fizetendo = 0
    if adosav == "A":
        fizetendo = adoterulet * ado
    elif adosav == "B":
        fizetendo = adoterulet * ado
    else:
        fizetendo = adoterulet * ado
    if fizetendo < 10000:
        return 0
    else:
        return fizetendo


halmaz = set(i.adozas for i in lista)
db = 0
szum = 0
fizetendo = 0
for y in sorted(halmaz):
    db = 0
    szum = 0
    if y == "A":
        fizetendo = int(elso_sor[0])
    elif y == "B":
        fizetendo = int(elso_sor[1])
    else:
        fizetendo = int(elso_sor[2])
    for i in lista:
        if i.adozas == y:
            db += 1
            szum += ado(i.adozas, i.terulet,fizetendo)
    print(f"{y} sávba {db} telek esik, az adó {szum} Ft.")
elozo = ""
jelenlegi = ""
utca = ""
elozoutca = ""
vizsgalas = set()
for i in lista:
    jelenlegi = i.adozas
    utca = i.utca
    if utca == elozoutca:
        if jelenlegi != elozo:
            vizsgalas.add(utca)
    elozo = jelenlegi
    elozoutca = utca
print("6. feladat. A több sávba sorolt utcák: ")
for i in sorted(vizsgalas):
    print(i)
f = open("fizetendo.txt", "w", encoding="UTF-8")
szum = 0
szotar = {}
for i in lista:
    if i.adozas== "A":
        fizetendo = int(elso_sor[0])
    elif i.adozas == "B":
        fizetendo = int(elso_sor[1])
    else:
        fizetendo = int(elso_sor[2])
    szotar[i.adoszam] = szotar.get(i.adoszam, 0) + ado(i.adozas, i.terulet,fizetendo)
for index, i in szotar.items():
    f.write(f"{index} {i}\n")
