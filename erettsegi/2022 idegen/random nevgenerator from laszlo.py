import random

knev = ["Laci", "Imre", "Ákos", "Alekosz"]
vnev = ["Lakatos", "Fehér", "Fekete", "Barna"]
db = 0
while db != 10:
    db += 1
    a = random.randint(0, len(knev)-1)
    b = random.randint(0, len(vnev)-1)
    print(f"{vnev[b]} {knev[a]}")
