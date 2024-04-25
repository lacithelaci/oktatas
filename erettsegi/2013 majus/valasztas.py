f = open("szavazatok.txt")
lista = []
for i in f:
    i = i.strip().split()
    lista.append(i)
print(f"2. feladat\nA helyhatósági választáson {len(lista)} képviselőjelölt indult.\n3. feladat")
a = "Ablak"
b = "Antal"
volt = False
for i in lista:
    if i[2] == a and i[3] == b:
        print(f"{a} {b} {i[1]} szavazatot kapott!")
        volt = True
if not volt:
    print("Ilyen nevű képviselőjelölt nem szerepel a nyilvántartásban!")
print("4. feladat")
db = 0
for i in lista:
    db += int(i[1])
print(f"A választáson {db} állampolgár, a jogosultak {(db / 12345) * 100:.2f}%-a vett részt.\n5. feladat")


def teljes(a):
    if a == "GYEP":
        return f"Gyümölcsevők Pártja"
    if a == "HEP":
        return f"Húsevők Pártja"
    if a == "TISZ":
        return f"Tejivók Szövetsége"
    if a == "ZEP":
        return f"Zöldségevők Pártja"
    if a == "-":
        return f"Független jelöltek"


szotar = {}
for i in lista:
    szotar[i[4]] = szotar.get(i[4], 0) + int(i[1])
for index, i in szotar.items():
    print(f"{teljes(index)}= {((i / db) * 100):.2f}%")


def fuggetlen(a):
    if a == "-":
        return f"független"
    else:
        return a

print("6. feladat")
masz = [int(i[1]) for i in lista]
for i in lista:
    if int(i[1]) == max(masz):
        print(f"{i[2]} {i[3]} {fuggetlen(i[4])}")





