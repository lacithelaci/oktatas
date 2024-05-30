from collections import defaultdict


class Szinek:
    def __init__(self, red, green, blue, sorszam, oszlopszam):
        self.red = int(red)
        self.green = int(green)
        self.blue = int(blue)
        self.sorszam = int(sorszam)
        self.oszlopszam = int(oszlopszam)

    def __repr__(self):
        return f"({self.red},{self.green},{self.blue})"


def beolvasas() -> list[Szinek]:
    lista = list()
    with open("kep.txt") as f:
        sorszama = 1
        for sor in f:
            elemek = sor.split()
            for oszlopszama in range(1, len(elemek) // 3 + 1):
                r, g, b = elemek[(oszlopszama - 1) * 3: oszlopszama * 3]
                lista.append(Szinek(r, g, b, sorszama, oszlopszama))
            sorszama += 1
    return lista


def masodik_feladat(lista: list[Szinek]) -> None:
    print("2.feladat:\nkérem egy képpont adatait")
    sor = int(input("Sor: "))
    oszlop = int(input("Oszlop: "))
    megadott_szin = [i for i in lista if i.sorszam == sor and i.oszlopszam == oszlop]
    print(f"A képpont színe RGB({megadott_szin[0].red},{megadott_szin[0].green},{megadott_szin[0].blue})")


def harmadik_feladat(lista: list[Szinek]) -> None:
    print("3. feladat:")
    vilagos = [i for i in lista if i.blue + i.green + i.red > 600]
    print(f"A világos képpontok száma: {len(vilagos)}")


def negyedik_feladat(lista: list[Szinek]) -> None:
    print("4. feladat:")
    legsotetebb = min([i.red + i.green + i.blue for i in lista])
    print(f"A legsötétebb pont RGB összege: {legsotetebb}\nA legsötétebb pixelek színe: ")
    for i in lista:
        if i.blue + i.red + i.green == legsotetebb:
            print(f"RGB({i.red},{i.green},{i.blue})")


def hatar(sorszam: list[int], elteres: int) -> bool:
    for i in range(len(sorszam) - 1):
        if abs(sorszam[i] - sorszam[i + 1]) > elteres:
            return True
    return False


def hatodik_feladat(lista: list[Szinek]) -> None:
    print("6. feladat")
    sorszam_dict = defaultdict(list)
    for elem in lista:
        sorszam_dict[elem.sorszam].append(elem.blue)
    seged_valasz = []
    for i in range(1, 361):
        if i in sorszam_dict and hatar(sorszam_dict[i], 10):
            seged_valasz.append(i)
    print(f"A felhő legfelső sora: {seged_valasz[0]}\nA felhő legalsó sora: {seged_valasz[-1]}")


def main():
    lista = beolvasas()
    masodik_feladat(lista)
    harmadik_feladat(lista)
    negyedik_feladat(lista)
    hatodik_feladat(lista)


if __name__ == '__main__':
    main()
