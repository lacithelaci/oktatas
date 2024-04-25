class Helyjegy:
    def __init__(self,ules,fel,le,sorszam):
        self.sorszam = sorszam
        self.ules = int(ules)
        self.fel =int( fel)
        self.le = int(le)
    def __repr__(self):
        return f"{self.ules} {self.fel} {self.le} {self.sorszam}"
    def tavolsag(self):
        return self.le-self.fel
    def ar(self):

        darab= self.tavolsag()//10
        if self.tavolsag()%10!=0:
            darab+=1
        fiz= darab*egységár
        maradek=fiz%10
        if maradek in range(0,3):
            return fiz-maradek
        if maradek in range(3,8):
            return fiz-maradek+5
        else:
            return fiz-maradek+10




lista=[]
f=open("eladott.txt")
for i,sor in enumerate(f):
    sor=sor.strip().split()
    if i==0:
        eladott_jegy=int(sor[0])
        vonalhossz=int(sor[1])
        egységár=int(sor[2])
    else:
        lista.append(Helyjegy(*sor,i))
print("2. feladat")
print(f"Az utolsó utas ülése {lista[-1].ules}, a távolság {lista[-1].tavolsag()} km")
print("3. feladat")
#print(vonalhossz)
for jegy in lista:
    #print(i.tavolsag())
    if jegy.tavolsag()==vonalhossz:
        print(f"{jegy.ules}", end=" ")
print()
print("3. feladat")
vegig=[str(jegy.ules) for jegy in lista if jegy.tavolsag()==vonalhossz]
print(" ".join(vegig))
print("4. feladat")
arak=[jegy.ar() for jegy in lista]
print(f"Az összes ár: {sum(arak)} forint")
print("5. feladat")
leszallas={jegy.le for jegy in lista}
utolso=sorted(leszallas)[-2]
#print(utolso)
utolso_lista=[jegy.le for jegy in lista if jegy.le==utolso or jegy.fel==utolso]
print(f"ennyien szálltak le: {len(utolso_lista)}")
print("feladat 6")
print("megállók száma: ",len(leszallas)-1)
print("feladat 7")
a = int(input("kérek egy kilométert"))
for ules in range(1, 49):
    lista5 = [helyjegy.sorszam for helyjegy in lista if helyjegy.ules and a >= helyjegy.fel and a < helyjegy.le]
    if len(lista5) == 0:
        print(f"{ules}. ülés: üres ")
    else:
        print(f"{ules}. ülés: {lista5[0]}. utas ")
# print(lista)


