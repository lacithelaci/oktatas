"""
A math modul biztosít számos matematikai műveletet és konstansokat,
például abszolút érték kiszámítása (fabs), felkerekítés (ceil), lefelé kerekítés (floor),
truncálás (trunc), maradék kiszámítása (fmod), szám normálalakba hozása (frexp),
NaN (Not a Number) érték kezelése (nan), NaN ellenőrzése (isnan), gyökvonás (sqrt),
egész gyökvonás (isqrt), hatványozás (pow), pi érték (pi). A datetime modul lehetővé
teszi az idővel kapcsolatos műveleteket, például az aktuális idő lekérdezése (now),
időformátumok kezelése (strftime), hét napjának lekérdezése (weekday). A random modul funkciói
közé tartozik a véletlenszerű számok generálása adott tartományban (randrange, randint, random),
lista elemeinek véletlenszerű megkeverése (shuffle), elem véletlenszerű kiválasztása (choice),
mintavételezés (sample). Ezeket a modulokat használva bonyolultabb számítási feladatokat
lehet megoldani a Python programozási nyelvben.
"""
import math
import datetime
import random
# Abszolút érték számítása
abs_value = math.fabs(-4.5)
print("Abszolút érték:", abs_value)

# Felkerekítés és lefelé kerekítés
ceil_value = math.ceil(3.7)
floor_value = math.floor(3.7)
print("Felfelé kerekítve:", ceil_value)
print("Lefelé kerekítve:", floor_value)

# Gyökvonás
sqrt_value = math.sqrt(25)
print("Gyökvonás eredménye:", sqrt_value)

# Pi érték
pi_value = math.pi
print("Pi értéke:", pi_value)

# Truncálás
truncated_value = math.trunc(4.9)
print("Truncált érték:", truncated_value)

# Maradék kiszámítása (fmod)
remainder = math.fmod(10, 3)
print("10 maradéka 3-mal osztva:", remainder)

# Szám normálalakba hozása (frexp)
"""
Mantissza: Ez a szám része, ami kicsi és az egység felé közelít. Ez egy valós szám lesz 0 és 1 között, ami fontos része a kiinduló számnak.
Exponens: Ez az egész szám része, ami megmondja, hogy hányszor kell 2-t emelni hatványra, hogy megkapjuk a kiinduló számot.
A mantissza lesz valami közel 0.625, ami a 10.0-hez tartozó kicsi rész.
Az exponens pedig 4, mert ha a 0.625-t megszorozzuk 2-vel négy alkalommal, megkapjuk a kiinduló 10.0-t.
szam = mantisz * 2**exponens
"""
mantissa, exponent = math.frexp(10.0)
print("Mantisza:", mantissa)
print("Exponens:", exponent)

# NaN (Not a Number) kezelése és ellenőrzése
nan_value = math.nan
print("NaN érték:", nan_value)
is_nan = math.isnan(nan_value)
print("NaN-e az érték:", is_nan)

# Hatványozás
power_value = math.pow(2, 3)
print("Hatványozás eredménye:", power_value)

# Egész gyökvonás (isqrt)
integer_sqrt = math.isqrt(25)
print("Egész gyökvonás eredménye:", integer_sqrt)

# Aktuális idő lekérdezése
current_time = datetime.datetime.now()
print("Aktuális idő:", current_time)

# Időformátum kezelése
formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
print("Formázott idő:", formatted_time)

# Hét napjának lekérdezése (0: hétfő, 1: kedd, ..., 6: vasárnap)
weekday = current_time.weekday()
print("A mai nap sorszáma a héten:", weekday)

# Véletlenszerű szám generálása
random_number = random.randint(1, 100)
print("Véletlenszerű szám 1 és 100 között:", random_number)

# Lista elemeinek megkeverése
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)
print("Megkevert lista:", my_list)

# Elem véletlenszerű kiválasztása
random_choice = random.choice(my_list)
print("Véletlenszerűen kiválasztott elem:", random_choice)

# Mintavételezés
sampled_elements = random.sample(range(1, 100), 5)
print("Mintavételezett elemek:", sampled_elements)

# Véletlenszerű szám generálása adott tartományban (randrange)
random_number_range = random.randrange(10, 20)  # 10 és 20 közötti véletlen szám generálása
print("Véletlenszerű szám 10 és 20 között:", random_number_range)

# Véletlenszerű egész szám generálása adott tartományban (randint)
random_integer = random.randint(1, 100)  # 1 és 100 közötti véletlen egész szám generálása
print("Véletlenszerű egész szám 1 és 100 között:", random_integer)

# Véletlenszerű lebegőpontos szám generálása 0 és 1 között (random)
random_float = random.random()  # 0 és 1 közötti véletlen lebegőpontos szám generálása
print("Véletlenszerű lebegőpontos szám 0 és 1 között:", random_float)
