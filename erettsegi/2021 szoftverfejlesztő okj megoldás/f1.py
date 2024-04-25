#Készítette: Szemán László
#Megoldási idő: 00:22:18
class Pilotak:
    def __init__(self,nev,szul,nemz,rajt):
        self.nev = nev
        self.szul = szul
        self.nemz = nemz
        self.rajt = rajt
    def __repr__(self):
        return f"{self.nev} {self.szul} {self.nemz} {self.rajt}"
    def fuggveny(self):
        asd=i.szul.split(".")
        return int(asd[0])
lista=[]
f=open("pilotak.csv",encoding="UTF-8")
for xd,i in enumerate(f):
    if xd!=0:
        i=i.strip().split(";")
        lista.append(Pilotak(*i))
print(f"3. feladat: {len(lista)}")
asd=""
for i in lista:
    asd=i.nev
print(f"4. feladat: {asd}")
print("5. feladat:")
for i in lista:
    if i.fuggveny()<1901:
        print(f"{i.nev} ({i.szul})")

lista2=[int(i.rajt) for i in lista if i.rajt!=""]
a=min(lista2)
asd2=""
for i in lista:
    if str(a)==i.rajt:
        asd2=i.nemz
print(f"6. feladat: {asd2}")
szotar={}
for i in lista:
    if i.rajt!="":
        szotar[i.rajt]=szotar.get(i.rajt,0)+1
print("7. feladat:",end=" ")
for xd,i in szotar.items():
    if int(i)>=2:
        print(xd,end=", ")