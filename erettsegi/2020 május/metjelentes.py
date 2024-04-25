class Jelentes:
    def __init__(self, telepules, ido, iranyero, homerseklet):
        self.telepules = telepules
        self.ido = ido
        self.iranyero = iranyero
        self.homerseklet = int(homerseklet)

    def __repr__(self):
        return f"{self.telepules} {self.ido} {self.iranyero} {self.homerseklet}"

    def oopp(self):
        a = self.ido
        b = a[0:2] + ":" + a[2:4]
        return b

    def szelerosseg(self):
        a = self.iranyero
        b = "#"
        return int(a[3:5]) * b

    def ora(self):
        a = self.ido
        b = a[0:2]
        return int(b)


lista = []
f = open("tavirathu13.txt")
for i in f:
    i = i.strip().split()
    lista.append(Jelentes(*i))
print("2. feladat")

a = input("Adja meg egy település kódját! Település:  ")
utolso = ""
for i in lista:
    if a == i.telepules:
        utolso = i.oopp()
print(f"Az utolsó mérési adat a megadott településről {utolso}-kor érkezett.\n3. feladat ")
hofokok = [i.homerseklet for i in lista]
max = max(hofokok)
min = min(hofokok)
for i in lista:
    if min == i.homerseklet:
        print(f"A legalacsonyabb hőmérséklet: {i.telepules} {i.oopp()} {min} fok. ")
for i in lista:
    if max == i.homerseklet:
        print(f"A legmagasabb hőmérséklet: {i.telepules} {i.oopp()} {max} fok.\n4. feladat ")
        break
szelcsend = 0
for i in lista:
    if i.iranyero == "00000":
        print(f"{i.telepules} {i.oopp()}")
        szelcsend += 1
if szelcsend == 0:
    print(f"Nem volt szélcsend a mérések idején.")
print("5. feladat")
telepules = set()
for i in lista:
    telepules.add(i.telepules)

for i in telepules:
    jelenlegi = 0
    min = ""
    max = ""
    nullazo = False
    db = 0
    szum = 0
    egy = False
    het = False
    tizenharom = False
    tizekilenc = False
    for j in lista:
        if i == j.telepules:
            jelenlegi = j.homerseklet
            if nullazo == False:
                min = j.homerseklet
                max = j.homerseklet
                nullazo = True
            if max < jelenlegi:
                max = jelenlegi
            if min > jelenlegi:
                min = jelenlegi
            if j.ora() == 1 or j.ora() == 7 or j.ora() == 13 or j.ora() == 19:
                szum += j.homerseklet
                db += 1
                if j.ora() == 1:
                    egy = True
                if j.ora() == 7:
                    het = True
                if j.ora() == 13:
                    tizenharom = True
                if j.ora() == 19:
                    tizekilenc = True
    if tizenharom and tizenharom and het and egy:
        print(f"{i} Középhőmérséklet: {round(szum / db)}; Hőmérséklet-ingadozás: {max - min} ")
    else:
        szum = "NA"
        print(f"{i} {szum}; Hőmérséklet-ingadozás: {max - min} ")

print("6. feladat\nA fájlok elkészültek")

for j in telepules:
    bc = j
    xd = open(f"{bc}.txt", "w", encoding="UTF-8")
    xd.write(f"{bc}\n")
    for i in lista:
        if bc == i.telepules:
            xd.write(f"{i.oopp()} {i.szelerosseg()}\n")
