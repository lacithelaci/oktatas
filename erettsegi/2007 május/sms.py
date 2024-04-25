def szo(a):
    betu = ""
    for i in a:
        if i in "abc":
            betu += "2"
        if i in "def":
            betu += "3"
        if i in "ghi":
            betu += "4"
        if i in "jkl":
            betu += "5"
        if i in "mno":
            betu += "6"
        if i in "pqrs":
            betu += "7"
        if i in "tuv":
            betu += "8"
        if i in "wxyz":
            betu += "9"
    return betu


kodok = []
a = input()
print("1. feladat:", szo("a"))
ablak = input()
print("2. feladat", szo(ablak))
f = open("szavak.txt")
lista = []
for i in f:
    i = i.strip()
    lista.append(i)
print("4. feladat")
for i in sorted(lista, key=lambda i: len(i), reverse=True):
    print(f"{i} {len(i)}")
    break
print("5. feladat")
db = 0
for i in lista:
    if len(i) <= 5:
        db += 1
print(f"rövidszavak: {db}")
f = open("kodok.txt", "w")
for i in lista:
    f.write(f"{szo(i)}\n")
print("7. feladat")
a = input()
for i in lista:
    if szo(i) == a:
        print(i)
    kodok.append(szo(i))
print("8. feladat")
szotar = {}
for i in kodok:
    szotar[i] = szotar.get(i, 0) + 1
tobb = []
for index, i in szotar.items():
    if i >= 2:
        tobb.append(index)
db = 0
for i in sorted(lista):
    for y in tobb:
        if szo(i) == y:
            db += 1
            print(f"{y}:{i};", end=" ")
            if db % 8 == 0:
                print()
print("9. feladat")
a = 0
for i in szotar.values():
    if a <= i:
        a = i
indesze=""
for index ,i in szotar.items():
    if i==a:
        indesze=index
print("9. feladat")
print(f"{indesze}:",end=" ")
for i in lista:
    if indesze==szo(i):
        print(f"{i},",end=" ")
