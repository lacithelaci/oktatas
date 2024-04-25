elso_sor = int(input())
lista = []
db=0
while db!=int(elso_sor):

    lista.append(int(input()))
    db+=1
osszes_lap = 52
kulonbseg = 21 - sum(lista)
kedvezo_huzhato_lapok = kulonbseg * 4
for i in lista:
    if i <= kulonbseg:
        kedvezo_huzhato_lapok -= 1
if osszes_lap - kedvezo_huzhato_lapok - len(lista) >= kedvezo_huzhato_lapok:
    print("STOP")
else:
    print(f"DRAW")
