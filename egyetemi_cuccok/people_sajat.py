from functools import total_ordering


@total_ordering
class Pearson:
    id: str
    name: str
    age: int
    male: bool

    def __init__(self, id: str, name: str, age: int, male: bool = True) -> None:
        self.id = str(id)
        self.name = str(name)
        self.age = int(age)
        self.male = bool(male)

    def __str__(self) -> str:
        return f"#<{self.id}>: <{self.name}> (<{self.age}>, <{self.male}>)"

    def __repr__(self) -> str:
        return f"People({self.id}, {self.name}, {self.age}, {self.male})"

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Pearson) and self.id == other.id

    def __hash__(self):
        return self.id.__hash__()

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        if not isinstance(other, Pearson):
            return NotImplemented
        return self.id < other.id

    """

    def __le__(self, other):
        if not isinstance(other, Pearson):
            return NotImplemented
        return self.id <= other.id

    def __gt__(self, other):
        if not isinstance(other, Pearson):
            return NotImplemented
        return self.id > other.id

    def __ge__(self, other):
        if not isinstance(other, Pearson):
            return NotImplemented
        return self.id >= other.id
    """


def main():
    p1 = Pearson("ID1", "Aladár", 18, True)
    p2 = Pearson("ID1", "ASD", 18, True)

    print(p1 == p2)  # false
    print(p1.__hash__(), p2.__hash__())
    print(p1 != p2)  # true
    print(p1.__lt__(p2))  # true


if __name__ == '__main__':
    main()
