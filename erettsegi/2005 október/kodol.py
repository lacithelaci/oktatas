import math


def szo(a):
    a = a.replace("á", "a")
    a = a.replace("é", "e")
    a = a.replace("í", "i")
    a = a.replace("ü", "u")
    a = a.replace("ű", "u")
    a = a.replace("ó", "o")
    a = a.replace("ö", "o")
    a = a.replace("ő", "o")
    f = "QWERTZUIOPLKJHGFDSAYXCVBNM"
    a = a.upper()
    ujra = ""
    for i in a:
        if i in f:
            ujra += i
        else:
            ujra += ""

    return ujra


print("3. feladat")
a = "Ez a próba szöveg, amit kódolunk!"
print(szo(a))
a = szo(a)
print("5. feladat")
auto = "auto"
auto = auto.upper()
hossz = len(szo(a)) / len(auto)
hossz = math.ceil(hossz)
megoldas = auto * 7
megoldas = megoldas[0:len(szo(a))]
print(megoldas)
vign={}
f=open("Vtabla.dat")
for sor in f:
    kezdokarakter=sor[0]
    sor=sor.strip()
    if kezdokarakter=='A':
        vign['abc']=sor
    if kezdokarakter in megoldas:
        vign[kezdokarakter]=sor
kodolt_uzenet=""
for karakter,kulcs_karakter in zip(a,megoldas):
    oszlop=vign['abc'].index(karakter)
    kodolt_uzenet+=vign[kulcs_karakter][oszlop]
f=open("kodolt.dat","w")
f.write(kodolt_uzenet)
