class Tanc:
    def __init__(self, tanc, lany, fiu):
        self.tanc = tanc
        self.fiu = fiu
        self.lany = lany

    def __repr__(self):
        return f"{self.tanc} {self.fiu} {self.lany}"


f = open("tancrend.txt")
lista = []
for i in f:
    i = i.strip()
    i2 = f.readline().strip()
    i3 = f.readline().strip()
    lista.append(Tanc(i, i2, i3))
tancok = [i.tanc for i in lista]
print(f"2. feladat\nAz első tánc {tancok[0]} volt.\nAz utolsó tánc {tancok[-1]} volt.")
szamba = [i.tanc for i in lista if i.tanc == "samba"]
print(f"3. feladat\n{len(szamba)} pár mutatott be sambát")
vilma = [i.tanc for i in lista if i.lany == "Vilma"]
print("4. feladat\nVilma ezekbe a táncokba szerepelt:")
for i in vilma:
    print(i)
print("5. feladat")
nev = ""
tanc = input("Kérem egy tánc nevét")
for i in lista:
    if i.lany == "Vilma" and i.tanc == tanc:
        nev = i.fiu
if nev != "":
    print(f"A {tanc} bemutatóján Vilma párja {nev} volt.")
else:
    print(f"Vilma nem táncolt {tanc}-t.")
print("6. feladat")
w = open("szereplok.txt", "w", encoding="UTF-8")
fiu = set()
lany = set()
for i in lista:
    fiu.add(i.fiu)
    lany.add(i.lany)
w.write("Lányok: ")
lany = ",".join(lany)
for i in lany:
    w.write(i)
w.write("\nFiúk: ")
fiu = ",".join(fiu)
for i in fiu:
    w.write(i)
print("Kész a file")
fiuk = {}
lany = {}
for i in lista:
    fiuk[i.fiu] = fiuk.get(i.fiu, 0) + 1
    lany[i.lany] = lany.get(i.lany, 0) + 1
max = 0
print("7.feladat\nA legtöbbet táncolt fiúk: ")
for index, i in fiuk.items():
    if max < i:
        max = i
for index, i in fiuk.items():
    if max == i:
        print(index)
max = 0
print("7.A legtöbbet táncolt lányok: ")
for index, i in lany.items():
    if max < i:
        max = i
for index, i in lany.items():
    if max == i:
        print(index)
