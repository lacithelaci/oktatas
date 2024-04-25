"""
Hozzárendelési operátorok (=, +=, -= stb.): Ezekkel az operátorokkal értékeket rendelünk hozzá változókhoz vagy változtatjuk meg a változó értékét.
Összehasonlító operátorok (==, >=, <=, != stb.): Ezek az operátorok két értéket hasonlítanak össze, és igaz vagy hamis értéket adnak eredményül.
Logikai operátorok (and, or, not): Ezek az operátorok logikai műveleteket hajtanak végre az értékeken.
Aritmetikai és egyéb operátorok (+, -, /, //, %, **, egyedi + és -):
Ezek az operátorok aritmetikai műveleteket végeznek (összeadás, kivonás, szorzás, stb.),
valamint egyéb speciális műveleteket hajtanak végre.
Azonosító operátor (is): Ez az operátor ellenőrzi, hogy két változó azonos objektumra mutat-e a memóriában.
Tartalmazási operátor (in): Ez az operátor azt ellenőrzi, hogy egy adott elem benne van-e egy adatszerkezetben vagy nem.
"""
# Hozzárendelési operátorok
x = 5
y = 3
z = x + y
print("Hozzárendelési operátorok:", z)  # Az 'x + y' eredménye az 'z' változóba lesz hozzárendelve

# Összehasonlító operátorok
a = 10
b = 15
result = a > b
print("Összehasonlító operátorok:", result)  # Az 'a > b' eredményét írja ki, ami hamis lesz (False)

# Logikai operátorok
c = True
d = False
result = c and d
print("Logikai operátorok:", result)  # Az 'and' művelet True és False között hamis (False)

# Aritmetikai és egyéb operátorok
number = 10 + 5 * 2
print("Aritmetikai operátorok:", number)  # A szorzás precedenciája magasabb, tehát 5*2 lesz először végrehajtva

# Azonosító operátor
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
result = list1 is list2
print("Azonosító operátor:", result)  # Két különböző objektumra mutatnak, így az 'is' operátor hamis (False)
print("Azonosító operátor:", list1 is list3)  # Azonos objektumra mutatnak, így az 'is' operátor igaz (True)
# Tartalmazási operátor
numbers = [1, 2, 3, 4, 5]
result = 3 in numbers
print("Tartalmazási operátor:", result)  # A 'numbers' listában benne van a 3, ezért az 'in' operátor igaz (True)
