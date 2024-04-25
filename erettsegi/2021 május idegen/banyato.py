f=open("melyseg.txt")
sor=f.readline()
oszlop=f.readline()
lista=[]
for i in f:
    i=i.strip().split(" ")
    lista.append(i)
print("2. feladat ")
sora=12
oszlopa=6
print(f"A mért mélység az adott helyen {lista[sora - 1][oszlopa - 1]} dm")
print(f"3. feladat ")
szum=0
db=0
def kerekito(a):
    a=a/10
    b=round(a)
    return b
for i in lista:
    for j in i:
        if int(j)!=0:
            szum+=int(j)
            db+=1
print(f"A tó felszíne: {db} m2, átlagos mélysége: {(szum/db/10):.2f} m ")
print("4.feladat")
max=int(lista[0][0])
for i in lista:
    for j in i:
        if max<int(j):
            max=int(j)
print(f"A tó legnagyobb mélysége: {max} dm ")
print("A legmélyebb helyek sor-oszlop koordinátái: ")
for oszlop,i in enumerate(lista):
    for sor,j in enumerate(i):
        if int(j)==max:
            print(f"({oszlop+1}; {sor+1})",end=" ")
print("\n5. feladat")
print('5. feladat')
hossz = 0
for i, sor in enumerate(lista):
    for j, melyseg in enumerate(sor):
       if int(melyseg) > 0:
            if int(sor[j-1]) == 0:
                hossz += 1
            if int(sor[j+1]) == 0:
                hossz += 1
            if int(lista[i-1][j]) == 0:
                hossz += 1
            if int(lista[i+1][j]) == 0:
                hossz += 1
print(f'A tó partvonala {hossz} m hosszú')
print("6. feladat")
oszlop=6
lista2=[]
for index,i in enumerate(lista):
    for index2, y in enumerate(i):
        if index2+1==oszlop:
            lista2.append(y)
csillag="*"
xd=open("diagram.txt","w")
for index,i in enumerate(lista2):
    xd.write(f"{(index+1):02d} {csillag*kerekito(int(i))}\n")
