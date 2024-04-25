class Kongresszus:
    def __init__(self, nev, honap, nap, sorszam, perc, cim, eszkoz):
        self.nev = nev
        self.honap = int(honap)
        self.nap = int(nap)
        self.sorszam = int(sorszam)
        self.perc = int(perc)
        self.cim = cim
        self.eszkoz = eszkoz

    def __repr__(self):
        return f"{self.nev} {self.honap} {self.nap} {self.sorszam} {self.perc} {self.cim} {self.eszkoz}"

    def honap_nap(self):
        return f"November {str(self.nap)}."


def ora_perc(a):
    ora = a // 60
    perc = a % 60
    return f"{(ora):02d}:{(perc):02d}"


f = open("eloadasok.txt", encoding="UTF-8")
lista = []
pontos = set()
for i in f:
    i = i.strip().split("\t")
    lista.append(Kongresszus(*i))
for i in lista:
    pontos.add(i.honap_nap())
print("2. feladat")
for y in sorted(pontos):
    print(f"{y}:")
    for i in sorted(lista, key=lambda i: (i.nap, i.sorszam)):
        if y == i.honap_nap():
            print(f"{i.sorszam}. {i.nev}: {i.cim}")
print("3. feladat")
szotar = {}
for i in lista:
    szotar[i.honap_nap()] = szotar.get(i.honap_nap(), 0) + i.perc
szam = 0
for index, i in sorted(szotar.items()):
    szam += 1
    print(f"{szam}. nap: {ora_perc(i)}")
print("4. feladat")
nov6 = [i.perc for i in lista if i.nap == 6]
max6 = max(nov6)
for i in lista:
    if i.nap == 6 and max6 == i.perc:
        print(f"{i.nev} {i.perc} ")
print("5. feladat ")
napok = set()
for i in lista:
    napok.add(i.nap)
nap = ""
feladat5 = []
lista8 = []
for y in napok:
    ebed = True
    ossz = 60 * 8
    for i in lista:
        if i.nap == y:
            ossz = ossz + i.perc + 20
            nap = i.honap_nap()
            if ebed:
                if ossz > 60 * 12:
                    ossz += 60
                    ebed = False
    feladat5.append(f"{nap}: {ora_perc(ossz)}")
    lista8.append((ossz))
for i in sorted(feladat5):
    print(i)
print("6. feladat")
harmadik_nap = []
for i in sorted(napok):
    harmadik_nap.append(i)
harmadik_nap = harmadik_nap[2]
ebed = True
ossz = 60 * 8
nap3 = [i for i in lista if i.nap == harmadik_nap]
for i in sorted(nap3, key=lambda i: (i.sorszam)):
    ossz = ossz + i.perc + 20
    nap = i.honap_nap()
    if ebed:
        if ossz > 60 * 12:
            ebed = False
            break
print(f"Az ebédszünet {ora_perc(ossz)} órakor kezdődik az harmadik napon.\n7. feladat")
szotar = {}
for i in lista:
    szotar[i.nev] = szotar.get(i.nev, 0) + 1
if len(szotar) != 0:
    for index, i in szotar.items():
        if i >= 2:
            print(f"{index} {i}")
else:
    print("Nem találtam egyező neveket.")
print("8. feladat")
nap = int(input("Kérek egy napot (5-8): "))
ora = int(input("Kérek egy órát: "))
perc = int(input("Kérek egy percet: "))
ebed = True
ossz = 60 * 8
nap3 = [i for i in lista if i.nap == nap]
for i in sorted(nap3, key=lambda i: (i.sorszam)):
    ossz = ossz + i.perc + 20
    if ebed:
        if ossz > 60 * 12:
            ebed = False
            break
ebed = ossz
percek = ora * 60 + perc
ossz = 8 * 60
lista2 = [i for i in lista if i.nap == nap]
vege = lista8[(nap-1) - 4]
volte = False
for i in sorted(lista2, key=lambda i: (i.sorszam)):
    if volte == False:
        if percek < ossz:
            print("Még nem kezdődött el")
            break
    ossz += i.perc
    if ossz >= percek:
        print("Előadás")
        break
    else:
        ossz = ossz + 20
        if ossz >= percek:
            print("Vita")
            break
    if percek > vege:
        print("Már véget ért")
        break
    if 60 >= (ebed + 60) - percek >= 0:
        print("Ebédszünet")
        break
print("9. feladat")
fajl = open("idorend.txt", "w", encoding="UTF-8")
for y in sorted(napok):
    ebed = True
    elozo = 60 * 8
    ossz = 60 * 8
    fajl.write(f"November {y}.\n")
    for i in sorted(lista, key=lambda i: (i.nap, i.sorszam)):
        if i.nap == y:
            elozo = ossz
            ossz = ossz + i.perc
            fajl.write(f"  {ora_perc(elozo)}-{ora_perc(ossz)} {i.nev}: {i.cim} ({i.eszkoz})\n")
            elozo = ossz
            ossz += 20
            fajl.write(f"  {ora_perc(elozo)}-{ora_perc(ossz)} Vita\n")
            if ebed:
                if ossz > 60 * 12:
                    ossz += 60
                    ebed = False
                    elozo = ossz - 60
                    fajl.write(f"  {ora_perc(elozo)}-{ora_perc(ossz)} Ebéd\n")
print("A fájl lérehozása sikeresen megtörtént.")
