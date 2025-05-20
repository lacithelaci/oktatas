class Konyv:
    def __init__(self, ev: int, negyedev: int, eredet: str, leiras: str, peldanyszam: int) -> None:
        self.ev = int(ev)
        self.negyedev = int(negyedev)
        self.eredet = eredet
        self.leiras = leiras
        self.peldanyszam = int(peldanyszam)


def main() -> None:
    lista: list[Konyv] = list()
    with open('kiadas.txt', encoding='utf-8') as f:
        for i in f:
            lista.append(Konyv(*i.strip('\n').split(';')))
    print(f'2. feladat:')
    szerzo: str = input('Szerző: ')
    print(f'{len([i for i in lista if szerzo in i.leiras])} könyvkiadás\n3. feladat: ')
    legnagyobb_peldanyszam: int = max([i.peldanyszam for i in lista])
    print(
        f'Legnagyobb példányszám: {legnagyobb_peldanyszam}, előfordult '
        f'{len([i for i in lista if i.peldanyszam == legnagyobb_peldanyszam])} alkalommal ')
    print('4. feladat: ')
    kulfoldi: Konyv = [i for i in lista if i.eredet == 'kf' and i.peldanyszam >= 40000][0]
    print(f'{kulfoldi.ev}/{kulfoldi.negyedev}. {kulfoldi.leiras}')
    print('5. feladat\nÉv\tMagyar kiadás\tMagyar példányszám\tKülföldi kiadás\tKülföldi példányszám')
    evek: set[int] = set(i.ev for i in lista)
    f = open('tabla.html', 'w', encoding='utf-8')
    f.write('<table>\n<tr><th>Év</th><th>Magyar kiadás</th><th>Magyar példányszám</th><th>Külföldi\n')
    for y in evek:
        magyar_kiadas: int = 0
        kulfoldi_kiadas: int = 0
        magyar_peldanyszam: int = 0
        kulfoldi_peldanyszam: int = 0
        for i in lista:
            if i.ev == y:
                if i.eredet == 'kf':
                    kulfoldi_kiadas += 1
                    kulfoldi_peldanyszam += i.peldanyszam
                else:
                    magyar_peldanyszam += i.peldanyszam
                    magyar_kiadas += 1
        print(f'{y}\t{magyar_kiadas}\t{magyar_peldanyszam}\t{kulfoldi_kiadas}\t{kulfoldi_peldanyszam}')
        f.write(f'<tr><td>{y}</td><td>{magyar_kiadas}</td><td>{magyar_peldanyszam}</td><td>{kulfoldi_kiadas}</td>'
                f'<td>{kulfoldi_peldanyszam}</td></tr>\n')
    f.write('</table> ')
    f.close()

    print('6. feladat:\nLegalább kétszer, nagyobb példányszámban újra kiadott könyvek:')
    tobbszor_kiadott: dict[str, list[int]] = {}

    for i in lista:
        tobbszor_kiadott.setdefault(i.leiras, []).append(i.peldanyszam)
    for kulcs, ertek in tobbszor_kiadott.items():
        tobb_kiadott_peldany: int = 0
        if len(ertek) > 1:
            for i in range(1, len(ertek)):
                if ertek[i] > ertek[0]:
                    tobb_kiadott_peldany += 1
            if tobb_kiadott_peldany >= 2:
                print(kulcs)


if __name__ == '__main__':
    main()
