class Jaror:
    def __init__(self, ora, perc, ms, rendszam):
        self.ora = int(ora)
        self.perc = int(perc)
        self.ms = int(ms)
        self.rendszam = rendszam

    def __repr__(self):
        return f"{self.ora} {self.perc} {self.ms} {self.rendszam}"
    def msbe(self):
        return self.ora*3600+self.perc*60+self.ms
    def opc(self):
        return f"{self.ora} {self.perc} {self.ms}"
def vissza(mp):
    o = mp //3600
    marad= mp%3600
    p=marad//60
    s=marad%60
    return f"{o}:{p}:{s}"
def betuk(a,b):
    db=0
    db2=0
    asd=True
    for i in range(7):
        if b[i]==a[i]:
            db += 1
    for i in range(7):
        if a[i]=="*":
            db2 += 1
    if db>0 and len(a)-db2==db:
        return asd==True
    else:
        return asd==False
f = open("jarmu.txt")
lista = []
for i in f:
    i = i.strip().split()
    lista.append(Jaror(*i))
a = lista[-1].ora - lista[0].ora
print(f"2. feladat\n{a + 1} órát dolgoztak\n3. feladat")
orak = set()
rsz = ""
for i in lista:
    orak.add(i.ora)
for y in orak:
    volte = False
    for i in lista:
        if volte == False:
            if i.ora == y:
                rsz = i.rendszam
                volte = True
    print(f"{y} óra: {rsz}")
print("4. feladat")
busz = 0
kamion = 0
motor = 0
egyeb = 0
for i in lista:
    if i.rendszam[0] == "B":
        busz += 1
    elif i.rendszam[0] == "K":
        kamion += 1
    elif i.rendszam[0] == "M":
        motor += 1
    else:
        egyeb += 1
print(f"Busz: {(busz)}\nKamion: {(kamion)}\nMotor: {(motor)}\nAutó: {(egyeb)}")
print("5. feladat")
elso=0
elozo=0
max=0
ora=0
ora2=0
for i in lista:
    elso=i.msbe()
    if elozo!=0:
        if max<elso-elozo:
            max=elso-elozo
            ora2=vissza(elozo)
            ora=vissza(elso)
    elozo=elso
print(f"A leghosszabb forgalommentes időszak: {ora2} - {ora}\n6.feladat")
rendszam=input("Kérek egy rendszámot")
for i in lista:
    if betuk(rendszam,i.rendszam):
        print(i.rendszam)
print("7. feladat\nA fájl kész")
perc=5*60
max=0
f=open("vizsgalt.txt","w",encoding="UTF-8")
for i in lista:
    if max<=i.msbe():
        f.write(f"{i.rendszam} {i.opc()}\n")
        max=i.msbe()+60*5