from functools import total_ordering


@total_ordering
class Car:
    plate: str
    _manufacturer: str
    __year: int
    __automatic: bool
    car_count: int = 0

    def __init__(self, plate, manufacturer, automatic, year: int = 2022):
        Car.car_count += 1
        self.plate = plate
        self.manufacturer = manufacturer
        self.year = int(year)
        self.automatic = bool(automatic)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Car):
            return False

        return (self.plate, self.year, self.manufacturer) \
            == (other.plate, other.year, other.manufacturer)

    def __lt__(self, other: object) -> bool:
        if not isinstance(other, Car):
            return NotImplemented

        return (self.year, self.manufacturer, self.plate) \
            < (other.year, other.manufacturer, other.plate)

    def has_new_plate(self):
        if len(self.plate) != 7:
            return False
        return self.plate[:4].isalpha() and self.plate[4:].isdigit()

    @property
    def manufacturer(self) -> str:
        return self._manufacturer

    @manufacturer.setter
    def manufacturer(self, value: str) -> None:
        self._manufacturer = value

    @property
    def year(self) -> int:
        return self.__year

    @year.setter
    def year(self, value: int) -> None:
        self.__year = value

    @property
    def automatic(self) -> bool:
        return self.__automatic

    @automatic.setter
    def automatic(self, value: bool) -> None:
        self.__automatic = value


def main():
    a = Car("A2DF352", "Audi", 2000, True)
    b = Car("ASDF32", "Audi", 2000, True)
    print(a.has_new_plate())


if __name__ == '__main__':
    main()
