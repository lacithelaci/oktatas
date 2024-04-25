class Eutazas:
    def __init__(self,megallo,felszallas,az,tipus,ervenyes):
        self.megallo = int(megallo)
        self.felszallas = felszallas
        self.az = az
        self.tipus = tipus
        self.ervenyes = int(ervenyes)
    def __repr__(self):
        return f"{self.megallo} {self.felszallas} {self.az} {self.tipus} {self.ervenyes}"
    def ervenenyese(self):
        a=int(self.felszallas[0:8])
        return a
    def ev1(self):
        a=self.felszallas
        return int(a[0:4])
    def honap1(self):
        a = self.felszallas
        return int(a[4:6])
    def nap1(self):
        a = self.felszallas
        return int(a[6:8])

    def ev2(self):
        a = str(self.ervenyes)
        return int(a[0:4])
    def honap2(self):
        a = str(self.ervenyes)
        return int(a[4:6])

    def nap2(self):
        a = str(self.ervenyes)
        return int(a[6:8])
    def eeee(self):
        a="-"
        b=str(self.ervenyes)
        c=str(b[0:4])+"-"+str(b[4:6])+"-"+str(b[6:8])
        return c
lista=[]
f=open("utasadat.txt","r",encoding="UTF-8")
for i in f:
    i=i.strip().split()
    lista.append(Eutazas(*i))
print(f"2. feladat\nA buszra {len(lista)} utas akart felszállni.")
print("3. feladat")
db=0
for i in lista:
    if i.tipus=="FEB" or i.tipus=="TAB" or i.tipus=="NYB":
        if i.ervenyes<i.ervenenyese():
            db+=1
    if i.ervenyes == 0 and i.ervenyes <= 10:
        db += 1
print(f"A buszra {db} utas nem szállhatott fel. ")
print("4. feladat")
megallok=set()
for i in lista:
    megallok.add(i.megallo)
max=0
maxmegallo=0
for i in sorted(megallok):
    felszallt=0
    megallo=0
    for j in lista:
        if i==j.megallo:
            felszallt+=1
        if max<felszallt:
            max=felszallt
            maxmegallo=j.megallo
print(f"A legtöbb utas ({max} fő) a {maxmegallo}. megállóban próbált felszállni. ")
print("5. feladat")
kedvezmenyes=0
hibas=0
ingyenes=0
for i in lista:
    if i.ervenyes < i.ervenenyese():

        if i.tipus=="TAB" or i.tipus=="NYB":
            hibas+=1
    if i.tipus == "TAB" or i.tipus == "NYB":
        kedvezmenyes+=1
    if i.tipus=="NYP" or i.tipus=="RVS" or i.tipus=="GYK":
        ingyenes+=1
print(f"Ingyenesen utazók száma: {ingyenes} fő")
print(f"A kedvezményesen utazók száma: {kedvezmenyes-hibas} fő")
print("6. feladat")
def napokszama(e1,h1,n1,e2,h2,n2):
    h1=(h1 + 9) % 12
    e1 = e1 - h1//10
    d1 = 365 * e1 + e1 // 4 - e1 // 100 + e1 // 400 + (h1 * 306 + 5) // 10 + n1 - 1
    h2 = (h2 + 9) % 12
    e2 = e2 - h2 // 10
    d2 = 365 * e2 + e2 // 4 - e2 // 100 + e2 // 400 + (h2 * 306 + 5) // 10 + n2 - 1
    napokszama = d2 - d1
    return napokszama
xd=open("figyelmeztetes.txt","w",encoding="UTF-8")
for i in lista:
    if i.tipus!="JGY":
        if napokszama(i.ev1(),i.honap1(),i.nap1(),i.ev2(),i.honap2(),i.nap2())<=3 and 0<=napokszama(i.ev1(),i.honap1(),i.nap1(),i.ev2(),i.honap2(),i.nap2()):
            xd.write(f"{i.az} {i.eeee()}\n")
