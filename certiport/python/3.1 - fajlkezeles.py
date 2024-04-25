"""
Ez a rész arról szól, hogy hogyan hozhatunk létre és
vizsgálhatunk kódrészleteket fájlbeviteli és -kiviteli műveletek végrehajtására Pythonban.
A fájlkezeléshez szükséges funkciók között szerepelnek az open, close, read, write, append funkciók,
melyek segítségével fájlokat lehet megnyitni, zárni, olvasni, írni, adatokat hozzáfűzni,
illetve az adatok létezését ellenőrizni és törölni. Emellett a with utasítás is fontos,
ami a fájlok automatikus zárását és erőforráskezelést segíti elő.
"""
# Fájl létrehozása és írása
with open('teszt.txt', 'w') as file:
    file.write('Ez egy teszt szöveg.\nMásodik sor.')

# Fájl beolvasása és kiíratása a képernyőre
with open('teszt.txt', 'r') as file:
    contents = file.read()
    print("Fájl tartalma:")
    print(contents)

# Fájlhoz adat hozzáfűzése
with open('teszt.txt', 'a') as file:
    file.write('\nHarmadik sor hozzáadva.')

# Újra beolvasás és kiíratás a frissített tartalommal
with open('teszt.txt', 'r') as file:
    updated_contents = file.read()
    print("\nFrissített fájl tartalma:")
    print(updated_contents)
