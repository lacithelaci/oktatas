def kut(lista):
    kut_magassaga = lista[0]
    elso_nap = lista[1]
    visszacsuszas = lista[2]
    szazalek = lista[3]
    szum = 0
    hozzaadando = elso_nap
    nap = 0
    kivonando = szazalek / 100 * elso_nap
    while True:
        nap += 1
        szum += hozzaadando
        hozzaadando -= kivonando
        if szum > kut_magassaga:
            return f"success on day {nap}"
        szum -= visszacsuszas
        if szum < 0:
            return f"failure on day {nap}"


while True:
    lista = list(map(int, input().split()))
    if lista[0] == 0:
        break
    else:
        print(kut(lista))
