class Helyjegy:
    def __init__(self, hely, kezdet, veg):
        self.hely = int(hely)
        self.kezdet = int(kezdet)
        self.veg = int(veg)
        self.sorszam = 0

    def __repr__(self):
        return f"{self.hely} {self.kezdet} {self.veg}"

    def utazott(self):
        return self.veg - self.kezdet


def kerekites(a, b, c):
    d = a - b
    if d % 10 != 0:
        d = int(d / 10)
        d = d + 1
    else:
        d = int(d / 10)
    d = d * c
    if d % 10 == 1 or d % 10 == 2:
        d = int(d / 10) * 10
    if d % 10 == 8 or d % 10 == 9:
        d = int(d / 10) * 10 + 10
    if d % 10 == 6 or d % 10 == 7:
        d = int(d / 10) * 10 + 5
    if d % 10 == 3 or d % 10 == 4:
        d = int(d / 10) * 10 + 5
    return d


f = open("eladott.txt")
elso_sor = f.readline()
elso_sor = elso_sor.split()
lista = []
for i in f:
    i = i.strip().split()
    lista.append(Helyjegy(*i))
for index, i in enumerate(lista):
    a = i.hely
    b = i.utazott()
    i.sorszam = index + 1
print(f"2. feladat\nA legutolsó jegyvásárló ülésének sorszáma: {a} és az általa beutazott távolság: {b} km\n3. feladat")
for i in lista:
    if str(i.utazott()) == elso_sor[1]:
        print(i.sorszam, end=" ")
print("\n4. feladat")
szum = 0
for i in lista:
    szum += kerekites(i.veg, i.kezdet, int(elso_sor[2]))
print(f"A jegyekből {szum} Ft bevétele származott a társaságnak.")
megallo = set()
for i in lista:
    megallo.add(i.veg)
megallo = sorted(megallo)
u1 = megallo[-2]
fel = 0
le = 0
for i in lista:
    if i.veg == u1:
        le += 1
    if i.kezdet == u1:
        fel += 1
print(f"5. feladat \nA busz végállomást megelőző utolsó megállásánál {fel} szálltak fel és {le} le")
print(f"6. feladat\n{len(megallo)}-szer állt meg")
ulesek=set()
for i in range(1,49):
    ulesek.add(i)
ures="üres"
f=open("kihol.txt","w",encoding="utf-8")
ido=int(input("Kérek egy km-et"))
for y in ulesek:
    ures="üres"
    for i in lista:
        if y==i.hely:
            if i.kezdet<=ido and i.veg>ido:
                ures=f"{i.sorszam}. utas"
    f.write(f"{y}. ülés: {ures}\n")


