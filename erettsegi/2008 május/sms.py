class Sms:
    def __init__(self, ora, perc, szam, uzenet):
        self.ora = int(ora)
        self.perc = int(perc)
        self.szam = szam
        self.uzenet = uzenet

    def __repr__(self):
        return f"{self.ora} {self.perc} {self.szam} {self.uzenet}"

    def perc1(self):
        return self.ora * 60 + self.perc


f = open("sms.txt")
elso_sor = f.readline()
lista = []
for i in f:
    i = i.strip().split()
    i2 = f.readline().strip()
    lista.append(Sms(*i, i2))
print("2. feladat")
for index, i in enumerate(lista):
    if index == 10:
        print(i)
print("3. feladat")
sztring = [i.uzenet for i in lista]
a = ""
b = sztring[0]
for i in sztring:
    if len(a) < len(i):
        a = i
    if len(b) > len(i):
        b = i
for i in lista:
    if i.uzenet == a:
        print(f"A leghosszabb sms: {i}")
    if i.uzenet == b:
        print(f"A legrövidebb sms: {i}")
husz = 0
negyven = 0
hatvan = 0
nyolvan = 0
szaz = 0
for i in lista:
    if len(i.uzenet) <= 20:
        husz += 1
    elif len(i.uzenet) <= 40:
        negyven += 1
    elif len(i.uzenet) <= 60:
        hatvan += 1
    elif len(i.uzenet) <= 80:
        nyolvan += 1
    elif len(i.uzenet) <= 100:
        szaz += 1
print(f"4. feladat\n1-20:{husz} 21-40:{negyven} 41-60:{hatvan} 61-80:{nyolvan} 81-100:{szaz}\n5. feladat")
szotar = {}
for i in lista:
    szotar[i.ora] = szotar.get(i.ora, 0) + 1
db = 0
for i in szotar.values():
    if i - 10 >= 0:
        db += (i - 10)

print(str(db) + " db")
bno = "123456789"
bnolista = [i for i in lista if i.szam == bno]
elozo = 0
jelenlegi = 0
masz = 0
van = False
db = 0
if len(bnolista) == 1:
    print("nincs elegendő üzenet")
else:
    for i in bnolista:
        jelenlegi = i.perc1()
        if db == 1:
            van = True
        if van:
            if masz <= jelenlegi - elozo:
                masz = jelenlegi - elozo
        db = 1
        elozo = jelenlegi
print(f"6. feladat\n{masz // 60}:{masz % 60}\n7.feladat")
d=input("Kérek egy telszámot")
a=input("Kérek egy órát")
b=input("Kérek egy percet")
c=input("Kérek egy üzenetet")
lista.append(Sms(d,a,b,c))
halmaz=set()
for i in lista:
    halmaz.add(i.szam)
telki=open("smski.txt","w",encoding="utf-8")
for y in sorted(halmaz):
    telki.write(f"{y}\n")
    for i in lista:
        if y==i.szam:
            telki.write(f"{i.ora} {i.perc} {i.uzenet}\n")
