import random

print("2. feladat\nAdja meg, mi nyitja a zárat!")
a = input("")
print("3. feladat")
f = open("ajto.txt")
lista = []
for i in f:
    i = i.strip()
    lista.append(i)
    lista2 = []
for index, i in enumerate(lista):
    if i == a:
        lista2.append(index + 1)
print("A nyitó kódszámok sorai:", *lista2)
print("4. feladat")


def ismetlodes(a):
    hasonlo = False
    db = 0
    for i in range(len(a)):
        db = 0
        for y in a:
            if a[i] == y:
                db += 1
                if db >= 2:
                    hasonlo = True
    return hasonlo


ismetel = False
for index, i in enumerate(lista):
    if ismetlodes(i):
        print(f"Az első ismétlődést tartalmazó próbálkozás sorszáma: {index + 1}")
        ismetel = True
        break
if not ismetel:
    print("nem volt ismétlődő számjegy")
print("5. feladat ")
lista2 = []
b = len(a)
while len(lista2) != b:
    d = random.randint(0, 9)
    if d not in lista2:
        lista2.append(d)

szam = ""
for i in lista2:
    szam += str(i)
print(f"Egy {len(a)} hosszú kódszám: {szam} ")
print("6. feladat")


def nyit(jo, proba):
    egyezik = len(jo) == len(proba)
    if egyezik:
        elteres=int(jo[0])-int(proba[0])
        for i in range(1,len(jo)):
            if(elteres - (int(jo[i]) - int(proba[i]))) % 10 != 0:
                egyezik=False
    return egyezik

for i in lista:
    i=str(i)
    if (len(i))!=len(a):
        print(f"{i} hibás hossz")
    else:
        if nyit(i,a):
            print(f"{i}: sikeres")
        else:
            print(f"{i}: hibás kódszám")

