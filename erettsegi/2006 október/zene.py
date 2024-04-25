class Zene:
    def __init__(self, ado, perc, ms, cim):
        self.ado = int(ado)
        self.perc = int(perc)
        self.ms = int(ms)
        self.cim = cim

    def __repr__(self):
        return f"{self.ado} {self.perc} {self.ms} {self.cim}"

    def msbe(self):
        return self.perc * 60 + self.ms


def ooppms(a):
    ora = a // 3600
    perc = (a - (ora * 3600)) // 60
    ms = a - (ora * 3600 + perc * 60)
    return f"{ora}:{perc}:{ms}"


f = open("musor.txt")
elso_sor = f.readline()
lista = []
for i in f:
    i1 = i[0:6].strip().split()
    i2 = i[6:].strip()
    lista.append(Zene(i1[0], i1[1], i1[2], i2))
print("2. feladat")
szotar = {}
for i in lista:
    szotar[i.ado] = szotar.get(i.ado, 0) + 1
for index, i in szotar.items():
    print(f"{index} adó : {i} szám")
print("3. feladat")
ado1 = [i for i in lista if i.ado == 1]
db = 0
for i in ado1:
    if i.cim.__contains__("Eric Clapton"):
        db += 1
szum = 0
db2 = 0
for i in ado1:
    if db2 >= 1 and db2 <= db:
        szum += i.msbe()
    if i.cim.__contains__("Eric Clapton"):
        db2 += 1
print(f"{ooppms(szum)} telt el.\n4. feladat")
hallhato = 0
ado = None
adok = set(i for i in range(1, 4))
for i in lista:
    if i.cim == "Omega:Legenda":
        ado = i.ado
        adok.discard(ado)
        break
for i in lista:
    if i.ado == ado:
        hallhato += i.msbe()
    if i.cim == "Omega:Legenda":
        break
print(f"{ado}. adón hallható az Omega:Legenda")
cim = ""
hallhato2 = 0
for y in adok:
    cim = ""
    hallhato2 = 0
    for i in lista:

        if i.ado == y:
            if hallhato >= hallhato2:
                cim = i.cim
                hallhato2 += i.msbe()

    print(f"{y}. adó: {cim}")
print("6. feladat")


def tartalmaz(a, b):
    db = 0
    for i in a:
        if b.__contains__(i):
            db += 1
    return len(a) == db



def megoldas(a, b):
    c = ""
    a = a.lower()
    b = b.lower()
    hossz = 0
    for i in a:
        for y in b[hossz:]:
            if i == y:
                c += y
                hossz = b.index(y)
                hossz+=1
                break
    return c == a


szoreszlet = "gaoaf"
masik = open("keres.txt", "w")
for i in lista:
    if megoldas(szoreszlet, i.cim):
        masik.write(f"{i.cim}\n")
ado1 = [i for i in lista if i.ado == 1]
ora = 0
aktido = 180
for i in ado1:
    akthossz = 60 + i.perc * 60 + i.ms
    if aktido + akthossz > 60 * 60:
        aktido = 180 + akthossz
    else:
        aktido = aktido + akthossz
print(f"{ooppms(aktido)}")
