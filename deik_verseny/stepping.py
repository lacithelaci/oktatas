def lepcsos(a):
    a = str(a)
    if int(a) < 10:
        return True
    for i in range(0, len(a) - 1):

        if int(a[i]) + 1 == int(a[i + 1]) or int(a[i]) - 1 == int(a[i + 1]):
            pass
        else:
            return False
    return True


lista = []
a = input()
for i in range(int(a.split()[0]), int(a.split()[1]) + 1):
    if lepcsos(i):
        lista.append(i)
print(lista)
