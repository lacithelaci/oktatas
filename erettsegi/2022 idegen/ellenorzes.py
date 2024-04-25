class Meres:
    def __init__(self, rendszam, kora, kperc, kms, kems, vora, vperc, vms, vems):
        self.rendszam = rendszam
        self.kora = int(kora)
        self.kperc = int(kperc)
        self.kms = int(kms)
        self.kems = int(kems)
        self.vora = int(vora)
        self.vperc = int(vperc)
        self.vms = int(vms)
        self.vems = int(vems)

    def __repr__(self):
        return f"{self.rendszam} {self.kora} {self.kperc} {self.kms} {self.kems} {self.vora} {self.vperc} {self.vms} {self.vems}"

    def kmh(self):
        osszms = (self.vora * 3600 + self.vperc * 60 + self.vms + self.vems / 1000) - (
                self.kora * 3600 + self.kperc * 60 + self.kms + self.kems / 1000)
        osszms = osszms / 3600
        return int(10 / osszms)

    def vegms(self):
        return self.vora * 3600 + self.vperc * 60 + self.vms + self.vems / 1000

    def kezdms(self):
        return self.kora * 3600 + self.kperc * 60 + self.kms + self.kems / 1000

    def bunti(self):
        if self.kmh() <= 121:
            return f"30 000 Ft"
        elif self.kmh() <= 136:
            return f"45 000 Ft"
        elif self.kmh() <= 151:
            return f"60 000 Ft"
        else:
            return f"200 000 Ft"


lista = []
f = open("meresek.txt")
for i in f:
    i = i.strip().split()
    lista.append(Meres(*i))
print(f"2. feladat\nA mérés során {len(lista)} jármű adatait rögzítették.\n3. feladat")
db = 0
for i in lista:
    if i.vora < 9:
        db += 1
print(f"9 óra előtt {db} jármű haladt el a végponti mérőnél.\n4. feladat")
ora = 8
perc = 20
db = 0
for i in lista:
    if i.kora == ora and i.kperc == perc:
        db += 1
print(f"a. A kezdeti méréspontnál elhaladt járművek száma:", db)
db = 0
for i in lista:
    if i.kora + i.kperc <= ora + perc and i.vperc + i.vora >= ora + perc:
        db += 1
print(f"b. A forgalomsűrűség: {db / 10}")
print(f"5. feladat\nA legnagyobb sebességgel haladó jármű")
masz = [i.kmh() for i in lista]
a = max(masz)
kezd = 0
veg = 0
for i in lista:
    if a == i.kmh():
        kezd = i.kezdms()
        veg = i.vegms()
        print(f"rendszáma: {i.rendszam}\nátlagsebessége: {i.kmh()} km/h ")
        break
db = 0
for i in lista:
    if i.kezdms() < kezd and i.vegms() > veg:
        db += 1
print(f"által lehagyott járművek száma: {db}\n6. feladat ")
db = 0
for i in lista:
    if i.kmh() >= 90:
        db += 1
print(f"A járművek {(db / len(lista) * 100):.2f}%-a volt gyorshajtó.\nA fájl elkészült. ")
f = open("buntetes.txt", "w", encoding="utf-8")
for i in lista:
    if i.kmh() >= 104:
        f.write(f"{i.rendszam} {i.kmh()}\t{i.bunti()}\n")
