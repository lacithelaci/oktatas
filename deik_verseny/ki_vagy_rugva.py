class Ki_vagy_rugva:
    def __init__(self, nev, fizetes):
        self.nev = nev
        self.fizetes = int(fizetes)

    def __repr__(self):
        return f"{self.nev} {self.fizetes}"


elso_sor = input().split()
felszabaditando_osszeg = int(elso_sor[1])
max_kirughato_fo = int(elso_sor[2])
lista = []
db1 = 0
while db1 != int(elso_sor[0]):
    lista.append(Ki_vagy_rugva(*input().strip().split()))
    db1 += 1
szum = 0
nevek = []
db = 0
for i in sorted(lista, key=lambda i: (i.fizetes), reverse=True):
    szum += i.fizetes
    db += 1
    nevek.append(i.nev)
    if szum >= felszabaditando_osszeg:
        break
if db <= max_kirughato_fo and felszabaditando_osszeg <= szum:
    print(db)
    for i in lista:
        if i.nev in nevek:
            print(f"{i.nev}, YOU ARE FIRED!")
else:
    print("impossible")
