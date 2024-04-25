def van_osztoja(szam, lista):
    for i in lista:
        if i != szam and szam % i == 0:
            return True
    return False


def maximalis_csokis_szam(n, lista):
    csoki_db = 0
    for i in range(n):
        if van_osztoja(lista[i], lista[:i] + lista[i + 1:]):
            csoki_db += 1

    return csoki_db


n = int(input())
x = list(map(int, input().split()))
max_csoki = maximalis_csokis_szam(n, x)
print(max_csoki)
