class Auto:
    def __init__(self,nap,ora,rendszam,az,km,kibe):
        self.nap = int(nap)
        self.ora = ora
        self.rendszam = rendszam
        self.az = int(az)
        self.km = int(km)
        self.kibe = int(kibe)
    def __repr__(self):
        return f"{self.nap} {self.ora} {self.rendszam} {self.az} {self.km} {self.kibe}"
    def ki(self):
        if i.kibe==0:
            return f"ki"
        else:
            return f"be"

lista=[]
f=open("autok.txt")
for i in f:
    i=i.strip().split()
    lista.append(Auto(*i))
print("2. feladat")
for i in lista:
    if i.kibe==0:
        a=i.nap
        b=i.rendszam
print(f"{a}. nap rendszám: {b} ")
print("3. feladat")
nap=int(input("Nap:"))
lista2=[]
for i in lista:
    if i.nap==nap:
        lista2.append(f"{i.ora} {i.rendszam} {i.az} {i.ki()}")
for i in lista2:
    print(i)
print("4. feladat")
a=0
b=0
for i in lista:
    if i.kibe==0:
        a+=1
    else:
        b+=1
c="CEG301"
print(f"A hónap végén {a-b} autót nem hoztak vissza. ")
print("5. feladat")
asd=" "
for xd in range(0,10):
    kezdokm=-1
    vegkm=-1
    rsz="CEG30"+str(xd)
    for i in lista:
        if rsz==i.rendszam:
            if kezdokm==-1:
                kezdokm=i.km
            vegkm=i.km
    print(f"{(rsz+asd+str(vegkm-kezdokm))} km")
print("6. feladat")
max=0
az2=""
kezdet=0
veg=0
jelenlegi=0
for i in range(500,601):
    az=i

    for xd in lista:
        if xd.az==az:
            if xd.kibe==0:
                kezdet=xd.km
            if xd.kibe==1:
                veg=xd.km
        if kezdet>0 and veg>0:
            jelenlegi=veg-kezdet
            veg=0
            kezdet=0
        if max<jelenlegi:
            max=jelenlegi
            az2=xd.az
print(f"Leghosszabb út: {max} km, személy: {az2}")
print("7. feladat")
rendszam=input("Rendszám: ")
print("Menetlevél kész. ")
a=rendszam+"_menetlevel.txt"
asd=open(a,"w",encoding="UTF-8")
for i in lista:
    if rendszam==i.rendszam:
        if i.kibe==0:
            asd.write(f"{i.az}   {i.nap}.   {i.ora}   {i.km} km ")
        else:
            asd.write(f"{i.nap}.   {i.ora}   {i.km } km\n")



