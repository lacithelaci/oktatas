class Radio:
    def __init__(self, nap, id, uzenet):
        self.nap = int(nap)
        self.id = int(id)
        self.uzenet = uzenet

    def __repr__(self):
        return f"{self.nap} {self.id} {self.uzenet}"

    def darabolt(self):
        a = self.uzenet.split()
        return a


f = open("veetel.txt")
lista = []
for i in f:
    i = i.strip().split()
    i2 = f.readline().strip()
    lista.append(Radio(*i, i2))
print("2. feladat")
for i in lista:
    print("Az első üzenet rögzítője:", i.id)
    break
a = ""
for i in lista:
    a = i.id
print("Az utolsó üzenet rögzítője:", a)
print("3. feladat")
for i in lista:
    if i.uzenet.__contains__("farkas"):
        print(f"{i.nap}. nap {i.id}. rádióamatör")
print("4. feladat")
halmaz = set()
for i in range(1, 12):
    halmaz.add(i)
db = 0
asd = 0
for y in sorted(halmaz):
    db = 0
    for i in lista:
        if i.nap == y:
            db += 1
    asd += db
    print(f"{y}. nap: {db} rádióamatőr")


def szame(szo):
    valasz = True
    for i in range(1, len(szo)):

        if szo[i] < '0' or szo[i] > '9':
            valasz = False

    szame = valasz
    return szame


f2 = open("adaas.txt", "w", encoding="utf-8")
c = ""
d = ""
segedlista = []
for y3 in halmaz:
    segedlista = []
    for i in lista:
        if i.nap == y3:
            segedlista.append(i.uzenet)
        d = ""
        for y in range(90):

            d = "#"
            for y2 in segedlista:

                if y2[y] != "#":
                    d = y2[y]
            c += d
    f2.write(f"{c[-90:]}\n")
print("7. feladat")
nap = int(input("Adja meg a nap sorszámát!  "))
amator = int(input("Adja meg a rádióamatőr sorszámát!"))
van = False
for i in lista:
    if nap == i.nap and amator == i.id:
        van = True
        if i.uzenet[0:4].__contains__("#"):
            print("Nincs információ")
            break
        else:
            if szame(i.uzenet[0]) and szame(i.uzenet[2]):
                print(f"A megfigyelt egyedek száma: {int(i.uzenet[0]) + int(i.uzenet[2])}")
            else:
                print("Nincs információ")
if not van:
    print("Nincs ilyen feljegyzés")
