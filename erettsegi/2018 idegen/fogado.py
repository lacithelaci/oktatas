class Fogado:
    def __init__(self,vnev,knev,idopont,foglalas_datuma):
        self.vnev = vnev
        self.knev = knev
        self.idopont = idopont
        self.foglalas_datuma = foglalas_datuma
    def __repr__(self):
        return f"{self.vnev} {self.knev} {self.idopont} {self.foglalas_datuma}"


    def nev(self):
        return f"{self.vnev} {self.knev}"


f=open("fogado.txt")
lista=[]
for i in f:
    i=i.strip().split()
    lista.append(Fogado(*i))
print(f"2. feladat\nFoglalások száma: {len(lista)} ")
print("3. feladat")
nev=input("Adjon meg egy nevet:")
lista2=[i.nev() for i in lista if i.nev()==nev]
print(f"{nev} néven {len(lista2)} időpontfoglalás van. ")
print("4. feladat")
idopont=input("Adjon meg egy érvényes időpontot (pl. 17:10):")
lista3=[i.nev() for i in lista if i.idopont==idopont]
lista3=sorted(lista3)
for i in lista3:
    print(i)
print("5. feladat")
lista4=sorted(lista, key=lambda i:i.foglalas_datuma,reverse=True)
a=lista4[-1]
print(f"Tanár neve: {a.nev()}\nFoglalt időpont: {a.idopont}\nFoglalás ideje: {a.foglalas_datuma}")
print("6. feladat")
barna="Barna Eszter"
szotar1=set()
szotar2=set()
for i in lista:
    if i.nev()==barna:
        szotar2.add(i.idopont)
    szotar1.add(i.idopont)
szotar3=szotar1.difference(szotar2)
szotar=sorted(szotar3)
for i in szotar:
    print(i)
print(f"Barna Eszter legkorábban távozhat: {szotar[-2]} ")