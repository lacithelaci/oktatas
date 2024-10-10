import math
from abc import ABC, abstractmethod


class Shape(ABC):

    @abstractmethod
    def count_of_edges(self) -> int:
        pass

    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def perimeter(self) -> float:
        pass


class Rectangle(Shape):
    __a: float
    __b: float

    def __init__(self, a: float, b: float):
        if a <= 0 or b <= 0:
            raise ValueError("Negatív érték")
        self.__a = a
        self.__b = b

    def __str__(self):
        return f"a:{self.__a}, b:{self.__b}"

    @property
    def a(self) -> float:
        return self.__a

    @a.setter
    def a(self, value: float) -> None:
        self.__a = value

    @property
    def b(self) -> float:
        return self.__b

    @b.setter
    def b(self, value: float) -> None:
        self.__b = value

    def count_of_edges(self) -> int:
        return 4

    def area(self) -> float:
        return self.a * self.b

    def perimeter(self) -> float:
        return 2 * (self.a + self.b)


class Circle(Shape):
    __r: float

    def __init__(self, r: float):
        if r <= 0:
            raise ValueError("Negatív érték")
        self.__r = r

    @property
    def r(self) -> float:
        return self.__r

    @r.setter
    def r(self, value: float) -> None:
        self.__r = value

    def __str__(self):
        return f"r: {self.r}"

    def count_of_edges(self) -> int:
        return 0

    def area(self) -> float:
        return self.r * math.pi

    def perimeter(self) -> float:
        return self.r ** 2 * math.pi


class Triangle(Shape):
    _a: float
    _b: float
    _c: float

    def __init__(self, a: float, b: float, c: float):
        if min(a, b, c) <= 0 or a + b < c or b + c < a or c + a < b:
            raise ValueError("Hibás hossz")

        self._a = a
        self._b = b
        self._c = c

    def __str__(self):
        return f"{self.a} {self.b} {self.c}"

    @property
    def a(self) -> float:
        return self._a

    @a.setter
    def a(self, value: float) -> None:
        self._a = value

    @property
    def b(self) -> float:
        return self._b

    @b.setter
    def b(self, value: float) -> None:
        self._b = value

    @property
    def c(self) -> float:
        return self._b

    @c.setter
    def c(self, value: float) -> None:
        self._b = value

    def count_of_edges(self) -> int:
        return 3

    def area(self) -> float:
        return math.sqrt(self.perimeter() / 2 * (self.perimeter() / 2 * self.a) * (self.perimeter() / 2 * self.b) * (
                self.perimeter() / 2 * self.c))

    def perimeter(self) -> float:
        return self.a + self.b + self.c


class RightTriangle(Triangle):

    def __init__(self, a: float, b: float, c: float):
        assert a ** 2 + b ** 2 != c ** 2, "Nem derékszögű"

        super().__init__(a, b, c)

    def __str__(self):
        return super().__str__()

    def area(self) -> float:
        return self.a * self.b / 2


def main():
    r = Circle(4)
    print(r)
    print(r.count_of_edges())
    print(r.area())
    print(r.perimeter())


if __name__ == '__main__':
    main()
