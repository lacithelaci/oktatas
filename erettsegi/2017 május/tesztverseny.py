class Verseny:
    def __init__(self,az,valasz):
        self.az = az
        self.valasz = valasz
        self.pontszam = 0
    def __repr__(self):
        f'{self.az} {self.valasz} '
def plussz(megoldas,valasz):
    a=len(megoldas)
    veg=""
    jelenleg=""
    for i in range(0,a-1):
        if megoldas[i]==valasz[i]:
            jelenleg="+"
        else:
            jelenleg=" "
        veg=veg+jelenleg
    return veg
def fuggveny(megoldas,valasz):
    pont=0
    for i in range(0,15):
        if i<=5:
            if megoldas[i-1]==valasz[i-1]:
                pont+=3
        if i>5 and i <=10:
            if megoldas[i-1]==valasz[i-1]:
                pont+=4
        if i > 10 and i <= 13:
            if megoldas[i-1] == valasz[i-1]:
                pont += 5
        if i==14:
            if megoldas[i-1] == valasz[i-1]:
                pont += 6

    return pont

f=open("valaszok.txt")
lista=[]
valaszok=f.readline()
for i in f:
    i=i.strip().split()
    lista.append(Verseny(*i))
print(f"1. feladat: Az adatok beolvasása\n2. feladat: A vetélkedőn {len(lista)} versenyző indult.\n3. feladat: A versenyző azonosítója =")
az=input("")
v1=""
for i in lista:
    if az==i.az:
        print(f"{i.valasz}")
        v1=i.valasz
print("4. feladat")
print(valaszok)
print(plussz(valaszok,v1))
print("5. feladat \nA feladat sorszáma =")
sorszam=10
lista2=[i.valasz for i in lista if i.valasz[sorszam-1]==valaszok[sorszam-1]]
print(f"A feladatra {len(lista2)} fő, a versenyzők {(len(lista2)/len(lista)*100):.2f}%-a adott helyes választ. ")
print("6. feladat")
print("A versenyzők pontszámának meghatározása ")
ki=open("pontok.txt","w",encoding="UTF-8")
for i in lista:
    ki.write(f"{i.az} {fuggveny(valaszok,i.valasz)}\n")
    i.pontszam=fuggveny(valaszok,i.valasz)
lista=sorted(lista,key=lambda i:i.pontszam,reverse=True)
szotar= set()
for i in lista:
    szotar.add(i.pontszam)
    if len(szotar)==3:
        break
szotar=sorted(szotar)
elso=szotar[2]
masodik=szotar[1]
harmadik=szotar[0]
print("7. feladat: A verseny legjobbjai: ")
for i in lista:
    if i.pontszam==elso:
        print(f"1. díj ({elso} pont): {i.az} ")
    if i.pontszam==masodik:
        print(f"2. díj ({elso} pont): {i.az} ")
    if i.pontszam==harmadik:
        print(f"3. díj ({elso} pont): {i.az} ")