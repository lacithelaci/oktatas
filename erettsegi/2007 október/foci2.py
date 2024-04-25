class Foci:
    def __init__(self,fordulo,hgol,vgol,hfgol,vfgol,hcsapat,vcsapat):
        self.fordulo = int(fordulo)
        self.hgol = int(hgol)
        self.vgol = int(vgol)
        self.hfgol = int(hfgol)
        self.vfgol = int(vfgol)
        self.hcsapat = hcsapat
        self.vcsapat = vcsapat
    def __repr__(self):
        return f"{self.fordulo} {self.hgol} {self.vgol} {self.hfgol} {self.vfgol} {self.hcsapat} {self.vcsapat}"
    def Eredmeny(self):
        a=i.vgol
        b=i.hgol

        if i.hgol>i.vgol:
            return f"{i.hgol}:{i.vgol}"
        else:
            return f"{i.vgol}:{i.hgol}"

lista=[]
f=open("meccs.txt")
for xd,i in enumerate(f):
    if xd!=0:
        i=i.strip().split(" ")
        lista.append(Foci(*i))
fordulo=1
print("2. feladat")
for i in lista:
    if fordulo==i.fordulo:
        print(f"{i.hcsapat}-{i.vcsapat}: {i.hgol}-{i.vgol} ({i.hfgol}-{i.vfgol})")
lista2=[]
for i in lista:
    if i.hfgol > i.vfgol:
        if i.vgol > i.hgol:
            lista2.append(f"{i.vcsapat} {i.fordulo}. forduloban")
    if i.hfgol < i.vfgol:
        if i.vgol < i.hgol:
            lista2.append(f"{i.hcsapat} {i.fordulo}. forduloban ")
print("3. feladat")
for i in lista2:
    print(i)
print("4.feladat")
a="Bogarak"
lott=0
kapott=0
for i in lista:
    if i.hcsapat == a:
        lott += i.hgol
        kapott += i.vgol
    if i.vcsapat==a:
        lott += i.vgol
        kapott += i.hgol
print("5.feladat")
print(f"lott: {lott} kapott: {kapott}")
print("6.feladat")
Vereseg=False
Fordulo=""
Csapattol=""
for i in lista:
    if a==i.hcsapat and i.hgol<i.vgol:
            Vereseg=True
            Csapattol=i.vcsapat
            fordulo=i.fordulo
            break

if Vereseg:
    print(f"{fordulo} {Csapattol}")
else:
    print("A csapat otthon veretlen maradt.")
szotar={}
for i in lista:
    szotar[i.Eredmeny()]=szotar.get(i.Eredmeny(),0)+1
asd=open("stat.txt","w")
lista3=[]
for i,xd in szotar.items():
    lista3.append(f"{i}-{xd} \n")
for i in lista3:
    i=str(i)
    asd.write(f"{i}")
