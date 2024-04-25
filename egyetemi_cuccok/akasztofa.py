import random


def benne_van(kitalalando_szo: str, betu: str):
    ures = ""
    for i in range(0, len(kitalalando_szo)):
        if kitalalando_szo[i] == betu:
            ures += betu
        else:
            ures += "_"
    return ures


def atiro(jelenlegi_allas, betukeres_utani_allas):
    ures = ""
    for i in range(0, len(jelenlegi_allas)):
        if jelenlegi_allas[i] != "_":
            ures += jelenlegi_allas[i]
        elif jelenlegi_allas[i] == "_" and betukeres_utani_allas[i] != "_":
            ures += betukeres_utani_allas[i]
        else:
            ures += "_"
    return ures


lista = []
f = open("szavak.txt", encoding="UTF-8")
for i in f:
    i = i.strip()
    lista.append(i)

db = 1
kitalalando_szo = random.choice(lista)
allas = "_" * len(kitalalando_szo)
eddig_használt_betűk = []
print("A szó hossza: ", len(kitalalando_szo))
while True:
    print("Jelenlegi próbálkozás:", db)
    bekert_betu = input("Kérek egy betűt: ")
    if len(bekert_betu) == 1:
        minta = benne_van(kitalalando_szo, bekert_betu)
        allas = atiro(minta, allas)
        db += 1
        print(allas)
    elif len(bekert_betu) == len(kitalalando_szo) and bekert_betu == kitalalando_szo:
        print("Nyertél, Ennyi próbálkozásból:", db)
        break
    elif len(bekert_betu) == len(kitalalando_szo) and bekert_betu != kitalalando_szo:
        print("Vesztettél")
        print("Ez a szó volt", kitalalando_szo)
        break
    else:
        print("Hiba, nem karaktert adtál meg! Büntetés: -1 kitalálás")
        db += 1
    if kitalalando_szo == allas:
        print("Nyertél")
        break
    if db == len(kitalalando_szo) + 1:
        print("Vesztettél!")
        print("Ez a szó volt", kitalalando_szo)
        break
    eddig_használt_betűk.append(bekert_betu)
    print("Eddig felhasznált betűk:", *eddig_használt_betűk)
