lista = ["alm*sam*", "*lmasa*a"]
c = ""
d = ""
for y in range(8):
    d = ""
    for i in lista:

        if i[y] != "*":
            d = i[y]
    c += d
print(c)
