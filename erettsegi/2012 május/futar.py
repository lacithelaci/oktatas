class Futar:
    def __init__(self,napszam,fuvarszam,km):
        self.napszam = int(napszam)
        self.fuvarszam = int(fuvarszam)
        self.km = int(km)
    def __repr__(self):
        return f"{self.napszam} {self.fuvarszam} {self.km}"
lista=[]
f=open("tavok.txt")
for i in f:
    i=i.strip().split()
    lista.append(Futar(*i))
lista=sorted(lista,key= lambda i:(i.napszam,i.fuvarszam))
print(f"2. feladat\n{lista[0].km} km volt a hét legelső útja kilométerben!\n3.feladat")
print(f"{lista[-1].km} km volt a hét utolsó útja kilométerben!")
print("4. feladat")
napok=set()
napok2=set()
for i in range(1,8):
    napok.add(i)
for i in lista:
    napok2.add(i.napszam)
print("A futár ezeken a napokon nem dolgozott:",end=" ")
print(*napok.difference(napok2))
print("5. feladat")
szotar={}
for i in lista:
    szotar[i.napszam]=szotar.get(i.napszam,0)+1
a=max(szotar.values())
for index,i in szotar.items():
    if a==i:
        print(f"{index}. napon volt a legtöbb fuvar\n6. feladat")
        break
szotar={}
lista3=[]
for i in lista:
    szotar[i.napszam] = szotar.get(i.napszam, 0) + i.km
for i,index in szotar.items():
    lista3.append(f"{i}. nap: {index} km")
a=napok.difference(szotar)
for i in a:
    lista3.append(f"{i}. nap: 0 km")
for i in sorted(lista3):
    print(i)
print("7. feladat")
def fizu(a):
    fiz=0
    if a<=2:
        fiz=f"500 Ft"
    elif a<=5:
        fiz = f"700 Ft"
    elif a <= 10:
        fiz = f"900 Ft"
    elif a <= 20:
        fiz = f"1 400 Ft"
    elif a <= 30:
        fiz = f"2 000 Ft"
    return fiz
def fizu2(a):
    fiz=0
    if a<=2:
        fiz=500
    elif a<=5:
        fiz = 700
    elif a <= 10:
        fiz = 900
    elif a <= 20:
        fiz = 1400
    elif a <= 30:
        fiz = 2000
    return fiz
a=int(input("Kérek egy km-et"))
print(f"{fizu(a)}")
print("8. feladat\nA fájl kész")
f=open("dijazas.txt","w",encoding="UTF-8")
for i in lista:
    f.write(f"{i.napszam}. nap {i.fuvarszam}. út: {fizu(i.km)}\n")
db=0
for i in lista:
    db+=fizu2(i.km)
print(f"{(db)} forintot kap a heti munkájáért! ")