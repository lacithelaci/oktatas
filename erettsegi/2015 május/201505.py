with open('Adatok/201505/Forrasok/4_Expedicio/veetel.txt', 'r', encoding='utf-8') as in_file:
    szoveg = in_file.readlines()
    print(szoveg)
    adatok = []
    i = 1
    for sor in szoveg:
        sor = sor.strip()
        if i % 2 != 0:
            sor = sor.split()
            eleje = list(map(int, sor))
            i +=  1
        else:
            sor = [eleje[0],eleje[1], sor]
            adatok.append(sor)
            i += 1
    print(adatok)

    print('2. feladat')
    print(f'Az első üzenet rögzítője: {adatok[0][1]}')
    print(f'Az utolsó üzenet rögzítője: {adatok[-1][1]}')

    print('3. feladat')
    for sor in adatok:
        if sor[2].find('farkas') > -1:
            print(f'{sor[0]}. nap {sor[1]}. rádióamatőr')

    print('4. feladat')
    # első megoldás
    nemvoltadas = [] # az 5. feladat miatt kigyűjtjük, mely napokon nem volt adás
    seged = []
    osszegek = []
    p = 0
    for sor in adatok:
        seged.append(sor[0])
    for i in range(1,12):
        j = seged.count(i)
        p += j
        osszegek.append(p)  # az 5. feladat miatt kigyűjtjük, hogy hányszor szerepel a hiányosan megadott szöveg (mikor kezdődik új nap!)
        print(f'{i}. nap: {j} rádióamatőr')
        if j == 0:
            nemvoltadas.append(i)
    print(osszegek)

    # második megoldás
    stat = {}
    for sor in adatok:
        nap = sor[0]
        stat[nap] = stat.get(nap,0)+1
    i = 1
    for kulcs, adat in sorted(stat.items()):
        if kulcs == i:
            print(f'második módszerrel: {i}. nap: {adat} rádióamatőr')
            i += 1
        else:
            print(f'második módszerrel: {i}. nap: 0 rádióamatőr')
            i += 1

    print('5. feladat')
    adatok1 = sorted(adatok) # rendezzük a listát
    seged = []
    seged2 = []
    z = 0 # ezzel nézzük majd, hányadik üzenetnél kezdődik az új nap
    for szamlalo in range(1,12): # végigmegyünk a napokon
        for f in adatok1[z][2]:
            seged.append(f)  # az adott napon ez az első hiányos adatsor, ehhez hasonlítjuk majd a következőket
        for k, sor in enumerate(adatok1): # vesszük az elemek indexét és magát az üzenetet a rendezett listából
            if z <= k < osszegek[szamlalo-1]: # csak az adott nap üzeneteit nézzük
                for index, j in enumerate(sor[2]):
                    if seged[index] != j and j != "#": # itt töltjük ki a hézagokat az egymás után olvasott üzenetekből
                        seged[index] = j
                x ="".join(seged) # visszabazseváljuk olvasható formátumra (összefűzzük őket)
        z = osszegek[szamlalo-1] # ugrunk az indexel, hogy a következő nap első üzenetével kezdje majd az összehasonlításokat
        seged = [] # kiürítjük az eddigi első üzenetet tartalmazó listát
        y = [szamlalo, x]
        seged2.append(y) # ebben lesz a nap sorszáma és az összeolvasott üzenet

    #nemvoltadas = [1,3] itt csak teszteltem, de érdemes benne hagyni
    for sor in nemvoltadas: # fent kigyűjtöttem, hogy melyik nap nem volt adás
        for masodik in seged2:
            if sor == masodik[0]: # ha van olyan nap, amikor nem volt adás, akkor az üzenetet beállítjük #-re
                seged2[sor-1][1] = "#"

    with open('Adatok/201505/Forrasok/4_Expedicio/adas.txt', 'w', encoding='utf-8') as out_file:
        for sor in seged2:
            print(f"{sor[0]}. napon az üzenet: {sor[1]}", file=out_file)

    print("6. feladat")
    def szame(szo):
        vissza = True
        for i in range(len(szo)):
            if szo[i] < '0' or szo[i] > '9':
                vissza = False
        return vissza

    print('7. feladat')
    napszam = int(input('Adja meg a nap sorszámát: '))
    figysorszam = int(input('Adja meg a rádióamatőr sorszámát: '))
    van = 0 # ezzel figyeljük majd, hogy van-e az adott napon amatőr
    for sor in adatok1:
        if sor[0] == napszam and sor[1] == figysorszam: # megnézzük, hogy van-e az adott napon ilyen számú amatőr
            van = 1
            if szame(sor[2][0]): # ha számmal kezdődik a feljegyzés, akkor tovább vizsgáljuk
                elsoszokoz = sor[2].find(' ') # megkeressük az első szóköz helyét, ebben kell lennie a szám/szám résznek
                hasznalhato = sor[2].find('#', 0, elsoszokoz) #az elejétől megnézzük a szóközig. Ha van benne #, akkor nem használható az adat!
            if hasznalhato == -1 : # akkor igaz, ha nincs benne #, tehát szám/szám formája van!
                    elsoszam = int(sor[2][:sor[2].find('/')]) # az elejétől a / -ig vesszük az első számot
                    masodikszam = int(sor[2][sor[2].find('/')+1:elsoszokoz]) # a / utántól a szóközig vesszük a második számot
                    farkasszam = elsoszam + masodikszam
                    print(f'A megfigyelt egyedek száma: {farkasszam}')
            else:
                print('Nincs információ')
    if van == 0:
        print('Nincs ilyen feljegyzés')






                





