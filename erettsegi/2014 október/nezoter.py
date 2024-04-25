f = open("foglaltsag.txt")
lista = []
listazo = []
db = 0
for i in f:
    i = i.strip()
    listazo = []
    for y in i:
        listazo.append(y)
    lista.append(listazo)
print("2. feladat")
a = int(input("sor:"))
b = int(input("oszlop:"))
if lista[a - 1][b - 1] == "x":
    print("foglalt")
else:
    print("nem foglalt")
db = 0
foglalt = 0
for i in lista:
    for y in i:
        db += 1
        if y == "x":
            foglalt += 1
print(
    f"3. feladat\nAz előadásra eddig {foglalt} jegyet adtak el, ez a nézőtér {(foglalt / db * 100):.2f}%-a.\n4. feladat ")
f = open("kategoria.txt")
lista2 = []
listazo = []
db = 0
for i in f:
    i = i.strip()
    listazo = []
    for y in i:
        listazo.append(y)
    lista2.append(listazo)
a = ""
for i in range(0, 15):
    for y in range(0, 20):
        if lista[i][y] == "o":
            a += "o"
        else:
            a += lista2[i][y]
szotar = {}
db = 0
for i in lista:
    for y in i:
        if y == "o":
            db += 1
for i in a:
    if i != "o":
        szotar[i] = szotar.get(i, 0) + 1
masz = 0
for i in szotar.values():
    if masz < i:
        masz = i
for index, i in szotar.items():
    if masz == i:
        print(f"A legtöbb jegyet a(z) {index}. árkategóriában értékesítették. ")
print("5. feladat")
szum = 0
for index, i in szotar.items():
    if index == "1":
        szum += 5000 * i
    elif index == "2":
        szum += 4000 * i
    elif index == "3":
        szum += 3000 * i
    elif index == "4":
        szum += 2000 * i
    elif index == "5":
        szum += 1500 * i
print(f"{szum} Ft a színház bevétele a pillanatnyilag eladott jegyek")
print("6. feladat")
db = 0
jelenlegi = ""
kovetkezo = ""
for i in range(1, 13):
    for y in range(1, 19):
        if lista[i][y] == "o" and lista[i + 1][y + 1] == "x" and lista[i - 1][y - 1] == "x":
            db += 1
        if lista[0][y] == "o" and lista[1][y] == "x":
            db += 1
        if lista[-1][y] == "o" and lista[-1][y] == "x":
            db += 1
print(f"{db} ilyen „egyedülálló” üres hely van a nézőtéren")
print("7. feladat\nA fájlba írás elkészült")
f = open("szabad.txt", "w")
a = ""
for i in range(0, 15):
    for y in range(0, 20):
        if lista[i][y] == "x":
            a += "x"
        else:
            a += lista2[i][y]
db = 0
for i in a:
    f.write(f"{i}")
    db += 1
    if db % 20 == 0:
        f.write("\n")
