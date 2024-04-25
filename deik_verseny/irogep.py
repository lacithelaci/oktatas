def karakter(a):
    if a == "sp":
        return " "
    if a == "bS":
        a = "\ "
        return a[0]
    if a == "sQ":
        return "'"
    return a


def szamtalo(szo):
    index = -1
    for i in range(0, len(szo)):
        if szo[i].isdigit():
            index = int(i)
    return index


lista=input().split()
szo = ""
index=None
for i in lista:
    if i == "nl":
        szo += "\n"
    else:
        index=szamtalo(i)
        szo+=int(i[0:index+1]) * karakter(i[index+1:])
print(szo)