from __future__ import annotations
import sys
from functools import total_ordering


@total_ordering
class Person:
    id: str
    __name: str  # privát
    _age: int  # védett
    male: bool
    age_limit: int = 18
    counter: int = 0

    def __init__(self, id: str, name: str, age: int, male: bool = True) -> None:
        self.id = str(id)
        self.__name = str(name)
        self._age = int(age)
        self.male = bool(male)
        Person.counter += 1

    def __str__(self) -> str:
        return f"#{self.id}: {self.__name} ({self._age}, {self.male})"

    def __repr__(self) -> str:
        return f"Person({self.id}, {self.__name}, {self._age}, {self.male})"

    def __eq__(self, other: object):
        return isinstance(other, Person) and self.id == other.id

    def __hash__(self) -> int:
        return self.id.__hash__()

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return NotImplemented
        return self.id < other.id

    def __del__(self):
        Student.counter -= 1  # destruktor

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int) -> None:
        if value < 1:
            raise ValueError("Hibás életkor")
        self._age = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value: str) -> None:
        self.__name = value

    def is_adult(self) -> bool:
        return self.age >= Person.age_limit

    @staticmethod
    def count_adults(lista: list[Person]) -> int:
        db = 0
        for i in lista:
            if i.age >= Person.age_limit:
                db += 1
        return db

    @staticmethod
    def get_adults(lista: list[Person]) -> list[Person]:
        listacska = []
        for i in lista:
            if i.age >= Person.age_limit:
                listacska.append(i)
        return listacska


class Student(Person):
    __neptun_kod: str

    def __init__(self, id: str, name: str, age: int, neptun_kod: str, male: bool = True) -> None:
        super().__init__(str(id), str(name), int(age), bool(male))
        self.__neptun_kod = str(neptun_kod)

    @property
    def neptun_kod(self) -> str:
        return self.__neptun_kod

    @neptun_kod.setter
    def neptun_kod(self, value: str) -> None:
        self.__neptun_kod = value

    def __repr__(self) -> str:
        return f"{super().__repr__()},{self.neptun_kod}"

    def __str__(self) -> str:
        return f"{super().__repr__()},{self.neptun_kod}"


def test():
    p1 = Person("ID1", "Aladár", 17, True)
    p2 = Person("ID1", "Aladár", 18)
    p3 = Student("ID1", "Aladár", 17, "asd-123")
    print(p1 == p2)
    print(p3.__repr__())


def main():
    if len(sys.argv) <= 1:
        raise ValueError("Kevés argumentum")
    n = int(sys.argv[1])
    people = []
    for i in range(n):
        line = input()
        token = line.strip().split(";")
        if len(token) == 4:
            people.append(Person(*token))
        elif len(token) == 5:
            people.append(Student(token[0], token[1], int(token[2]), token[4], bool(token[3])))

    for i in people:
        print(i)

    print(Person.get_adults(people))


if __name__ == '__main__':
    main()
