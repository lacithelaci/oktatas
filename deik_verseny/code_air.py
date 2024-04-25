def kiszamito(jegy_alapar, dragulas, db, ablakos_felar, veszkijaratok, veszkijaratos_ar, i):
    osszeg = jegy_alapar + db * dragulas
    if i[-1] in ["A" or "F"]:
        osszeg += ablakos_felar
    if int(i[:-1]) in veszkijaratok:
        osszeg += veszkijaratos_ar
    return osszeg


elso_sor = input().strip().split()
jegy_alapar = int(elso_sor[0])
dragulas = int(elso_sor[1])
ablakos_felar = int(elso_sor[2])
veszkijaratos_ar = int(elso_sor[3])
masodik_sor = input().strip().split()
sorok_szama = int(masodik_sor[0])
veszkijaratszam = int(masodik_sor[1])
veszkijaratok = list(map(int, input().strip().split()))
lista = []
while True:
    try:
        i = input()
        if i == "":
            break
        lista.append(i.strip())
    except EOFError:
        break

db = 0
osszeg = [sum(kiszamito(jegy_alapar, dragulas, index, ablakos_felar, veszkijaratok, veszkijaratos_ar, i) for index, i in
              enumerate(lista))]
print(*osszeg)
for i in lista:
    print(f"{i}: {kiszamito(jegy_alapar, dragulas, db, ablakos_felar, veszkijaratok, veszkijaratos_ar, i)}")
    db += 1
