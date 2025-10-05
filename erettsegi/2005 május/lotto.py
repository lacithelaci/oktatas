# 1-2. feladat: Kérje be az 52. hét lottószámait és rendezze őket

print("Kérem adja meg az 52. hét öt lottószámát, szóközzel elválasztva:")
user_input = input()
week_52_numbers = list(map(int, user_input.split()))

if len(week_52_numbers) != 5:
    print("\nHiba: pontosan 5 számot kell megadni!")
else:
    # 2. feladat: számok rendezése emelkedő sorrendbe
    week_52_numbers.sort()
    print("\nAz 52. hét lottószámai (rendezett sorrendben):", week_52_numbers)

# 3. feladat: Kérjen be egy számot 1-51 között
week_number = int(input("Adjon meg egy számot 1 és 51 között: "))

# 4. feladat: A megfelelő hét lottószámainak kiírása az állományból
# Lottószámok beolvasása és egyből listába alakítása
lotto_weeks = []
with open("lottosz.dat", "r") as file:
    for line in file:
        # Sorból számok listája, és hozzáadás a heti adatok listájához
        lotto_weeks.append(list(map(int, line.split())))

# Kiválasztott hét lottószámai
selected_week_numbers = lotto_weeks[week_number - 1]  # mivel a lista 0-tól indexel
print(f"\nA {week_number}. hét lottószámai:", selected_week_numbers)

# 5. feladat: Van-e olyan szám, amit egyszer sem húztak ki az 51 hét alatt?
all_numbers = set(range(1, 91))  # lehetséges számok 1-90
drawn_numbers = set()  # a kihúzott számok halmaza

for week in lotto_weeks:
    drawn_numbers.update(week)  # hozzáadjuk a heti számokat

# Ellenőrzés
if all_numbers - drawn_numbers:
    print("\nVan olyan szám, amit egyszer sem húztak ki az 51 hét alatt.")
else:
    print("\nNincs olyan szám, amit egyszer sem húztak ki az 51 hét alatt.")

# 6. feladat: Hányszor volt páratlan szám a kihúzott lottószámok között?
odd_count = 0
for week in lotto_weeks:
    odd_count += sum(1 for number in week if number % 2 == 1)

print("\nA páratlan számok összesen", odd_count, "alkalommal szerepeltek az 51 hét alatt.")

# 7. feladat
# 52. hét hozzáfűzése a listához
lotto_weeks.append(week_52_numbers)

# 8. feladat: Kiírás a lotto52.ki fájlba
with open("lotto52.ki", "w") as file:
    for week in lotto_weeks:
        line = " ".join(map(str, week))  # számok szóközzel elválasztva
        file.write(line + "\n")

print("\nAz összes lottószám sikeresen kiírva a 'lotto52.ki' fájlba.")

# Számok előfordulásának számlálása 1–90
count_numbers = [0] * 90  # index 0 -> 1-es szám, index 89 -> 90-es szám

# Lotto52 fájl beolvasása
with open("lotto52.ki", "r") as file:
    for line in file:
        numbers = list(map(int, line.split()))
        for num in numbers:
            count_numbers[num - 1] += 1  # indexelés: 1 -> 0

# Eredmény kiírása 6 sorban, soronként 15 értékkel
for i in range(6):
    row = count_numbers[i * 15: (i + 1) * 15]
    print(" ".join(map(str, row)))

# 9. feladat: A prímszámok listája 1-90 között
primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89]

# Kiírjuk, mely prímszámokat nem húzták ki
not_drawn_primes = [p for p in primes if count_numbers[p - 1] == 0]

if not_drawn_primes:
    print("\nAz alábbi prímszámokat nem húzták ki az év során:", *not_drawn_primes)
else:
    print("\nMinden prímszámot legalább egyszer kihúztak az év során.")
