import sys
from typing import NamedTuple


class RollerCoaster(NamedTuple):
    name: str
    world: str
    height: int
    time: int


def from_line(line: str) -> RollerCoaster:
    line = line.strip("\n").split(";")
    return RollerCoaster(line[0], line[1], int(line[2]), int(line[3]))


def to_line(coaster: RollerCoaster) -> str:
    return f"{coaster.name} ({coaster.world}): {coaster.time}"


def order(coasters: list[RollerCoaster]) -> list[RollerCoaster]:
    return sorted(coasters, key=lambda i: (i.time, -i.height, i.name))


def query(coasters: list[RollerCoaster]) -> set[str]:
    return set(i.world for i in coasters)


def query2(coasters: list[RollerCoaster]) -> dict[str, int]:
    szotar = dict()
    for i in coasters:
        szotar[i.world] = szotar.get(i.world, 0) + 1
    return szotar


def query3(coasters: list[RollerCoaster]) -> dict[str, list[RollerCoaster]]:
    seged_halmaz = set(i.world for i in coasters)
    szotar = dict()
    for i in seged_halmaz:
        seged_lista = []
        for y in coasters:
            if i == y.world:
                seged_lista.append(y)
        szotar[i] = seged_lista
    return szotar


def query4(coasters: list[RollerCoaster]) -> dict[str, list[str]]:
    seged_halmaz = set(i.world for i in coasters)
    szotar = dict()
    for i in seged_halmaz:
        seged_lista = []
        for y in coasters:
            if i == y.world:
                seged_lista.append(y.name)
        szotar[i] = seged_lista
    return szotar


def main() -> None:
    if len(sys.argv) != 1:
        lista = []
        try:
            fajlnev = sys.argv[1]
            with open(f"{fajlnev}", "r", encoding="UTF-8") as fajl:
                for line in fajl:
                    lista.append(from_line(line))
                parancssor = sys.argv[2]
                if parancssor == "order":
                    for i in order(lista):
                        print(to_line(i))
                elif parancssor == "query":
                    halmaz = query(lista)
                    for i in halmaz:
                        print(i)
                elif parancssor == "query2":
                    szotar = query2(lista)
                    for index, i in szotar.items():
                        print(str(index) + ": " + str(i))
                elif parancssor == "query3":
                    szotar = query3(lista)
                    for index, i in szotar.items():
                        print(index + ":")
                        for y in i:
                            print(to_line(y))
                elif parancssor == "query4":
                    szotar = query4(lista)
                    for index, i in szotar.items():
                        print(index + ":")
                        for y in i:
                            print(y)
                else:
                    print("Hibásan megadott parancssori argomentum.", file=sys.stderr)
        except FileNotFoundError:
            print("A fájl nem található.", file=sys.stderr)
        except IndexError:
            print("Hiányzó parancssori argomentum.", file=sys.stderr)
    else:
        print("Ez egy hibaüzenet a standard hibacsatornán, mivel a fájl nem található.", file=sys.stderr)


if __name__ == '__main__':
    main()
