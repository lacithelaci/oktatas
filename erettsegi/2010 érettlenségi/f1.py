print("1. feladat")
be=input("kérek egy szöveget")
#betuk=set()
#for betu in be:
 #   betuk.add(betu)
betuk={betu for betu in be}
print(*betuk)
print("A betűk száma: ",len(betuk))
f=open("szotar.txt")
lista=[]
print("feladat 3")
for sor in f:
    sor=sor.strip()
    lista.append(sor)
for szo in lista:
    print("".join(sorted(szo)))
for szo in lista:
    s=""
    for betu in sorted(szo):
        s+=betu
    print(s)
print("4. feladat")
asszo=input("Kérek egy szót:")
bsszo=input("Kérek egy szót:")
def anagrama(asszo,bsszo):

    asszo="".join(sorted(asszo))
    bsszo="".join(sorted(bsszo))
    if asszo==bsszo:
        return "Anagramma"
    else:
        return "Nem anagramma"


def anagrama2(asszo,bsszo):
    a=True
    asszo="".join(sorted(asszo))
    bsszo="".join(sorted(bsszo))
    if asszo==bsszo:
        return a==True

print(anagrama(asszo,bsszo))
print("5. feladat")
c=input("Kérek egy szót")
lista3=[]
for i in lista:
    if anagrama2(c,i)==True:

        lista3.append(i)
if len(lista3)==0:
    print("Nincs anagramma")
else:
    print("Anagrammák:",*lista3)
asd=len(lista[0])
for i in lista:
    if asd<=len(i):
        asd=len(i)
print("feladat 6.")
print("A leghosszabb szavak")
for i in lista:
    if asd==len(i):
        print(f"{i}")
a=open("rendezett.txt","w",encoding="UTF-8")
print("feladat 7")
for i in sorted(lista,key=lambda i:len(i)):
    a.write(f"{i}\n")

