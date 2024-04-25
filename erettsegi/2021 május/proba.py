lista = [1, 2, 3, 5, 3, 12, 3, 2, 1]
lista2 = []
elozo = 0
valtozas = False
lehet=True
elso = 0
masodik = 0
harmadik = 0
for i in lista:
    if i > elozo:
        elso = 1
    else:
        masodik = 1
        valtozas=True
    if valtozas and i>elozo:
        harmadik=1
    if i==elozo:
        lehet=False
    elozo=i
ossz=elso+masodik+harmadik
if lehet and ossz==2:
    print("Folyamatosan mélyül")
else:
    print("Nem mélyül folyamatosan")