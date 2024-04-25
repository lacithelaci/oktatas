class Beosztas:
    def __init__(self,nev,targy,osztaly,oraszam):
        self.nev = nev
        self.targy = targy
        self.osztaly = osztaly
        self.oraszam = int(oraszam)
    def __repr__(self):
        return f"{self.nev} {self.targy} {self.osztaly} {self.oraszam}"


lista=[]
f=open("beosztas.txt",encoding="UTF-8")
for i in f:
    i=i.strip()
    i2=f.readline().strip()
    i3= f.readline().strip()
    i4= f.readline().strip()
    lista.append(Beosztas(i,i2,i3,i4))
print(f"2. feladat\nA fájlban {len(lista)} bejegyzés van.")
print("3.feladat")
ossz=0
for i in lista:
    ossz+=i.oraszam
print("Az iskolában a heti összóraszám:",ossz)
print("4.feladat")
nev=input("Egy tanár neve=")
ossz=0
for i in lista:
    if i.nev==nev:
        ossz+=i.oraszam
print(f"A tanár heti óraszáma: {ossz}")
o=open("of.txt","w",encoding="UTF-8")
for i in lista:
    if i.targy=="osztalyfonoki":
        o.write(f"{i.osztaly} - {i.nev}\n")
print("6. feladat")
osztaly=input("Osztály=")
tantargy=input("Tantárgy=")
db=0
for i in lista:
    if i.osztaly==osztaly:
        if i.targy==tantargy:
            db+=1
if db<1:
    print("Nem csoportbontásban tanulják. ")
else:
    print("Csoportbontásban tanulják. ")
lista2={""}
for i in lista:
    lista2.add(i.nev)
print("7.feladat")
print(f"Az iskolában {len(lista2)-1} tanár tanít. ")