def fuggveny(minimum_lada, ladaszam):
    if minimum_lada > ladaszam:
        return "impossible"
    elif minimum_lada == int(minimum_lada):
        return int(minimum_lada)
    else:
        return int(minimum_lada) + 1


bekert_szam = int(input())
db = 0
while bekert_szam != db:
    sor1 = input().split()
    lada_teherbiras = int(sor1[0])
    ladaszam = int(sor1[1])
    almafaszam = int(sor1[2])

    almafa = list(map(int, input().strip().split()))
    osszeg = sum(almafa)
    minimum_lada = osszeg / lada_teherbiras
    print(fuggveny(minimum_lada,ladaszam))
    db += 1

