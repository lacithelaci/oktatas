class Fuvar:
    def __init__(self, nap, fuvarszam, km):
        self.nap = int(nap)
        self.fuvarszam = int(fuvarszam)
        self.km = int(km)

    def __repr__(self):
        return f"{self.nap} {self.fuvarszam} {self.km}"


f = open("tavok.txt")
lista = []
for i in f:
    i = i.strip().split()
    lista.append(Fuvar(*i))
lista = sorted(lista, key=lambda i: (i.nap, i.fuvarszam))
print("2. feladat")
print(lista[0].km)
print("3. feladat")
print(lista[-1].km)
print("4. feladat")
napok=set()
for i in lista:
    napok.add(i.nap)
napok2=set()
for i in range(1,8):
    napok2.add(i)

print(napok2.difference(napok))
print("5. feladat")
szotar={}
for i in lista:
    szotar[i.nap]=szotar.get(i.nap,0)+1
a=maxszotar.values()