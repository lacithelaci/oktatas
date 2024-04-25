class Szinek:
    def __init__(self, egy, ketto, harom):
        self.egy = egy
        self.ketto = ketto
        self.harom = harom

    def __repr__(self):
        return f"{self.egy} {self.ketto} {self.harom} {i.egybeszin()}"

    def egybeszin(self):
        a = self.egy + " " + self.ketto + " " + self.harom
        return a


f = open("kep.txt")
lista = []
for i in f:
    i = i.strip().split()
    lista.append(Szinek(*i))
a = 200
b = 96
c = 64
van = False
print("2. feladat")
for i in lista:
    if int(i.egy) == a and b == int(i.ketto) and c == int(i.harom):
        van = True
if not van:
    print("nincs")
else:
    print("van")
a = 35 * 50 + 8
for index, i in enumerate(lista):
    if index + 1 == a:
        a = i.egybeszin()

sorban = 0
oszlopban = 0
oszlop = 8
otven = 50
print("3. feladat")
for index, i in enumerate(lista):
    if index + 1 >= 35 * 50 + 1 and index + 1 <= 35 * 50 + 50:
        if i.egybeszin() == a:
            sorban += 1
    if (index + 1) % otven == 8:
        otven += 50
        if i.egybeszin() == a:
            oszlopban += 1
otven = 50
otvenegy = 51
otvenketto = 52
nyolc = 50
kilenc = 50
nulla = 50
print(f"Sorban: {sorban} Oszlopban: {oszlopban}")
print("4. feladat")
kek = 0
piros = 0
zold = 0
for i in lista:
    if i.egy == "255" and i.ketto=="0" and i.harom=="0":
        piros += 1
    if i.egy == "0" and i.ketto=="255" and i.harom=="0":
        zold += 1
    if i.egy == "0" and i.ketto=="0" and i.harom=="255":
        kek += 1
if piros<=kek>=zold:
    print("Kékből van a legtöbb")
elif kek<=piros>=zold:
    print("Vörösből van a legtöbb")
else:
    print("Zöldből van a legtöbb")
nullanulla = "0 0 0"
for index, i in enumerate(lista):
    if index + 1 <= 150 or index + 1 >= 2350:
        i.egybeszin = nullanulla
    if (index + 1) % otven == 1:
        otven += 50
        i.egybeszin = nullanulla
    if (index + 1) % otvenegy == 1:
        otvenegy += 50
        i.egybeszin = nullanulla
    if (index + 1) % otvenketto == 1:
        otvenketto += 50
        i.egybeszin = nullanulla

    if (index + 1) % nyolc == 0:
        nyolc += 50
        i.egybeszin = nullanulla
    if (index + 1) % kilenc == 49:
        kilenc += 50
        i.egybeszin = nullanulla
    if (index + 1) % nulla == 48:
        nulla += 50
        i.egybeszin = nullanulla

f = open("keretes.txt", "w")
for index, i in enumerate(lista):
    if i.egybeszin == "0 0 0":
        f.write(f"{i.egybeszin}\n ")
    else:
        f.write(f"{i.egy} {i.ketto} {i.harom}\n ")
print("7. feladat")
indesz=0
for index,i in enumerate(lista):
    if i.egy=="255" and i.ketto=="255" and i.harom=="0":
        indesz=index
        break
db=0
print(f"Kezd: {index//50}, {index%50} ")
for index,i in enumerate(lista):
    if i.egy=="255" and i.ketto=="255" and i.harom=="0":
        indesz=index
        db+=1
print(f"Vég: {index//50}, {index%50}\nKéppontok száma: {db} ")