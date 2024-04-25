elso_sor = int(input())
tobbi_adat = list(map(int, input().strip().split()))
max_szorzat = 0
for i in range(len(tobbi_adat)):
    jelenlegi_min = tobbi_adat[i]
    for j in range(i, len(tobbi_adat)):
        jelenlegi_min = min(jelenlegi_min, tobbi_adat[j])
        max_szorzat = max(max_szorzat, jelenlegi_min * (j - i + 1))

print(max_szorzat)