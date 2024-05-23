import math


class Krater:
    def __init__(self, x, y, r, nev):
        self.x = float(x)
        self.y = float(y)
        self.r = float(r)
        self.nev = nev

    def __repr__(self):
        return f"{self.x} {self.y} {self.r} {self.nev}"


def beolvasas() -> list[Krater]:
    lista = []
    with open("felszin_tpont.txt", encoding="utf-8") as f:
        for i in f:
            lista.append(Krater(*i.strip('\n').split('\t')))
    return lista


def masodik_feladat(lista: list[Krater]) -> None:
    print(f"2. feladat\nA kráterek száma: {len(lista)}")


def harmadik_feladat(lista: list[Krater]) -> None:
    print("3. feladat")
    benne_van = False
    nev = input("Kérem egy kráter nevét: ")
    for i in lista:
        if i.nev == nev:
            print(f"A(z) {i.nev} középpontja X={i.x} Y={i.y} sugara R={i.r}. ")
            benne_van = True
    if not benne_van:
        print(f"Nincs ilyen nevű kráter.")


def negyedik_feladat(lista: list[Krater]) -> None:
    a = sorted(lista, key=lambda i: i.r, reverse=True)[0]
    print(f"4. feladat\nA legnagyobb kráter neve és sugara: {a.nev} {a.r} ")


def tavolsag(x1: float, y1: float, x2: float, y2: float) -> float:
    return math.sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1))


def hatodik_feladat(lista: list[Krater]) -> None:
    krater = input("6.feladat\nKérem egy kráter nevét: ")
    krater_adatok = None
    for i in lista:
        if i.nev == krater:
            krater_adatok = i

    if krater_adatok:
        kozos = [i.nev for i in lista if tavolsag(i.x, krater_adatok.x, i.y, krater_adatok.y) > i.r + krater_adatok.r]
        print("Nincs közös része:")
        for i in kozos:
            print(i, end=", ")


def hetedik_feladat(lista: list[Krater]) -> None:
    nevek = [i for i in lista]
    print("\n7. feladat")
    for y in nevek:
        for i in lista:
            if tavolsag(y.x, y.y, i.x, i.y) < y.r - i.r:
                print(f"A(z) {y.nev} kráter tartalmazza a(z) {i.nev} krátert. ")


def nyolcadik_feladat(lista: list[Krater]) -> None:
    with open("terulet.txt", "w", encoding="utf-8") as f:
        for i in lista:
            f.write(f"{round(i.r ** 2 * 3.14, 2)}\t{i.nev}\n")


def main() -> None:
    adatok = beolvasas()
    masodik_feladat(adatok)
    harmadik_feladat(adatok)
    negyedik_feladat(adatok)
    hatodik_feladat(adatok)
    hetedik_feladat(adatok)
    nyolcadik_feladat(adatok)


if __name__ == '__main__':
    main()
