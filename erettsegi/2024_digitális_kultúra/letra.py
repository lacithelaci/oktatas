lista = [3, 1, 1, 2, 1, 5, 5, 4, 4, 4, 1, 2, 3, 6, 4, 6, 1, 4]
print("2. feladat")
db = 0
allas = 0
for i in lista:
    allas += i
    if allas % 10 == 0:
        allas -= 3
        db += 1
    print(allas, end=" ")
print(f"\n3. feladat\nA játék során {db} alkalommal lépett létrára.")
if allas >= 45:
    print("4.feladat\nA játékot befejezte")
else:
    print("4.feladat\nA játékot abbahagyta")
