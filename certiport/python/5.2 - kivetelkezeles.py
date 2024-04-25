"""
Kódok elemzése és létrehozása, amelyek kezelik a kivételeket különböző kulcsszavakkal,
mint például try, except, else, finally, raise. Ezek a kulcsszavak segítenek a Python programokban
a kivételek kezelésében és azoknak a megfelelő válaszok kiváltásában.
Ez a megközelítés lehetővé teszi a kód futásának biztonságosabbá és megbízhatóbbá tételét,
mivel a kivételek lehetőséget adnak a különleges esetek kezelésére,
így a programok jobban kontrollálhatók és ellenállóbbak lesznek a hibás bemenetekkel
vagy feltételekkel szemben. Az try-except blokkokkal történő kivételek kezelése lehetővé teszi a programok számára,
hogy elegánsan és hatékonyan reagáljanak különböző hibás helyzetekre, és elősegíti a kód stabilitását és megbízhatóságát.
"""

# Kivételek kezelése példa
try:
    num1 = int(input("Adj meg egy számot: "))
    num2 = int(input("Adj meg még egy számot: "))
    result = num1 / num2
    print("Az osztás eredménye:", result)
except ValueError:
    print("Hiba: Érvénytelen érték! Csak számokat adj meg.")
except ZeroDivisionError:
    print("Hiba: Nullával nem lehet osztani.")
else:
    print("Nincs kivétel.")
finally:
    print("Vége a kivételek kezelésének.")


# Kivétel explicit kiváltása ('raise') példa
def check_age(age):
    if age < 0:
        raise ValueError("Az életkor nem lehet negatív szám.")
    elif age < 18:
        print("Kiskorú vagy.")
    else:
        print("Felnőtt vagy.")


try:
    check_age(-5)
except ValueError as ve:
    print(ve)
