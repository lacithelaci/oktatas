class Targy:
    def __init__(self,nev,tantargy,osztaly,oraszam):
        self.nev = nev
        self.tantargy = tantargy
        self.osztaly = osztaly
        self.oraszam = int(oraszam)
    def __repr__(self):
        return f"{self.nev} {self.tantargy} {self.osztaly} {self.oraszam}"
lista=[]
f=open("beosztas.txt",encoding="UTF-8")
for i in f:
    i=i.strip()
    asd=f.readline().strip()
    asd2=f.readline().strip()
    asd3=f.readline().strip()
    lista.append(Targy(i,asd,asd2,asd3))
print("2. feladat")
print(f"A fájlban {len(lista)} bejegyzés van.")
print("3. feladat")
a=0
for i in lista:
    a+=i.oraszam
print(f"Az iskolában a heti összóraszám: {a} ")
print("4. feladat ")
b=0
bekeres=input("Egy tanár neve=")
for i in lista:
    if i.nev==bekeres:
        b+=i.oraszam
print(f"A tanár heti óraszáma: {b} ")
ofo=open("of.txt","w",encoding="UTF-8")
for i in lista:
    if i.tantargy=="osztalyfonoki":
        ofo.write(f"{i.nev}: {i.osztaly} \n")
osztaly=input("Osztály=")
tan=input("Tantárgy=")
db=0
for i in lista:
    if i.tantargy==tan and i.osztaly==osztaly:
        db+=1
print("6. feladat")
if db==1:
    print("Osztályszinten tanulják")
else:
    print("csoportbontásban tanulják")
print("7. feladat")
szotar={}
for i in lista:
    szotar[i.nev]=szotar.get(i.nev,0)+1
print(f"Az iskolában {len(szotar)} tanár tanít.")