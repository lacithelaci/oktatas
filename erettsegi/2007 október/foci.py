# foci.py

class Meccs:
    def __init__(self, fordulo, haza_gol, vendeg_gol, f_haza_gol, f_vendeg_gol, haza_csapat, vendeg_csapat):
        self.fordulo = int(fordulo)
        self.haza_gol = int(haza_gol)
        self.vendeg_gol = int(vendeg_gol)
        self.f_haza_gol = int(f_haza_gol)
        self.f_vendeg_gol = int(f_vendeg_gol)
        self.haza_csapat = haza_csapat
        self.vendeg_csapat = vendeg_csapat

    def __str__(self):
        return f"{self.fordulo}. forduló: {self.haza_csapat} {self.haza_gol}-{self.vendeg_gol} {self.vendeg_csapat} (félidő: {self.f_haza_gol}-{self.f_vendeg_gol})"


# --------------------------
# 1. feladat: beolvasás
# --------------------------
meccsek = []

try:
    f = open("meccs.txt", "r", encoding="utf-8")
    sorok = f.read().splitlines()
    f.close()

    for sor in sorok[1:]:
        adatok = sor.split()
        meccsek.append(Meccs(*adatok))

except FileNotFoundError:
    print("A meccs.txt fájl nem található. Az első 10 mérkőzés betöltve programon belül.")
    pelda_meccsek = [
        "14 1 2 0 2 Agarak Ovatosak",
        "5 4 0 1 0 Erosek Agarak",
        "4 0 2 0 2 Ijedtek Hevesek",
        "8 1 1 0 0 Ijedtek Nyulak",
        "8 3 2 3 1 Lelkesek Bogarak",
        "13 0 1 0 1 Fineszesek Csikosak",
        "2 1 0 0 0 Pechesek Csikosak",
        "1 4 0 2 0 Csikosak Kedvesek",
        "9 2 0 0 0 Nyulak Lelkesek",
        "6 0 2 0 0 Ovatosak Nyulak"
    ]
    for sor in pelda_meccsek:
        adatok = sor.split()
        meccsek.append(Meccs(*adatok))

# --------------------------
# kiírás
# --------------------------
# --------------------------
# 2. feladat
# --------------------------
print("2. feladat:")
fordulo_szam = int(input("Adja meg a forduló számát: "))

# az adott forduló mérkőzései
fordulo_meccsek = [m for m in meccsek if m.fordulo == fordulo_szam]

for m in fordulo_meccsek:
    print(f"{m.haza_csapat}-{m.vendeg_csapat}: {m.haza_gol}-{m.vendeg_gol} ({m.f_haza_gol}-{m.f_vendeg_gol})")

# --------------------------
# 3. feladat
# --------------------------
print("\n3. feladat:")
for m in meccsek:
    # Ha a félidőben a hazai vesztett, de a végeredmény hazai győzelem
    if m.f_haza_gol < m.f_vendeg_gol and m.haza_gol > m.vendeg_gol:
        print(f"{m.fordulo}. forduló: {m.haza_csapat}")
    # Ha a félidőben a vendég vesztett, de a végeredmény vendég győzelem
    elif m.f_vendeg_gol < m.f_haza_gol and m.vendeg_gol > m.haza_gol:
        print(f"{m.fordulo}. forduló: {m.vendeg_csapat}")

# --------------------------
# 4. feladat
# --------------------------
print("4. feladat:")
csapat_nev = input("Adja meg a csapat nevét: ")
if not csapat_nev.strip():
    csapat_nev = "Lelkesek"  # alapértelmezett csapat, ha nem adott meg nevet

# --------------------------
# 5. feladat
# --------------------------
print("5. feladat:")
lott_gol = 0
kapott_gol = 0

for m in meccsek:
    if m.haza_csapat == csapat_nev:
        lott_gol += m.haza_gol
        kapott_gol += m.vendeg_gol
    elif m.vendeg_csapat == csapat_nev:
        lott_gol += m.vendeg_gol
        kapott_gol += m.haza_gol

print(f"lőtt: {lott_gol} kapott: {kapott_gol}")

# --------------------------
# 6. feladat
# --------------------------
print("6. feladat:")

elso_vereseg = None

for m in meccsek:
    if m.haza_csapat == csapat_nev:
        if m.haza_gol < m.vendeg_gol:  # hazai vereség
            elso_vereseg = m
            break  # első vereség megtalálva, kilépünk

if elso_vereseg:
    print(f"Első hazai vereség: {elso_vereseg.fordulo}. forduló, ellenfél: {elso_vereseg.vendeg_csapat}")
else:
    print("A csapat otthon veretlen maradt.")

# --------------------------
# 7. feladat
# --------------------------
print("7. feladat:\nMegtörtént a fájlbaírás")

eredmeny_statisztika = {}

for m in meccsek:
    # mindig a nagyobb szám előre
    gol1, gol2 = max(m.haza_gol, m.vendeg_gol), min(m.haza_gol, m.vendeg_gol)
    key = f"{gol1}-{gol2}"
    eredmeny_statisztika[key] = eredmeny_statisztika.get(key, 0) + 1

# fájlba írás
with open("stat.txt", "w", encoding="utf-8") as f:
    for eredmeny, darab in sorted(eredmeny_statisztika.items(), key=lambda x: (-x[1], x[0])):
        f.write(f"{eredmeny}: {darab} darab\n")
