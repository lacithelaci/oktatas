f = open("melyseg.txt")
lista = []
for i in f:
    i = i.strip()
    lista.append(i)
print("1. feladat\nA fájl adatainak száma:", len(lista))
print("2. feladat ")
a = int(input("Adjon meg egy távolságértéket! "))
xd = ""
for index, i in enumerate(lista):
    if a - 1 == index:
        print(f"Ezen a helyen a felszín {i} méter mélyen van. ")
        xd = i
        break
print("3. feladat")
db = 0
for i in lista:
    if i == "0":
        db += 1
print(f"Az érintetlen terület aránya {(db / len(lista) * 100):.2f}%. ")
f = open("godrok.txt", "w")
jelenlegi = ""
db = 0
for i in lista:
    elozo = i
    if i != "0":
        f.write(f"{i} ")
    if db != 0:
        if elozo == "0" and jelenlegi != "0":
            f.write(f"\n")
    jelenlegi = i
    db += 1
print("5. feladat")
f = open("godrok.txt")
lista2 = []
for i in f:
    i = i.strip()
    lista2.append(i)
print("A gödrök száma:", len(lista2))
print("6. feladat")
if xd != "0":
    db = 0
    for index, i in enumerate(lista):
        if i == "0":
            db += 1
        if index + 1 == a:
            break
    hely = a - db
    db2 = 0
    indesz = 0
    for index, i in enumerate(lista2):

        for y in i:
            db2 += 1
        if db2 == 3:
            indesz = index
            break
    db2 = 0
    godor = ""
    for index, i in enumerate(lista2):
        if index <= indesz:
            for y in i:
                if y != " ":
                    db2 += 1
        if index == indesz:
            godor = i
    print(f"a)\nA gödör kezdete: {(db2+db - (a+db))} méter, a gödör vége: {db2 + a - hely} méter. ")
    godor = godor.replace(" ", "")
    godorke = [int(i) for i in godor]
    elozo = 0
    valtozas = False
    lehet = True
    elso = 0
    masodik = 0
    harmadik = 0
    for i in godorke:
        if i > elozo:
            elso = 1
        else:
            masodik = 1
            valtozas = True
        if valtozas and i > elozo:
            harmadik = 1
        if i == elozo:
            lehet = False
        elozo = i
    ossz = elso + masodik + harmadik
    print("b)")
    if lehet and ossz == 2:
        print("Folyamatosan mélyül")
    else:
        print("Nem mélyül folyamatosan")
    print(f"c)\nA legnagyobb mélysége {max(godorke)} méter. ")
    print(f"d)\nA térfogata {sum(godorke) * 10} m^3. ")
    print(f"e)\nA térfogata {(sum(godorke) - len(godorke)) * 10} m^3. ")
else:
    print("Az adott helyen nincs gödör.")
