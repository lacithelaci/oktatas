class Telefon:
    def __init__(self, ora1, perc1, ms1, ora2, perc2, ms2):
        self.ora1 = int(ora1)
        self.perc1 = int(perc1)
        self.ms1 = int(ms1)
        self.ora2 = int(ora2)
        self.perc2 = int(perc2)
        self.ms2 = int(ms2)
        self.sorszam = 0

    def __repr__(self):
        return f"{self.ora1} {self.perc1} {self.ms1} {self.ora2} {self.perc2} {self.ms2} {self.sorszam}"

    def ossz1(self):
        return self.ora1 * 3600 + self.perc1 * 60 + self.ms1

    def ossz2(self):
        return self.ora2 * 3600 + self.perc2 * 60 + self.ms2
    def opms2(self):
        return f"{self.ora2} {self.perc2} {self.ms2}"

def msbe(o, p, ms):
    o = o * 3600
    p = p * 60
    return ms + o + p


lista = []
f = open("hivas.txt")
for i in f:
    i = i.strip().split()
    lista.append(Telefon(*i))
for index, i in enumerate(lista):
    i.sorszam = index + 1
print("3. feladat")
szotar = {}
for i in lista:
    szotar[i.ora1] = szotar.get(i.ora1, 0) + 1
for index, i in szotar.items():
    print(f"{index} ora {i} hivas")
print("4. feladat")
max = 0
indexe = 0
for i in lista:
    if i.ossz2() - i.ossz1() > max:
        max = i.ossz2() - i.ossz1()
        indexe = i.sorszam
print(f"A leghosszabb ideig vonalban levo hivo {indexe}. sorban szerepel, a hivas hossza: {max} masodperc.\n5. feladat")
ora = 10
perc = 11
ms = 12
a = msbe(ora, perc, ms)
db = 0
varakozok = []
for i in lista:
    if a >= i.ossz1() and a <= i.ossz2():
        db += 1
        varakozok.append(i.sorszam)
print(f"A varakozok szama: {db - 1} a beszelo a {varakozok[0]}. hivo.")
print("6. feladat")
helyesek = []
max = 0
for i in lista:
    if i.ora1 < 12 and i.ora2>=8:
        if max < i.ossz2():
            max = i.ossz2()
            helyesek.append(i)
max = helyesek[-2].ossz2() - helyesek[-1].ossz1()
print(f"Az utolso telefonalo adatai a(z) {helyesek[-1].sorszam}. sorban vannak, {max} masodpercig vart.")
y=open("sikeres.txt","w")
first="8 0 0"
for index,i in enumerate(helyesek):
    i.sorszam=index+1
    y.write(f"{i.sorszam} {first} {i.opms2()}\n")
    first=i.opms2()