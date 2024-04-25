class Furdo:
    def __init__(self,azonos,hely,kibe,ora,perc,masodperc):
        self.azonos = int(azonos)
        self.hely = int(hely)
        self.kibe = int(kibe)
        self.ora = int(ora)
        self.perc = int(perc)
        self.masodperc = int(masodperc)
    def __repr__(self):
        return f"{self.azonos} {self.hely} {self.kibe} {self.ora} {self.perc} {self.masodperc}"
lista=[]
f=open("furdoadat.txt")
for i in f:
    i=i.strip().split()
    lista.append(Furdo(*i))
lista2=[]
for i in lista:
    lista2.append(i.azonos)
a=lista2[0]
b=lista2[-1]
elsoido=0
utolso_ido=0
print("2. feladat")
for i in lista:
    if i.azonos==a and i.kibe==1 and i.hely==0:
        print(f"Az első vendég {i.ora}:{i.perc}:{i.masodperc}-kor lépett ki az öltözőből.")
    if i.azonos == b and i.kibe == 1 and i.hely == 0:
        print(f"Az utolsó vendég {i.ora}:{i.perc}:{i.masodperc}-kor lépett ki az öltözőből. ")
szotar={}
for i in lista:
    szotar[i.azonos]=szotar.get(i.azonos,0)+1
db=0
for i,xd in szotar.items():
    if xd==4:
        db+=1
print("3. feladat")
print(f"A fürdőben {db} vendég járt csak egy részlegen. ")
print("4.feladat")