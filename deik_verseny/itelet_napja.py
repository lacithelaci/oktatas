napok = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
honapok = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
adatok_szama = int(input())
db = 0
while True:
    if db == adatok_szama:
        break
    adatok = input().split()
    bekert_ho = int(adatok[0])
    bekert_nap = int(adatok[1])
    osszeg = (sum(honapok[0:bekert_ho - 1]) + bekert_nap) % 7
    print(napok[osszeg])
    db += 1