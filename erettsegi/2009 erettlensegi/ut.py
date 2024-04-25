class Jarmu:
    def __init__(self,ora,perc,mp,ido,varos):
        self.ora =int( ora)
        self.perc =int( perc)
        self.mp =int( mp)
        self.ido =int( ido)
        self.varos = varos
    def __repr__(self):
        return f"{self.ora} {self.perc} {self.mp} {self.ido} {self.varos} {self.sebesseg()}"
    def halad(self):
        if self.varos=="A":
            return "F"
        else:
            return "A"
    def masodperc(self):
        return self.ora*60*60+self.perc*60+self.mp
    def sebesseg(self):
        return 1000/self.ido
    def var(self):
        if self.varos=="A":
            return "Also"
        else:
            return "Felso"
    def osszido(self):
        return self.ora * 60 * 60 + self.perc * 60 + self.mp+self.ido
    def valami(self):
        seconds=self.ora * 60 * 60 + self.perc * 60 + self.mp+self.ido
        seconds = seconds % (24 * 3600)
        hour = seconds // 3600
        seconds %= 3600
        minutes = seconds // 60
        seconds %= 60
        return f"{hour:02d}:{minutes:02d}:{seconds:02d}"
def vissza(mp):
    o = mp //3600
    marad= mp%3600
    p=marad//60
    s=marad%60

    return f"{o} {p} {s}"
lista=[]
f=open("forgalom.txt",encoding="UTF-8")
for i,sor in enumerate(f):
    if i>0:
        sor=sor.strip().split()
        lista.append(Jarmu(*sor))
print(lista)
n=int(input("2. feladat \n Adja meg a jármű sorszámát"))
print(lista[n-1].halad())
print("3. feladat")
felso=[jarmu for jarmu in lista if jarmu.halad()=="F"]
print(f"A két utolsó között különbség: {felso[-1].masodperc()-felso[-2].masodperc()} másodperc volt")
szam={}
print("4. feladat")
szama={}
szamb={}
for jarmu in lista:
    if jarmu.varos=="A":
        szama[jarmu.ora]=szama.get(jarmu.ora,0)+1
    else:
        szamb[jarmu.ora] = szamb.get(jarmu.ora, 0) + 1
for ora,db in szama.items():
    print(f"{ora} {db} {szamb[ora]}")
print("5. feladat")
gyors=sorted(lista,key=lambda j:j.sebesseg(),reverse=True)
for jarmu in gyors[0:9]:
    print(f"{jarmu.ora} {jarmu.perc} {jarmu.varos} {jarmu.sebesseg():2.1f}")
a=open("also.txt","w",encoding="UTF-8")
print("6.feladat")
for i,jarmu in enumerate(lista):
    ido=jarmu.masodperc()+jarmu.ido

    if i>0:
        if ido<elozo:
            ido=elozo
    a.write(f"f{vissza(ido)}\n")
    elozo = ido



