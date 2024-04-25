hossz = False
szabalyos_karakter = True
szabalyos_lepes = True
osszes_karakter = input().strip().split()
lista = []
db = 0


def megallapit_resztabla(sor, oszlop):
    resztabla_sor = sor // 4
    resztabla_oszlop = oszlop // 4
    resztabla_szam = resztabla_sor * 4 + resztabla_oszlop + 1
    return resztabla_szam


while db != 16:
    beolvasando = input().strip().split()
    lista.append(beolvasando)
    db += 1
ismetles_nelkuli = set()
for i in lista:
    for y in i:
        ismetles_nelkuli.add(y)
if len(ismetles_nelkuli) == 16:
    hossz = True

for i in ismetles_nelkuli:
    for y in i:
        if y not in osszes_karakter:
            szabalyos_karakter = False
for i in range(0, 16):
    lepesellenorzo = set()
    for y in range(0, 16):
        lepesellenorzo.add(y)
    if len(lepesellenorzo) != 16:
        szabalyos_lepes = False


lepesellenorzo = set()
for resztabla1 in range(1, 17):
    for i in range(0, 16):
        for y in range(0, 16):
            if megallapit_resztabla(i, y) == resztabla1:
                lepesellenorzo.add(lista[i][y])
    if len(lepesellenorzo) != 16:
        szabalyos_lepes = False
    lepesellenorzo = set()

if hossz and szabalyos_lepes and szabalyos_karakter:
    print("VALID")
else:
    print("INVALID")
