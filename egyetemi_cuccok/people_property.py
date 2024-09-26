from functools import total_ordering


@total_ordering
class Person:
    id: str
    __name: str
    _age: int
    male: bool
    age_limit: int = 18
    pizzas: list[str] = []

    def __str__(self) -> str:
        return f"#{self.id}: {self.name} ({self.age}, {self.male})"

    def __repr__(self) -> str:
        return f"{self.id} {self.name} {self.age} {self.name}"

    def __init__(self, id: str, name: str,
                 age: int, male: bool = True):
        self.id = id
        self.__name = name
        self._age = age
        self.male = male
        self.pizzas = []

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Person) \
            and self.id == other.id

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return NotImplemented

        return self.id < other.id

    def is_adult(self):
        return self.age >= Person.age_limit

    @property
    def age(self) -> int:
        return self._age

    @age.setter
    def age(self, value: int):
        if value < 1:
            raise ValueError("Hibás életkor")
        self._age = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Nem adtál meg értéket")
        self.__name = value


def main() -> None:
    p1 = Person("ID1", "Aladár", 18, True)
    p2 = Person("ID2", "Aladár", 18, True)
    p3 = Person("ID3", "Aladár", 18, True)

    p1.age = 35
    p1.name = "Géza"
    print(p1.age)
    print(p1.is_adult())
    p1.pizzas.append("pizza1")
    print(p1.pizzas)
    print(Person.pizzas)

if __name__ == '__main__':
    main()
