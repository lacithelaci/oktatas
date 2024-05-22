class Osztaly:
    def __init__(self, az, ora, cselekves):
        self.az = az
        self.ora = ora
        self.cselekves = int(cselekves)

    def __repr__(self):
        return f"{self.az} {self.ora} {self.cselekves}"

    def perc(self):
        return int(self.ora[0:2]) * 60 + int(self.ora[3:])


def beolvasas() -> list[Osztaly]:
    lista = []
    with open("bedat.txt", encoding="utf-8") as f:
        for i in f:
            lista.append(Osztaly(*i.strip("\n").split()))
    return lista


def masodik_feladat(lista: list[Osztaly]) -> None:
    print(f"2. feladat\nAz első tanuló {[i.ora for i in lista if i.cselekves == 1][0]}-kor lépett be a főkapun. ")
    print(f"Az utolsó tanuló {[i.ora for i in lista if i.cselekves == 2][-1]}-kor lépett ki a főkapun. ")


def harmadik_feladat(lista: list[Osztaly]) -> None:
    with open("kesok.txt", "w", encoding="utf-8") as f:
        for i in lista:
            if "08:15" >= i.ora > "07:50" and i.cselekves == 1:
                f.write(f"{i.ora} {i.az}\n")


def negyedik_feladat(lista: list[Osztaly]) -> None:
    print(f"4. feladat\nA menzán aznap {len([i for i in lista if i.cselekves == 3])} tanuló ebédelt.")


def otodik_feladat(lista: list[Osztaly]) -> None:
    print(f"5. feladat\nAznap {len(set(i.az for i in lista if i.cselekves == 4))} tanuló kölcsönzött a könyvtárban. ")
    if len([i for i in lista if i.cselekves == 3]) > len(set(i.az for i in lista if i.cselekves == 4)):
        print("Nem voltak többen, mint a menzán.")
    else:
        print("Többen voltak, mint a menzán.")


def ellenorzo(parameter_azonosito: int, parameter_lista: list[Osztaly]) -> bool:
    seged_lista = [str(x.cselekves) for x in parameter_lista if
                   parameter_azonosito == x.az and x.ora < "11:00" and x.cselekves in [1, 2]]
    return "2" not in "".join(seged_lista) and "11" in "".join(seged_lista)


def hatodik_feladat(lista: list[Osztaly]) -> None:
    azonositok = {i.az for i in lista}
    for azonosito in azonositok:
        if ellenorzo(azonosito, lista):
            print(azonosito, end=" ")


def hetedik_feladat(lista: list[Osztaly]) -> None:
    print("\n7. feladat")
    tanulo_az = input("Egy tanuló azonosítója= ")
    if tanulo_az in [i.az for i in lista]:
        seged = [i.perc() for i in lista if i.az == tanulo_az and i.cselekves in [1, 2]]
        if len(seged) % 2 == 1:
            seged.append(19 * 60)
        perc = 0
        for i in range(0, len(seged), 2):
            perc += seged[i + 1] - seged[i]
        print(f"A tanuló érkezése és távozása között {perc // 60} óra {perc - (perc // 60 * 60)} perc telt el. ")
    else:
        print("Ilyen azonosítójú tanuló aznap nem volt az iskolában.")


def main() -> None:
    adatok = beolvasas()
    masodik_feladat(adatok)
    harmadik_feladat(adatok)
    negyedik_feladat(adatok)
    otodik_feladat(adatok)
    hatodik_feladat(adatok)
    hetedik_feladat(adatok)


if __name__ == '__main__':
    main()
