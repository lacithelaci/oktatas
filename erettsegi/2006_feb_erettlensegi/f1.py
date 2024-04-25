class Hivas:
    def __init__(self,kora,kperc,kms,vora,vperc,vms,tszam):
        self.kora = int(kora)
        self.kperc =int( kperc)
        self.kms =int( kms)
        self.vora =int( vora)
        self.vperc =int( vperc)
        self.vms =int(vms)
        self.tszam = tszam
    def __repr__(self):
        return f"{self.kora} {self.kperc} {self.kms} {self.vora} {self.vperc} {self.vms} {self.tszam}"
    def szamlazott(self):
        a=(self.vora*60+self.vperc+self.vms/60)-(self.kora*60+self.kperc+self.kms/60)
        #a=int(a)
        if int(a)<a:
            a=int(a)+1
        return a

lista=[]
f=open("HIVASOK.TXT")
for i in f:
    i=i.split()
    i2=f.readline()
    lista.append(Hivas(*i,i2))



def mobile(a):
    b="vezetékes"
    for i in a.split():
        if a[0]=="4" and a[1]=="1" or a[0]=="7" and a[1]=="1":
            b="mobil"
        if a[0]=="3" and a[1]=="9":
            b="mobil"
    return b

a="417373732323"
#a=input("kérek egy telefonszámot")
print("1. feladat")
print(mobile(a))
kóra=1
kperc=1
kms=60
vóra=2
vperc=1
vms=60
dc=(vóra*60+vperc+vms/60)-(kóra*60+kperc+kms/60)
print("2. feladat")
print(f"{dc} percet telefonált")
t=open("percek.txt ","w",encoding="UTF-8")
for i in lista:
    t.write(f"{i.szamlazott()} {i.tszam}")
csucsido=0
nem_csucsido=0
for i in lista:
    if i.kora>=7 and i.kora<=18:
        csucsido+=1
    else:
        nem_csucsido+=1
mobil=0
vezetek=0
print("4. feladat")
print(f"A csúcsidőben intézett hívások: {csucsido}. A nem csúcsidőben lévő hívások száma {nem_csucsido}")
for i in lista:
    if mobile(i.tszam)=="mobil":
        mobil+=i.szamlazott()
    if mobile(i.tszam)=="vezetékes":
        vezetek+=i.szamlazott()
vhivas=30
mhivas=69.175
print("5. feladat")
print(f"Vezetékes hívások perce:{int(vezetek)}, Mobilos hívások perce {mobil}")
print("6. feladat")
szumma=0

for i in lista:
    if i.kora>=7 and i.kora<=18:
        if mobile(i.tszam)=="mobil":
            szumma+=i.szamlazott()*mhivas
        if mobile(i.tszam)=="vezetékes":
            szumma += i.szamlazott() * vhivas
print(f"A csúcsdíjas hívások ára: {szumma:.0f} forint")
