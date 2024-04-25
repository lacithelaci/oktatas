def elosztas(N, M, penzek):
    penzek.sort()
    osszeg = sum(penzek)
    if osszeg < M or penzek[0] > M:
        return "IMPOSSIBLE"

    eloszthato = [0] * N
    maradek = M

    for i in range(N):
        eloszthato[i] = min(penzek[i], maradek // (N - i))
        maradek -= eloszthato[i]

    return eloszthato

# Bemenet beolvasása
N = int(input())
M = int(input())
penzek = []
for _ in range(N):
    penzek.append(int(input()))

# Eredmény kiíratása
eredmeny = elosztas(N, M, penzek)
if eredmeny == "IMPOSSIBLE":
    print(eredmeny)
else:
    for penz in eredmeny:
        print(penz)