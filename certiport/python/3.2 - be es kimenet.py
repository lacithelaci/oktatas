"""
Ebben a részben olyan kódrészleteket vizsgálunk és készítünk,
 amelyek konzolbemeneti és -kimeneti műveleteket végeznek Pythonban.
 Ennek része a konzolról történő bemenet beolvasása, és a formázott szövegek kiírása,
 amelyek lehetnek a string.format() metódus vagy az f-String használatával formázottak.
 Emellett a parancssori argumentumok használata is ide tartozik,
 amelyek lehetővé teszik a programnak az induláskor átadott paraméterek feldolgozását.
"""
# Konzolbemenet olvasása és kimenetre írása
name = input("Kérem, adja meg a nevét: ")
age = int(input("Kérem, adja meg az életkorát: "))

print(f"Az Ön neve: {name}, és az életkora: {age}")

# String formázás string.format() metódussal
quantity = 3
itemno = 567
price = 49.95

print("Mennyiség: {0}, Tételszám: {1}, Ár: {2}".format(quantity, itemno, price))

# F-string használata
print(f"Mennyiség: {quantity}, Tételszám: {itemno}, Ár: {price}")

# Parancssori argumentumok használata
import sys

print("Parancssori argumentumok:")
for arg in sys.argv:
    print(arg)
#argomentum típusai

#1. Kötelező argumentumok:
if len(sys.argv) != 2:
    print("Használat: python program.py <név>")
    sys.exit(1)

nev = sys.argv[1]
print(f"Hello, {nev}!")
#2. Opcionális argumentumok:
default_name = "Vendég"

if len(sys.argv) == 2:
    name = sys.argv[1]
else:
    name = default_name

print(f"Hello, {name}!")
#3. Kapcsolók vagy opciók:
if "--help" in sys.argv or "-h" in sys.argv:
    print("Ez egy egyszerű program.")
    print("Használat: python program.py --help vagy -h megjeleníti ezt az üzenetet.")
    sys.exit(0)

print("Futtatás normál módban.")
#4. Pozícionális argumentumok:
for idx, arg in enumerate(sys.argv):
    print(f"Pozíció {idx}: {arg}")
#5. Értékadásos argumentumok:
args = {}

for arg in sys.argv[1:]:
    key, value = arg.split('=')
    args[key] = value

print("Értékadásos argumentumok:")
print(args)

