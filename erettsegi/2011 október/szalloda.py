class Szalloda:
    def __init__(self, sorszam, szobaszam, erkezesnap, tavozasnap, vendegszam, reggeli, az):
        self.sorszam = int(sorszam)
        self.szobaszam = int(szobaszam)
        self.erkezesnap = int(erkezesnap)
        self.tavozasnap = int(tavozasnap)
        self.vendegszam = int(vendegszam)
        self.reggeli = int(reggeli)
        self.az = az

    def __repr__(self):
        return f"{self.sorszam} {self.szobaszam} {self.erkezesnap} {self.tavozasnap} {self.vendegszam} {self.reggeli} {self.az}"

    def tartozkodas(self):
        return self.tavozasnap - self.erkezesnap + 1

    def kifizetni(self):
        osszeg = 0
        for i in range(self.erkezesnap, self.tavozasnap):
            if i <= 121:
                osszeg += 9000
            elif i <= 244:
                osszeg += 10000
            else:
                osszeg += 8000
        if self.vendegszam > 2:
            osszeg += 2000 * self.tartozkodas()
        if self.reggeli == 1:
            osszeg += (self.tartozkodas() - 1) * 1100 * self.vendegszam
        return osszeg


def honap(a):
    if a <= 31:
        return f"1"
    elif a <= 59:
        return f"2"
    elif a <= 90:
        return f"3"
    elif a <= 120:
        return f"4"
    elif a <= 151:
        return f"5"
    elif a <= 181:
        return f"6"
    elif a <= 212:
        return f"7"
    elif a <= 243:
        return f"8"
    elif a <= 273:
        return f"9"
    elif a <= 304:
        return f"10"
    elif a <= 334:
        return f"11"

    elif a <= 365:
        return f"12"
def honap2(a):
    lista=[1,31,59,90,120,151,181,212,243,273,304,334]
    db=0
    szamlalo=0
    elozo=""
    jelenlegi=""
    for i in lista:
        jelenlegi=i
        szamlalo+=1
        db += 1
        if szamlalo>=1:
            if jelenlegi>=a and elozo<=a:

                return db
                break
        elozo=jelenlegi

print(honap2(2))
f = open("pitypang.txt")
lista = []
elso_sor = f.readline()
for i in f:
    i = i.strip().split()
    lista.append(Szalloda(*i))
print("2. feladat")
hossz = [i.tartozkodas() for i in lista]
masz = max(hossz)
for i in lista:
    if i.tartozkodas() == masz:
        print(f"{i.az}({i.erkezesnap}) – {i.tartozkodas()}")
f = open("bevetel.txt", "w", encoding="utf-8")
osszeg = 0
for i in lista:
    f.write(f"{i.sorszam}:{i.kifizetni()}\n")
    osszeg += i.kifizetni()
print("3. feladat\nA szálloda bevétele: ", str(osszeg) + " Ft")
print("4. feladat")
szotar = {}
for i in lista:
    for i in range(i.erkezesnap, i.tavozasnap + 1):
        szotar[honap(i)] = szotar.get(honap(i), 0) + 1
for index, i in szotar.items():
    print(f"{index} : {i} vendégéj")
print("5. feladat")
kezd = int(input("Kezdet"))
veg = int(input("Vég"))
foglalt = set()
szobak = set(i for i in range(1, 28))
szabad=True
for i in lista:
    szabad=True
    for y in range(kezd,veg+1):
        for y2 in range(i.erkezesnap,i.tavozasnap+1):
            if y==y2:
                szabad=False
    if not szabad:
        foglalt.add(i.szobaszam)


kulonbseg=szobak.difference(foglalt)
print("Szabad szobák száma: ",len(kulonbseg))
if len(kulonbseg)!=0:
    for i in range(1):
        print("Ezek a szábák:",end=" ")
        for y in kulonbseg:
            print(y,end=" ")


