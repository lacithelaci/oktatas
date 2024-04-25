def osztok(a):
    paros = sum(1 for i in range(1, a + 1) if a % i == 0 and i % 2 == 0)
    paratla = sum(1 for i in range(1, a + 1) if a % i == 0 and i % 2 == 1)

    if paros == paratla:
        return 0
    elif paros > paratla:
        return 2
    return 1


bekert_szam = int(input())
for _ in range(bekert_szam):
    a = int(input())
    print(osztok(a))