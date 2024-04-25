#  Copyright (c) 2022.
#  A forráskód készítője: Ladányi Attila
#  Tanulság: először olvass és csak utána írd a programot

bszam = int(input("1. feladat\nAdja meg a számlálót: "))
bnev = int(input("Adja meg a nevezőt: "))

if bszam % bnev == 0:
    print("Egész")
else:
    print("Nem egész")


def lnko(a, b):
    if a == b:
        return a
    elif a < b:
        return lnko(a, b - a)
    elif a > b:
        return lnko(a - b, b)


kozososzto = lnko(bszam, bnev)

if bszam % bnev == 0:
    print(f"\n3. feladat\n{bszam}/{bnev} = {int(bszam / bnev)}")
else:
    print(f"\n3. feladat\n{bszam}/{bnev} = {int(bszam / kozososzto)}/{int(bnev / kozososzto)}")

bszammasik = int(input("\n4. feladat\nAdja meg a számlálót: "))
bnevmasik = int(input("Adja meg a nevezőt: "))


def osszead(szamlalo, nevezo, masikszamlalo, masiknevezo):
    veg = [szamlalo * masikszamlalo, nevezo * masiknevezo]

    lko = lnko(veg[0], veg[1])

    if not veg[0] % veg[1] == 0:
        veger = f"{szamlalo}/{nevezo} * {masikszamlalo}/{masiknevezo} = {veg[0]}/{veg[1]} = {int(veg[0] / lko)}/{int(veg[1] / lko)}"
    else:
        veger = f"{szamlalo}/{nevezo} * {masikszamlalo}/{masiknevezo} = {veg[0]}/{veg[1]} = {int(veg[0] / veg[1])}"

    return veger


print(f"{osszead(bszam, bnev, bszammasik, bnevmasik)}")


def lkkt(a, b):
    return a * b / lnko(a, b)


def szoroz(szamlalo, nevezo, masikszamlalo, masiknevezo):
    veg = [szamlalo * lkkt(nevezo, masiknevezo) + masikszamlalo * lkkt(nevezo, masiknevezo),
           masiknevezo * lkkt(nevezo, masiknevezo)]

    if not veg[0] % veg[1] == 0:
        veger = f"{szamlalo}/{nevezo} + {masikszamlalo}/{masiknevezo} = {int(szamlalo * lkkt(nevezo, masiknevezo))}/{int(nevezo * lkkt(nevezo, masiknevezo))} + {int(masikszamlalo * lkkt(nevezo, masiknevezo))}/{int(masiknevezo * lkkt(nevezo, masiknevezo))} = {int(veg[0])}/{int(veg[1])} = {int(veg[0] / lnko(veg[0], veg[1]))}/{int(veg[1] / lnko(veg[0], veg[1]))}"
    else:
        veger = f"{szamlalo}/{nevezo} + {masikszamlalo}/{masiknevezo} = {int(szamlalo * lkkt(nevezo, masiknevezo))}/{int(nevezo * lkkt(nevezo, masiknevezo))} + {int(masikszamlalo * lkkt(nevezo, masiknevezo))}/{int(masiknevezo * lkkt(nevezo, masiknevezo))} = {int(veg[0])}/{int(veg[1])} = {int(veg[0] / veg[1])}"

    return veger


print(f"\n6. feladat\n{szoroz(bszam, bnev, bszammasik, bnevmasik)}")

f = open("eredmeny.txt", "w", encoding="utf-8")

for i in open("adat.txt", "r", encoding="utf-8"):
    i = i.strip().split()

    egyikszam = int(i[0])
    egyiknev = int(i[1])
    masikszam = int(i[2])
    masiknev = int(i[3])
    muvelet = i[4]

    if muvelet == "+":
        f.write(f"{osszead(egyikszam, egyiknev, masikszam, masiknev)}\n")
    elif muvelet == "*":
        f.write(f"{szoroz(egyikszam, egyiknev, masikszam, masiknev)}\n")
