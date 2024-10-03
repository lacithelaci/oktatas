from enum import Enum
from functools import total_ordering


class Gender(Enum):
    MALE = "male"
    FEMALE = "female"


@total_ordering
class Person:
    id: str
    __name: str
    _age: int
    gender: Gender

    def __str__(self) -> str:
        return f"#{self.id}: {self.name} ({self.age}, {self.gender.value})"

    def __repr__(self) -> str:
        return f"{self.id} {self.name} {self.age} {self.gender}"

    def __init__(self, id: str, name: str,
                 age: int, gender: Gender = Gender.MALE.value):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender

    def __eq__(self, other: object) -> bool:
        return isinstance(other, Person) \
            and self.id == other.id

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Person):
            return NotImplemented

        return self.id < other.id


def main() -> None:
    p1 = Person("ID1", "Aladár", 18)
    p2 = Person("ID2", "Aladár", 18)
    p3 = Person("ID3", "Aladár", 18)

    print(p1.gender)


if __name__ == '__main__':
    main()
