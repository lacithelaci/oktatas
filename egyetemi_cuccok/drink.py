from __future__ import annotations

from functools import total_ordering


@total_ordering
class Drink:
    nev: str
    _kiszereles: str
    __ar: int

    def __init__(self, nev: str, ar: int, kiszereles: str = "5 dl"):
        self.nev = nev
        self.__ar = int(ar)
        self._kiszereles = kiszereles

    def __repr__(self) -> str:
        return f"{self.nev}, {self.kiszereles}, {self.ar}"

    def __str__(self) -> str:
        return f"{self.nev}, {self.kiszereles}, {self.ar} Ft"

    def __eq__(self, other: Drink) -> bool:
        return isinstance(other,
                          Drink) and self.ar == other.ar and self.nev == other.nev and self.kiszereles == other.kiszereles

    def __lt__(self, other: Drink) -> bool:
        if not isinstance(other, Drink):
            return NotImplemented
        if self.ar != other.ar:
            return self.ar > other.ar
        if self.kiszereles != other.kiszereles:
            return self.kiszereles < other.kiszereles
        return self.nev < other.nev

    @staticmethod
    def milyen_kiszerelesben_talalhato(lista: list[Drink], nev: str) -> str:
        for i in lista:
            if i.nev == nev:
                return i.kiszereles
        return "Nem található ilyen ital"

    @staticmethod
    def kiszereleszam(lista: list[Drink]) -> int:
        return len(set(i.kiszereles for i in lista))

    @staticmethod
    def dragabb_italszam(lista: list[Drink], ar: int) -> int:
        return len([i for i in lista if i.ar > ar])

    @staticmethod
    def dragabb_kiszereles(lista: list[Drink], ar: int) -> int:
        return len(set(i.kiszereles for i in lista if i.ar > ar))

    @staticmethod
    def tartalmazza(lista: list[Drink], kiszereles: set[str]) -> int:
        return len([i for i in lista if i.kiszereles in kiszereles])

    @staticmethod
    def kiszereleshez_db(lista: list[Drink]) -> dict[str, int]:
        szotar = {}
        for i in lista:
            szotar[i.kiszereles] = szotar.get(i.kiszereles, 0) + 1
        return szotar

    @staticmethod
    def kiszereleshez_nevek(lista: list[Drink]) -> dict[str, set[str]]:
        szotar = {}
        for i in lista:
            if i.kiszereles not in szotar:
                szotar[i.kiszereles] = set()
            else:
                szotar[i.kiszereles].add(i.nev)
        return szotar

    @staticmethod
    def atlagtol_dragabb(lista: list[Drink]) -> set[Drink]:
        atlagar = sum([i.ar for i in lista]) / len([i.ar for i in lista])
        return set(i for i in lista if i.ar > atlagar)

    @staticmethod
    def lista_atlagtol_dragabb(lista: list[Drink]) -> list[Drink]:
        atlagar = sum([i.ar for i in lista]) / len([i.ar for i in lista])
        return sorted(list(i for i in lista if i.ar > atlagar), key=lambda i: i.ar, reverse=True)

    @property
    def ar(self) -> int:
        return self.__ar

    @ar.setter
    def ar(self, value: int) -> None:
        self.__ar = value

    @property
    def kiszereles(self) -> str:
        return self._kiszereles


class Szeszesital(Drink):
    __alkohol: float

    def __init__(self, nev: str, ar: int, alkohol: float, kiszereles: str = "5 dl"):
        super().__init__(nev, ar, kiszereles)
        self.__alkohol = float(alkohol)

    def __repr__(self) -> str:
        return f"{super().__repr__()}, {self.alkohol}"

    def __str__(self) -> str:
        return f"{self.alkohol}% alkoholtartalmú {super().__repr__()} Ft"

    @property
    def alkohol(self) -> float:
        return self.__alkohol

    @alkohol.setter
    def alkohol(self, value: float) -> None:
        self.__alkohol = value

    @staticmethod
    def lista_atlagtol_dragabb(lista: list[Drink]) -> list[Szeszesital]:
        return [i for i in lista if isinstance(i, Szeszesital)]
