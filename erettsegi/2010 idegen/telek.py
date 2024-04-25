import math


class Telkek:
    def __init__(self, hazszam, szel, hosszu):
        self.hazszam = int(hazszam)
        self.szel = int(szel)
        self.hosszu = int(hosszu)

    def __repr__(self):
        return f"{self.hazszam} {self.szel} {self.hosszu}"

    def terulet(self):
        return self.szel * self.hosszu

    def ado(self):
        fabatka = 0
        if self.terulet() <= 700:
            fabatka = self.terulet() * 51
        elif self.terulet() <= 1000:
            fabatka = 700 * self.terulet() + ((self.terulet() - 700) * 39) + 200
        else:
            fabatka = 700 * self.terulet() + (self.terulet() - 700) * 39
            # ((self.terulet - 700) * 39)+200
        if self.szel <= 15 or self.hosszu <= 25:
            fabatka = fabatka * 0.8
        return fabatka


f = open("telkek.txt")
elso_sor = f.readline()
lista = []
for i in f:
    i = i.strip().split()
    lista.append(Telkek(*i))
lista = sorted(lista, key=lambda i: i.hazszam)
szum = 0
for i in lista:
    szum += i.szel
szum += 2 * 80
print(f"2. feladat\n{szum} métert kell annak gyalogolnia, aki körbe akarja járni a két utcát")
keskeny = 0
for i in lista:
    if i.hazszam % 2 == 0 and i.szel <= 20:
        keskeny += 1
print(f"3. feladat\n{keskeny} telek esetén teljes utcafront beépítést kell alkalmazni.\n4. feladat")
gazdagsor = [i for i in lista if i.hazszam % 2 == 1]
teruletuk = [i.terulet() for i in gazdagsor]
maximum = max(teruletuk)
minimum = min(teruletuk)
h1 = 0
h2 = 0
for i in lista:
    if maximum == i.terulet():
        h1 = i.hazszam
    if minimum == i.terulet():
        h2 = i.hazszam
print(f"a legnagyobb és legkisebb telek házszáma: {h1}:{h2}\n{int(abs((h1 - h2) / 2))} ház van közöttük\n5. feladat")
szum = 0
for i in lista:
    if i.hazszam % 2 == 1:
        szum += round(i.ado() / 100) * 100

print(f"{int(szum)} fabatka adóbevételre számíthat Gazdagsor után az önkormányzat\n6. feladat")
db = 0
for i in sorted(lista, key=lambda i: i.hazszam, reverse=True):
    if i.hazszam % 2 == 1:
        db += 1
        print(f"{i.hazszam}: {i.szel} méter")
        if db == 3:
            break
f=open("joletsor.csv","w")
for i in range(len(lista)):
    if lista[i].hazszam%2==0:
        hosszu=lista[i-1].hosszu+10
        f.write(f"{lista[i].hazszam} {lista[i].szel} {hosszu}\n")

