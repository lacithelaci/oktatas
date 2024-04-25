"""
A kód részeinek elemzése, hibák azonosítása és javítása fontos a szintaxis hibák,
logikai hibák és futási időben jelentkező hibák kezelésében.
"""


# Szintaxis hiba példa
# Hibás írásmód a függvény definíciójában (zárójel lehagyása, kettőspont lehagyása, stb)
def my_function():
    print("Hello World")

# Logikai hiba példa
# Rossz eredmény a logikai összehasonlítás miatt
num1 = 5
num2 = 7
if num1 > num2:
    print("num1 nagyobb")
else:
    print("num2 nagyobb")

# Futási időben fellépő hiba példa
# Nullával való osztás
numerator = 10
denominator = 0
result = numerator / denominator  # Ez futási időben hibát fog eredményezni
print(result)
