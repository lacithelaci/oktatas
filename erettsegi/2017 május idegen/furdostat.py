class Furdo:
    def __init__(self, az, furdoaz, kibe, ora, perc, ms):
        self.az = int(az)
        self.furdoaz = int(furdoaz)
        self.kibe = int(kibe)
        self.ora = int(ora)
        self.perc = int(perc)
        self.ms = int(ms)

    def __repr__(self):
        return f"{self.az} {self.furdoaz} {self.kibe} {self.ora} {self.perc} {self.ms}"

    def hova(self):
        if self.kibe == 0:
            return f"be"
        else:
            return f"ki"

    def ora_perc_ms(self):
        return f"{self.ora}:{self.perc}:{self.ms}"

    def masodperc(self):
        a = self.perc * 60
        b = self.ms
        c = self.ora * 3600
        return a + b + c


def vissza(a):
    ora = a // 3600
    perc = a // (60) - ora * 60
    ms = a - (ora * 3600 + perc * 60)
    return f"{ora}:{perc}:{ms}"


lista = []
f = open("furdoadat.txt")
for i in f:
    i = i.strip().split(" ")
    lista.append(Furdo(*i))
print("2. feladat")
lista2 = []
for i in lista:
    if i.hova() == "ki" and i.furdoaz == 0:
        lista2.append(i.ora_perc_ms())
print(
    f"Az első vendég {lista2[0]}-kor lépett ki az öltözőből.\nAz utolsó vendég {lista2[-1]}-kor lépett ki az öltözőből.  ")
print("3. feladat")
szotar = {}
for i in lista:
    szotar[i.az] = szotar.get(i.az, 0) + 1
db = 0
for i in szotar.values():
    if i == 4:
        db += 1
print(f"A fürdőben {db} vendég járt csak egy részlegen. ", )
print("4. feladat\nA legtöbb időt eltöltő vendég: ")
vendegek = set()
for i in lista:
    vendegek.add(i.az)
max = 0
vendeg = 0
for y in vendegek:
    az = y
    volt = True
    kint = 0
    bent = 0
    for i in lista:
        if i.az == az:
            if volt:
                if i.hova() == "ki":
                    bent = i.masodperc()
                    volt = False
            if i.hova() == "be":
                kint = i.masodperc()
        if max < kint - bent:
            max = kint - bent
            vendeg = i.az
print(f"{vendeg}. vendég {vissza(max)} \n5. feladat")
kilenc = set()
kil = 9 * 60 * 60
tizenhat = set()
husz = set()
for i in lista:
    if kil >= i.masodperc():
        kilenc.add(i.az)
    elif 16 * 3600 >= i.masodperc():
        tizenhat.add(i.az)
    elif 20 * 3600 >= i.masodperc():
        husz.add(i.az)
b = tizenhat.difference(kilenc)
a = husz.difference(tizenhat)
print(f"6-9 óra között {len(kilenc)} vendég\n9-16 óra között {len(b)} vendég\n16-20 óra között {len(a)} vendég ")
print("6. feladat")
print("Kész a fájl")
x = open("szauna.txt", "w", encoding="UTF-8")
osszeg = 0
for y in vendegek:
    az = y
    volt = True
    volt2 = True
    kint = 0
    bent = 0
    szum = 0
    osszeg = 0
    for i in lista:
        if i.az == az and i.furdoaz == 2:
            if volt:
                if i.hova() == "ki":
                    bent = i.masodperc()
                    volt = False
            if volt2:
                if i.hova() == "be":
                    kint = i.masodperc()
                    volt2 = False
            if volt == False and volt2 == False:
                szum = kint - bent
                volt = True
                volt2 = True
            osszeg -= szum
    if osszeg > 0:
        x.write(f"{y} {vissza(osszeg)}\n")
print("7. feladat")
uszoda = set()
szauna = set()
gyogyviz = set()
strand = set()
for i in lista:
    if i.furdoaz == 1:
        uszoda.add(i.az)
    if i.furdoaz == 2:
        szauna.add(i.az)
    if i.furdoaz == 3:
        gyogyviz.add(i.az)
    if i.furdoaz == 4:
        strand.add(i.az)
print(f"Uszoda: {len(uszoda)}\nSzaunák: {len(szauna)}\nGyógyvizes medencék: {len(gyogyviz)}\nStrand: {len(strand)}    ")
