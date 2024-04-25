lista = []
f = open("szotar.txt")
for i in f:
    i = i.strip()
    lista.append(i)
print('1. feladat')
bekert_szo = input("Kérek egy szöveget")
halmaz = set()
for i in bekert_szo:
    halmaz.add(i)
print(f"{len(halmaz)} különböző karakter található a szövegben\n3. feladat")


def sorbarendezett(a):
    b = ""
    for i in sorted(a):
        b += i

    return b


print("Kész a fájlba írás")
f = open("abc.txt", "w", encoding="utf-8")
for i in lista:
    f.write(f"{sorbarendezett(i)}\n")
print("4. feladat")
elso_szo = input("Első szó:")
masodik_szo = input("Második szó:")
if sorbarendezett(elso_szo) == sorbarendezett(masodik_szo):
    print("Anagramma")
else:
    print("Nem anagramma")
print("5. feladat")
bekert_szo = input("Kérek egy szót")
anagramma = []
for i in lista:
    if sorbarendezett(bekert_szo) == sorbarendezett(i):
        anagramma.append(i)
if len(anagramma) == 0:
    print("Nincs a szótárban anagramma")
else:
    print(f"{bekert_szo} anagrammái:")
    for i in anagramma:
        print(i)
print("6. feladat")
hossz = 0
for i in sorted(lista, key=lambda i: len(i)):
    hossz = len(i)
print("A leghosszabb szavak: ")
anagramma = []
for i in lista:
    if len(i) == hossz:
        anagramma.append(i)
for i in sorted(anagramma, key=lambda i: sorbarendezett(i)):
    print(i)
elozo = ""
jelenlegi = ""
db = 0
f = open("rendezve.txt", "w")
for i in sorted(lista, key=lambda i: (len(i), sorbarendezett(i))):

    jelenlegi = i
    if db != 0:
        if sorbarendezett(jelenlegi) == sorbarendezett(elozo):
            f.write(f"{elozo} ")
        else:
            f.write(f"{elozo}\n")
        if len(jelenlegi) != len(elozo):
            f.write("\n")
    db += 1
    elozo = jelenlegi
