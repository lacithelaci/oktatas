from math import gcd
def lnko(a, b):
    max_lnko = 1
    min_osszeg = float('inf')
    eredmeny = None

    for i in range(a, b):
        for j in range(i + 1, b + 1):
            if gcd(i, j) > max_lnko:
                max_lnko = gcd(i, j)
                eredmeny = (i, j)
                min_osszeg = i + j
            elif gcd(i, j) == max_lnko and i + j < min_osszeg:
                eredmeny = (i, j)
                min_osszeg = i + j

    return eredmeny

a = input()

pair = lnko(int(a.split()[0]), int(a.split()[1]))
print(*pair)
