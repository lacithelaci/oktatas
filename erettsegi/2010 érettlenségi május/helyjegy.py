#Szemán László
class Busz:
    def __init__(self,ules,kezdet,veg):
        self.ules =int(ules)
        self.kezdet =int(kezdet)
        self.veg = int(veg)
    def __repr__(self):
        return f"{self.ules} {self.kezdet} {self.veg}"
    def kerekites(self):
        a=self.veg-self.kezdet
        teljes = (a+9)//10 * 71
        return (teljes+2)// 5 * 5

        return a
lista=[]
f=open("eladott.txt",encoding="UTF-8")
for i,sor in enumerate(f):
    if i>0:
        sor=sor.strip().split()
        lista.append(Busz(*sor))
print(lista)
lista2=[i.ules for i in lista]
lista3=[i.kezdet for i in lista]
lista4=[i.veg for i in lista]
print("2. feladat")
print(f"A legutolsó jegyvásárlónak az ülésének a száma {lista2[-1]} és az általa beutazott távolság {lista4[-1]-lista3[-1]} km")
print("3. feladat")
lista5=[]
for y,i in enumerate(lista):
    if i.kezdet==0 and i.veg==172:

        print("Vásárlók:",y+1)
for i in lista:
    lista5.append(i.kerekites())
print("4. feladat")
print(f"A jegybevétel: {sum(lista5)} forint")
megallo=[]
for i in lista:
    if i.kezdet not in megallo :
        megallo.append(i.kezdet)
    if i.veg not in megallo :
        megallo.append(i.veg)
megallok=[]
for i in sorted(megallo):
    megallok.append(i)
f=0
l=0
for i in lista:
    if i.kezdet==megallok[-2]:
        f+=1
    if i.veg==megallok[-2]:
        l+=1

print("5. feladat")
print(f"Az utolsó előtti állomáson {f} szálltak fel {l} és szálltak le")
print("6. feladat")
print("Ennyi megálló van:",len(megallo)-2)
