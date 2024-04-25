import random


class Verseny:
    def __init__(self, kerdes, valasz, pont, tema):
        self.kerdes = kerdes
        self.valasz = int(valasz)
        self.pont = int(pont)
        self.tema = tema

    def __repr__(self):
        return f"{self.kerdes} {self.valasz} {self.pont} {self.tema}"


lista = []
f = open("felszam.txt")
for i in f:
    i = i.strip()
    i2 = f.readline().strip().split()
    lista.append(Verseny(i, *i2))
print(f"2. feladat\n{len(lista)} feladat van az adatfájlban")
matek = [i for i in lista if i.tema == "matematika"]
print(f"3. feladat\n{len(matek)} matematika feladat van\nEzek közül:")
szotar = {}
for i in matek:
    szotar[i.pont] = szotar.get(i.pont, 0) + 1
for index, i in szotar.items():
    print(f"{index} pontos: {i} db")
pont = [i.valasz for i in lista]
a = max(pont)
b = min(pont)
print(f"4. feladat\n{b}-től {a}-ig terjed a fájlban található válaszok számértéke\n5. feladat")
halmaz = set()
for i in lista:
    halmaz.add(i.tema)
print("A témakörök:", *halmaz)
print("6. feladat")
a = input("Milyen temakorbol szeretne kerdest kapni?")
temakoros = [i for i in lista if i.tema == a]
szam = random.randint(0, len(temakoros) - 1)
kerdes = temakoros[szam]
print(kerdes.kerdes)
valasz = int(input())
if valasz == kerdes.valasz:
    print(f"A valasz {kerdes.pont} pontot er. ")
else:
    print(f"A valasz 0 pontot er.\nA helyes valasz: {kerdes.valasz} ")
lista2 = []
pontoslista=[]
db = 0
pontszam = 0
f = open("tesztfel.txt", "w")
while (len(lista2) != 10):
    a = random.randint(0, len(lista) - 2)
    for index, i in enumerate(lista):
        if index == a:
            if i.kerdes not in lista2:
                lista2.append(f"{i.pont} {i.valasz} {i.kerdes}")
                pontoslista.append(i.pont)

for i in lista2:
    f.write(f"{i}\n")
f.write(f"A feladatsorra osszesen {sum(pontoslista)} pont adhato. ")