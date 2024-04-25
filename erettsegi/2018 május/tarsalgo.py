class Tarsalgo:
    def __init__(self,ora,perc,az,kibe):
        self.ora = int(ora)
        self.perc = int(perc)
        self.az = int(az)
        self.kibe = kibe
    def __repr__(self):
        return f"{self.ora} {self.perc} {self.az} {self.kibe}"
    def oopp(self):
        return f"{str(self.ora)}:{str(self.perc)}"
    def perc2(self):
        return 60*self.ora+self.perc
f=open("ajto.txt")
lista=[]
for i in f:
    i=i.strip().split()
    lista.append(Tarsalgo(*i))
elso=lista[0]
print(f"2. feladat\nAz első belépő: {elso.az}  ")
utolso=[i.az for i in lista if i.kibe=="ki"]
print(f"Az utolsó kilépő: {utolso[-1]} ")
szotar= {}
xd=open("athaladas.txt","w",encoding="UTF-8")
for i in lista:
    szotar[i.az]=szotar.get(i.az,0)+1
for index,i in sorted(szotar.items()):
    xd.write(f"{index} {i}\n")
print("4. feladat")
lista2=[]
for index,i in szotar.items():
    if i%2==1:
        lista2.append(index)
print("A végén a társalgóban voltak: ",*sorted(lista2))
print("5. feladat ")
bentlevok=0
max=0
jelenlegi=0
for i in lista:
    if i.kibe=="be":
        bentlevok+=1
    if i.kibe=="ki":
        bentlevok-=1
    if bentlevok>max:
        max=bentlevok
        jelenlegi=i.oopp()
print(f"Például {jelenlegi}-kor voltak a legtöbben a társalgóban.\n6.feladat ")
a=int(input("Adja meg a személy azonosítóját!  "))
print("7.feladat")
for i in lista:
    if a==i.az:
        if i.kibe=="be":
            print((i.oopp()),end="-")
        if i.kibe=="ki":
            print(f"{str(i.oopp())}")
print("8.feladat")
bentperc=0
kintperc=0
osszperc=0
allapot="ki"
for i in lista:
    bentperc = 0
    kintperc = 0
    if a==i.az:
        if i.kibe=="be":
            bentperc=i.perc2()
            allapot="ki"
        if i.kibe=="ki":
            kintperc=i.perc2()
            allapot="be"
    osszperc+=kintperc-bentperc
if allapot=="ki":
    print(f"A(z) {a}. személy összesen {osszperc + 15 * 60} percet volt bent, a megfigyelés végén a társalgóban volt. ")
else:
    print(f"A(z) {a}. személy összesen {osszperc} percet volt bent, a megfigyelés végén nem volt a társalgóban. ")