f = open("program.txt")
elso_sor = f.readline()
lista = []
for i in f:
    i = i.strip()
    lista.append(i)
utasitas = int(input("Kérem az utasítássor sorszámát!"))
for index, i in enumerate(lista):
    if index == utasitas:
        utasitas = i
        break
print("2. feladat")
elozo = ""
elso = ""
egyszerusitheto = False
for i in utasitas:
    elozo = i
    if elozo != elso and elozo == "E" and elso == "D":
        egyszerusitheto = True
    if elozo != elso and elozo == "D" and elso == "E":
        egyszerusitheto = True
    if elozo != elso and elozo == "K" and elso == "N":
        egyszerusitheto = True
    if elozo != elso and elozo == "N" and elso == "K":
        egyszerusitheto = True
    elso = elozo
if egyszerusitheto:
    print("egyszerűsíthető")
else:
    print("nem egyszerűsíthető")
d = 0
e = 0
k = 0
n = 0
lepes1 = 0
lepes2 = 0
db = 0
elmozdulas = 0
maximum = 0
minimum = 0
for i in utasitas:
    if i == "D":
        d += 1
    if i == "E":
        e += 1
    if i == "K":
        k += 1
    if i == "N":
        n += 1
    if i == "E" or i == "K":
        elmozdulas += 1
    if i == "D" or i == "N":
        elmozdulas -= 1
    db += 1
    if maximum < elmozdulas:
        maximum = elmozdulas
        lepes1 = db
    if minimum > elmozdulas:
        minimum = elmozdulas
        lepes2 = db
kulonbseg = 0
minimum = minimum * -1
ed = e - d
kn = k - n
if ed < 0:
    ed = ed * -1
if kn < 0:
    kn = kn * -1
print(f"{ed} lépést kell tenni az ED, {kn} lépést a KN tengely mentén.")
if maximum > minimum:
    kulonbseg = maximum - minimum
    print(f"{(kulonbseg):.3f} cm :{lepes1}.lépésnél")
else:
    kulonbseg = minimum - maximum
    print(f'{(kulonbseg):.3f} cm : {lepes2}. lépésnél')
print("3. feladat")


def utmegtetel(a):
    db = 0
    elozo = ""
    elso = ""
    for i in a:
        elso = i
        if elso == elozo:
            db += 1
        else:
            db += 3
        elozo = i
    return db


for index, i in enumerate(lista):
    if utmegtetel(i) <= 100:
        print(f"{index + 1}. sor {utmegtetel(i)} lépés")
print("4. feladat")


def utasitasocska(utasitas):
    db = 1
    db1 = 0
    elozo = ""
    elso = ""
    betu = ""
    laci = 0
    osszefon = ""
    for i in utasitas:
        elozo = i
        if laci > 0:
            if elozo == elso:
                db += 1

            else:
                osszefon += f"{str(db)}{str(elso)}"
                db = 1
        elso = elozo
        laci += 1
    osszefon = osszefon.replace("1", "")
    return osszefon


print("A fájlba írás megtötént")
f = open("ujprog.txt", "w", encoding="utf-8")
for i in lista:
    f.write(f"{utasitasocska(i)}\n")
print("5. feladat")
szo = input("Kérek egy utasítássort")
elozo = ""
jelenlegi = ""
db = 0
asd = 0
for i in range(len(szo)):
    jelenlegi = szo[i]
    if elozo.isdigit():
        asd = db
        print(f"{int(elozo) * jelenlegi}", end="")
    elozo = jelenlegi
    db += 1
