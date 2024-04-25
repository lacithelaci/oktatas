#!/usr/bin/python3

# ---------------------------------------------------

print("\n1. feladat");
E = []
be = open("eloadasok.txt","r",encoding="UTF-8")
for sor in be:
    sor = sor.strip().split('\t')
    eloadas = {
	"eloado" : sor[0],
	"ho" : int(sor[1]),
	"nap" : int(sor[2]),
	"sorsz" : int(sor[3]),
	"hossz" : int(sor[4]),
	"cim" : sor[5],
	"eszkozok" : sor[6]
    }
    E.append(eloadas)
be.close()
print("Az adatok beolvasása sikeresen megtörtént.")

# ---------------------------------------------------

print("\n2. feladat");

def rendez(eloadas):
    return 100*eloadas["nap"] + eloadas["sorsz"]

E.sort(key = rendez)
kiirt_nap = 0
for eloadas in E:
    if kiirt_nap != eloadas["nap"]:
	    print("\nnovember {0}.:".format(eloadas["nap"]))
	    kiirt_nap = eloadas["nap"]
    print("  {0}. {1}: {2}".format(eloadas["sorsz"], eloadas["eloado"], eloadas["cim"]))

# ---------------------------------------------------

print("\n3. feladat");
ossz = 0
for i in range(len(E)):
    ossz = ossz + E[i]["hossz"]
    if i == len(E) - 1 or E[i]["nap"] != E[i+1]["nap"]:
	    print("  {0}. nap: {1}:{2}".format(E[i]["nap"]-4, ossz // 60, ossz % 60))
	    ossz = 0

# ---------------------------------------------------

print("\n4. feladat");
max = 0
for eloadas in E:
    if eloadas["nap"] == 6 and eloadas["hossz"] > max:
	    max = eloadas["hossz"]
for eloadas in E:
    if eloadas["nap"] == 6 and eloadas["hossz"] == max:
	    print("{0} {1} perc".format(eloadas["eloado"], eloadas["hossz"]))


# ---------------------------------------------------

print("\n5. feladat");
j = 0
for i in range(5, 9):
    ossz = 8*60;
    while j < len(E) and E[j]["nap"] == i:
	    ossz = ossz + E[j]["hossz"] + 20
	    j = j + 1
    if ossz >= 12*60:
	    ossz = ossz + 60
    print("november {0}.: {1}:{2}".format(i, ossz // 60, ossz % 60))

# ---------------------------------------------------

print("\n6. feladat")
ossz = 8*60;
j = 0;
while j < len(E) and ossz <= 12*60:
    if E[j]["nap"] == 7:
	    ossz = ossz + E[j]["hossz"] + 20
    j = j + 1
print("Az ebédszünet {0}:{1} órakor kezdődik az harmadik napon.".format(ossz // 60, ossz % 60))

# ---------------------------------------------------

print("\n7. feladat")
nevek = []
ismet = []
for eloadas in E:
    nevek.append(eloadas["eloado"])
for nev in nevek:
    if nev not in ismet:
	    db = nevek.count(nev)
	    if db > 1:
		    print("{0} {1}".format(nev, db))
		    ismet.append(nev)
if len(ismet) == 0:
    print("Nem találtam egyező neveket.")

# ---------------------------------------------------

print("\n8. feladat")
nap = int(input("Kérem a napot (5-8): "))
ora = int(input("Kérem az órát: "))
perc = int(input("Kérem a percet: "))
ido = ora*60 + perc
ebed_elott = True
ossz = 60*8
if ido < ossz:
    print("Még nem kezdődött el")
i = 0
while ossz < ido and i < len(E):
    if nap == E[i]["nap"]:
	    ossz = ossz + E[i]["hossz"]
	    if ossz >= ido:
		    print("Előadás")
	    else:
		    ossz = ossz + 20
		    if ossz >= ido:
			    print("Vita")
		    elif ebed_elott and ossz >= 12*60:
			    ossz = ossz + 60
			    ebed_elott = False
			    if ossz >= ido:
				    print("Ebéd")
    i = i + 1;
if ido > ossz:
    print("Véget ért már")

# ---------------------------------------------------

print("\n9. feladat")
ki = open("idorend2.txt", "w")
nap = 0;
for eloadas in E:
    if eloadas["nap"] != nap:
	    ebed_elott = True
	    ossz = 8*60
	    nap = eloadas["nap"]
	    print("november {0}.".format(nap), file=ki)
    print("  {0}:{1:02d}-".format(ossz // 60, ossz % 60), end='', file=ki)
    ossz = ossz + eloadas["hossz"];
    print("{0}:{1:02d} {2}: {3} ({4})".format(ossz // 60, ossz % 60, eloadas["eloado"], eloadas["cim"], eloadas["eszkozok"]), file=ki)
    print("  {0}:{1:02d}-".format(ossz // 60, ossz % 60), end='', file=ki)
    ossz = ossz + 20
    print("{0}:{1:02d} Vita".format(ossz // 60, ossz % 60), file=ki)
    if ebed_elott and ossz >= 12*60:
	    print("  {0}:{1:02d}-".format(ossz // 60, ossz % 60), end='', file=ki)
	    ossz = ossz + 60
	    print("{0}:{1:02d} Ebéd".format(ossz // 60, ossz % 60), file=ki)
	    ebed_elott = False
ki.close()
print("A fájl lérehozása sikeresen megtörtént.")

