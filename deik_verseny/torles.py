def torolt_szavak(szoveg, lista):
    while True:
        min_index = float('inf')
        torlendo_szo = None
        for szo in lista:
            index = szoveg.find(szo)
            if index != -1 and index < min_index:
                min_index = index
                torlendo_szo = szo
        if torlendo_szo is None:
            break
        szoveg = szoveg[:min_index] + szoveg[min_index + len(torlendo_szo):]
    return szoveg


szoveg = input()
lista = input().split()
print(len(torolt_szavak(szoveg, lista)), torolt_szavak(szoveg, lista))
