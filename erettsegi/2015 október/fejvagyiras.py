import random


def fej():
    a = random.randint(1, 11)
    if a % 2 == 1:
        return f"F"
    else:
        return "I"


print(f"1. feladat\nA pénzfeldobás eredménye: {fej()}\n2. feladat")
print("Tippeljen! (F/I)=")
a = "I"
b = fej()
print(f"A tipp {a}. a dobás eredménye: {b} volt")
if a == b:
    print("Ön eltalálta.")
else:
    print("Ön nem találta el.")
print("3. feladat")
f = open("kiserlet.txt")
lista = []
for i in f:
    i = i.strip()
    lista.append(i)
print(f"A kísérlet {len(lista)} dobásból állt\n4. feladat")
db = 0
for i in lista:
    if i == "F":
        db += 1
print(f"A fej relatív gyakorisága {(db / len(lista) * 100):.2f}% volt\n5. feladat")
db=0
for i in range(len(lista)-2):
    if lista[i]=="F" and lista[i-1]!="F" and lista[i+1]!="F" and lista[i+2]!="F":
        db+=1

print(db)
sztring=""
for i in lista:
    sztring+=i
sztring=sztring.split("I")
db=0
for i in sztring:
    if len(i)==2:
        db+=1
print(db)

print(db)
print("6. feladat")
db = 0
masz = 0
elozo = ""
kovetkezo = ""
van = False
pl = 0
indesz = 0
indesz2 = 0
for index, i in enumerate(lista):
    elozo = i
    if elozo == "F":
        van = True
    if elozo == kovetkezo and kovetkezo == "F":
        db += 1
        indesz = index + 1
    else:
        db = 0
    if masz <= db:
        masz = db
        indesz2 = indesz
    kovetkezo = elozo
if van:
    pl = 1
print(f"A leghosszabb tisztefej sorozat {masz + pl} tagból áll, kezdete a(z) {(indesz2) - masz}. dobás.")


def negy():
    s = ""
    for i in range(4):
        a = random.randint(1, 11)
        if a % 2 == 1:
            s += "F"
        else:
            s += "I"
    return s


lista = []
for i in range(1000):
    a = negy()
    lista.append(negy())
db = 0
db2 = 0
for i in lista:
    if i == "FFFF":
        db += 1
    if i == "FFFI":
        db2 += 1
f = open("dobasok.txt", "w")
f.write(f"FFFF: {db}, FFFI: {db2} \n")
for i in lista:
    f.write(f"{i} ")
