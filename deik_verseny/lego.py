lista = []
while True:
    i = input().split()
    if i == []:
        break
    lista.append(i)

lista2 = []
while True:
    try:
        i = input().split()
        if i == []:
            break
        lista2.append(i)
    except EOFError:
        break


lehetseges = True
lista3 = []
for i in sorted(lista):
    osszeg = 0
    for y in lista2:
        if i[0] == y[0] and i[1] == y[1]:
            osszeg += int(y[2])
    if osszeg < int(i[2]):
        lehetseges = False
    lista3.append(f"{i[0]} {i[1]}: {osszeg}/{i[2]}")
if lehetseges:
    print("Can be built")
else:
    print("Cannot be built")
for i in lista3:
    print(i)
