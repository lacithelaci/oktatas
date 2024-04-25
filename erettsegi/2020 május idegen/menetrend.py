class Menetrend:
    def __init__(self, vonataz, vasutaz, ora, perc, indul_vagy_erkezik):
        self.vonataz = int(vonataz)
        self.vasutaz = int(vasutaz)
        self.ora = int(ora)
        self.perc = int(perc)
        self.indul_vagy_erkezik = indul_vagy_erkezik

    def __repr__(self):
        return f"{self.vonataz} {self.vasutaz} {self.ora} {self.perc} {self.indul_vagy_erkezik}"


lista = []
f = open("vonat.txt")
for i in f:
    i = i.strip().split("\t")
    lista.append(Menetrend(*i))
vonatok = set(i.vonataz for i in lista)
vasut = set(i.vasutaz for i in lista)
print(f"2. feladat\nAz állomások száma: {len(vasut)}\nA vonatok száma: {len(vonatok)}")
print("3. feladat")
elozo=""
jelenlegi=""
elozo_az=""
jelenlegi_az=""
msz=0
db=0
for i in sorted(lista,key=lambda i:(i.vonataz)):
    jelenlegi=i.ora+i.perc
    jelenlegi_az=i.vonataz
    if db>1:
        if elozo_az==jelenlegi_az:
            if elozo-jelenlegi>msz:
                msz=elozo-jelenlegi
    elozo_az=i.vonataz
    elozo=jelenlegi
    db+=1
print(msz)