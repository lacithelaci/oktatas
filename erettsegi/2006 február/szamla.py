class Hivas:
    def __init__(self, kora, kperc, kms, vora, vperc, vms, telszam):
        self.kora = int(kora)
        self.kperc = int(kperc)
        self.kms = int(kms)
        self.vora = int(vora)
        self.vperc = int(vperc)
        self.vms = int(vms)
        self.telszam = telszam

    def __repr__(self):
        return f"{self.kora} {self.kperc} {self.kms} {self.vora} {self.vperc} {self.vms} {self.telszam}"

    def kossz(self):
        ossz = self.kora * 3600 + self.kperc * 60 + self.kms
        return ossz

    def vossz(self):
        ossz = self.vora * 3600 + self.vperc * 60 + self.vms
        return ossz

    def beszelt(self):
        c = self.vossz() - self.kossz()
        maradek = c % 60
        c = c // 60
        if maradek != 0:
            maradek = 1
        return c + maradek

    def vezetekes(self):
        mobil = False
        if self.telszam[0:2] == "39" or self.telszam[0:2] == "41" or self.telszam[0:2] == "71":
            mobil = True
        return mobil


def szamlazott(o, p, ms):
    ossz = o * 3600 + ms + p * 60
    return ossz


def fizetett(a, b):
    c = a - b
    maradek = c % 60
    c = c // 60
    if maradek != 0:
        maradek = 1
    return c + maradek


f = open("HIVASOK.txt")
lista = []
for i in f:
    i = i.strip().split()
    i2 = f.readline()
    lista.append(Hivas(*i, i2))
print("1.feladat")
tel = input("Adjon meg egy telefonszámot")
if tel[0:2] == "39" or tel[0:2] == "41" or tel[0:2] == "71":
    print("Mobil\n2.feladat")
else:
    print("Vezetékes\n2.feladat")
a = int(input("Adjon meg egy időpontot"))
b = int(input())
c = int(input())
d = int(input("Adjon meg egy időpontot"))
e = int(input())
f = int(input())
print(f"A kiszámított időtartam {fizetett(szamlazott(d, e, f), szamlazott(a, b, c))} perc")
f = open("percek.txt", "w")
for i in lista:
    f.write(f"{i.beszelt()} {i.telszam}")
csucs = 0
kivul = 0
for i in lista:
    if i.kossz() >= 7 * 3600 and i.kossz() <= 18 * 3600:
        csucs += 1
    else:
        kivul += 1
print(f"3.feladat - 4.feladat\n{csucs} hívás volt csúcsidőben és csúcsidőn kívül {kivul} hívás volt.")
vezetekes = 0
mobil = 0
for i in lista:
    if i.vezetekes():
        mobil += i.beszelt()
    else:
        vezetekes += i.beszelt()
print(f"5.feladat\n{mobil} percet beszélt a felhasználó mobil számmal és {vezetekes} percet vezetékessel")
vezetekes = 0
mobil = 0
for i in lista:
    if i.kossz() >= 7 * 3600 and i.kossz() <= 18 * 3600:
        if i.vezetekes():
            mobil += i.beszelt() * 69.175
        else:
            vezetekes += i.beszelt() * 30
ossz = mobil + vezetekes
print(f"6. feladat\n{ossz} forintot kell fizetnie a felhasználónak a csúcsdíjas hívásokért!")
