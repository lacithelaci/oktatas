f=open("lottosz.dat")
lista=[]
for i in f:
    i=i.strip().split()
    lista.append(i)
print("1. feladat\nKérje be az 52. heti lottószámokat")
db=0
lista2=[]
while db!=5:
    a=int(input("Kérem az 52. heti lottószámokat"))
    a=str(a)
    lista2.append(a)
    db+=1
lista2=sorted(lista2)
print("2. feladat")
print(*lista2)
print("3. feladat")
het=int(input("Kérjen be egy számot"))
print("4. feladat")
for index,i in enumerate(lista):
    if index+1==het:
        for y in i:
            print(f"{y}",end=" ")
halmaz=set()
for i in lista:
    for y in i:
        halmaz.add(y)
print("\n5. feladat")
if len(halmaz)==90:
    print("Van")
else:
    print("Nincs")
print("6. feladat")
paratlan=0
for i in lista:
    for y in i:
        if int(y)%2==1:
            paratlan+=1
print("Páratlanok száma:",paratlan)
print("7. feladat")
print("A kiírás és a hozzáfűzés megtörtént")
lista.append(lista2)
ki=open("lotto52.ki.txt","w",encoding="UTF-8")
db=0
for i in lista:
    for y in i:
        db+=1
        ki.write(f"{y} ")
        if db%5==0:
            ki.write("\n")
szotar={}
szotar2={}
for i in lista:
    for y in i:
        y=int(y)
        szotar[y]=szotar.get(y,0)+1
for i in sorted(szotar):
    szotar2[i]=szotar[i]
db=1
print("8. feladat")
for i in szotar2.values():

    print(i,end=" ")
    if db % 15 == 0:
        print()
    db+=1
print("\n9. feladat ")
prim={"2", "3", "5", "7", "11", "13", "17", "19", "23", "29", "31", "37", "41", "43", "47", "53", "59", "61", "67", "71","73", "79", "83", "89"}
primek2= {""}
def prime(a):
    db=0
    for i in range(1,a+1):
        if a%i==0:
            db+=1
    return db==2
for i in lista:
    for y in i:
        if prime(int(y)):
            primek2.add(y)
primek3=prim.difference(primek2)
print("Nem húzták ki: ")
for i in primek3:
    print(i)