from typing import cast

from common.repository import Repository
from model import Aircraft
from queries import Queries


class Solution(Queries, Repository):

    @staticmethod
    def type_mapper(values: dict[str, any]) -> object:
        if "number" in values:
            aircraft = Aircraft(**values)
            aircraft.manufacturer = next(
                aircraft.Manufacturer[entry.name]
                for entry in aircraft.Manufacturer
                if entry.value == aircraft.manufacturer
            )
            return aircraft
        else:
            return Aircraft.Configuration(**values)

    @property
    def entities(self) -> list[Aircraft]:
        return cast(list[Aircraft], super().entities)

    def get_count_of_manufacturer(self, manufacturer: Aircraft.Manufacturer) -> int:
        return len([i for i in self.entities if i.manufacturer == manufacturer])

    def order_by_year_desc_number_asc(self) -> list[Aircraft]:

        return [i for i in sorted(self.entities, key=lambda i: (-i.year, i.number))]

    def get_counts_by_manufacturers(self) -> dict[Aircraft.Manufacturer, int]:
        return {i.manufacturer: len([y.number for y in self.entities if y.manufacturer == i.manufacturer]) for i in
                self.entities}

    def get_type_with_most_configurations(self) -> Aircraft:
        return next(i for i in sorted(self.entities, key=lambda i: len(i.configurations), reverse=True))

    def get_latest_type_by_manufacturer(self, manufacturer: Aircraft.Manufacturer) -> Aircraft:
        types = [i for i in self.entities if i.manufacturer == manufacturer]
        if not types:
            raise AssertionError('Nincs típus a gyártóhoz')
        latest = max([i.year for i in self.entities if i.manufacturer == manufacturer])
        return next(i for i in self.entities if i.year == latest)


def main():
    repository = Solution('../data/sample.json')
    print('Gyártótípus szám: ', end=' ')
    print(repository.get_count_of_manufacturer(Aircraft.Manufacturer.AIRBUS))


if __name__ == '__main__':
    main()
