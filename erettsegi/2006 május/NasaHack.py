db = 0
tizk = 10000
db2 = 0
while db != 1000000:
    db += 1
    if db % 10000 == 0:
        tizk += 10000
        db2 += 1
    print(f"Nasa hackelésének előrehaladása: {db2}%")
print("Kész")
