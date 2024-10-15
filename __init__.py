from __future__ import annotations
from functools import total_ordering


@total_ordering
class Zoo:
    faj: str
    __kor: float
    __suly: float

    def __init__(self, faj: str, suly: float, kor: float = 0.0):
        self.faj = faj
        self.__kor = float(kor)
        self._suly = float(suly)

    def __repr__(self):
        return f"{self.faj}, {self.kor}, {self.suly}"

    def __str__(self):
        return f"{self.faj}: {self.kor} év, {self.suly} kg"

    def __eq__(self, other):
        return isinstance(other, Zoo) and self.faj == other.faj and self.suly == other.suly and self.kor == other.kor

    def __lt__(self, other):
        return (self.faj, -self.kor, self.suly) < (other.faj, -other.kor, other.suly)

    @property
    def kor(self) -> float:
        return self.__kor

    @property
    def suly(self) -> float:
        return self._suly

    @suly.setter
    def suly(self, value: float) -> None:
        self._suly = value

    @staticmethod
    def eletkor(fajnev: str, lista: list[Zoo]) -> list[float]:
        return list(i.kor for i in lista if i.faj == fajnev)


class Emlos(Zoo):
    __labszam: int

    def __init__(self, faj: str, suly: float, labszam: int, kor: float = 0.0):
        super().__init__(faj, suly, kor)
        self.__labszam = int(labszam)

    def __repr__(self):
        return f"{super().__repr__()}, {self.labszam}"

    def __str__(self):
        return f"{super().__str__()}, (lábak száma: {self.labszam})"

    @property
    def labszam(self) -> float:
        return self.__labszam
