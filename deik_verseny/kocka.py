lista = []
db = 0
while db != 3:
    lista.append(input())
    db += 1


def y_tengelyes_parhuzamossag(lista):
    a = lista[0]
    b = lista[1]
    c = lista[2]
    return a[2] == c[0] and a[1] == c[1] and a[0] == c[2] and b == b[::-1] and b!="ooo"


def o_szam(lista):
    szum = 0
    for i in lista:
        szum += i.count("o")
    return szum


if y_tengelyes_parhuzamossag(lista) and o_szam(lista) != 0:
    print(o_szam(lista))
else:
    print("unknown")
