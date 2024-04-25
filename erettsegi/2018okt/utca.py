class Utca:
    def __init__(self,par,meter,szin):
        self.par = int(par)
        self.meter =int( meter)
        self.szin = szin
        self.hazszam = 0
    def __repr__(self):
        return f"{self.par} {self.meter} {self.szin}"
    def ures(self):
        a=" "
        c=len(str(i.hazszam))
        return a*(i.meter-c)
f=open("kerites.txt")
lista=[]
paros=0
for i in f:
    i=i.strip().split()
    lista.append(Utca(*i))
print(f"2. feladat \nAz eladott telkek száma: {len(lista)}")
print("3. feladat")
paros1=-1
paros2=0
for i in lista:
    paros=i.par
if paros==0:
    print("A páros oldalon adták el az utolsó telket. ")
else:
    print("A páratlan oldalon adták el az utolsó telket. ")
for i in lista:
    if i.par==0:
        paros2+=2
        i.hazszam=paros2
    if i.par==1:
        paros1+=2
        i.hazszam=paros1
    a=i.hazszam
print(f"Az utolsó telek házszáma: {a} ")
paratlan=[i for i in lista if i.par%2==1]
elozo=""
szamocska=0
for i in paratlan:
    if (elozo==i.szin and i.szin!=":" and i.szin!="#" and elozo!="#" and elozo!=":"):
        print(f"4. feladat\nA szomszédossal egyezik a kerítés színe: {i.hazszam - 2}")
        break
    elozo=i.szin
print("5. feladat")
#a=int(input("Adjon meg egy házszámot!"))
a=83
b=a-2
c=a+2
bszin=""
cszin=""
for i in lista:
    if a==i.hazszam:
        print(f"A kerítés színe / állapota: {i.szin}")
        a=i.szin
    if b==i.hazszam:
        bszin=i.szin
    if c==i.hazszam:
        cszin=i.szin
szinek2={""}
szinek2.add(a)
szinek2.add(bszin)
szinek2.add(cszin)
szinek={"A","B","C","D","F","G","H","I","J","K","L","Y","X","C","V","B","N","M","Q","W"}
szinek3=set("QWERTZUIOPLKJHGFDSAYXCVBNM")
lehetseges=szinek3.difference(szinek2)
for i in lehetseges:
    a=i
print("A kerítés színe / állapota:",a)
xd=open("utcakep.txt","w",encoding="UTF-8")

f=""
for i in paratlan:
    xd.write(f"{(i.szin)*i.meter}")
xd.write("\n")
xd.close()
xd=open("utcakep.txt","a")
for i in paratlan:
    xd.write(f"{i.hazszam}{i.ures()}")