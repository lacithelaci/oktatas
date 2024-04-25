class Fogado:
    def __init__(self,vnev,knev,foglalas_idopont,foglalas_kezdete):
        self.vnev = vnev
        self.knev = knev
        self.foglalas_idopont = foglalas_idopont
        self.foglalas_kezdete = foglalas_kezdete
    def __repr__(self):
        return f"{self.vnev} {self.knev} {self.foglalas_idopont} {self.foglalas_kezdete}"
    def nev(self):
        return f"{self.vnev} {self.knev}"
    def datum(self):
        asd=i.foglalas_kezdete
        asd2=asd[0:10]
        return asd2

lista=[]
f=open("fogado.txt",encoding="UTF-8")
for i in f:
    i=i.strip().split()
    lista.append(Fogado(*i))
print("2. feladat")
print(f"Foglalások száma: {len(lista)} ")
print("3. feladat")
nev=input("Adjon meg egy nevet:")
db=0
for i in lista:
    if i.nev()==nev:
        db+=1
print(f"{nev} néven {db} időpontfoglalás van")
idopont=input("Adjon meg egy érvényes időpontot (pl. 17:10):")
lista2=[]
for i in lista:
    if idopont==i.foglalas_idopont:
        lista2.append(i.nev())
print("4. feladat")
for i in sorted(lista2):
    print(i)
print("5. feladat")
tanarnev=""
idop=""
idej=""
for i in sorted(lista,key=lambda i:i.foglalas_kezdete, reverse=True):
    tanarnev=i.nev()
    idop=i.foglalas_idopont
    idej=i.foglalas_kezdete
print(f"Tanár neve: {tanarnev} ")
print(f"Foglalt időpont: {idop} ")
print(f"Foglalás ideje: {idej}")
print("6. feladat")
barna="Barna Eszter"
lista3=[]
for i in lista:
    if i.nev()==barna:
        lista3.append(i.foglalas_idopont)
for i in sorted(lista3):
    print(i)
print(f"Barna Eszter legkorábban távozhat: {sorted(lista3)[-2]}")
