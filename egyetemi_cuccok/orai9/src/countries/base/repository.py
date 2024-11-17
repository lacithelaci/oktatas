import json
from copy import deepcopy
from typing import Any

from countries.base.model import Country


class CountryRepository:
    """
    Reads and stores data of countries.
    """

    __countries = list[Country]

    def __init__(self, path: str) -> None:
        """
        Creates an instance.

        :param path: the path of the JSON document storing countries
        """
        with open(path, encoding="utf-8") as file:
            self.__countries = json.load(file, object_hook=self.type_mapper)

    @staticmethod
    def type_mapper(values: dict[str, any]) -> Country | dict[str, Any]:
        """
        Maps thw nodes of the JSON document to types.

        :param values: a dictionary representing the actual node
        :return: the corresponding object
        """
        if "name" in values:
            country = Country(**values)
            country.region = next(
                Country.Region[entry.name]
                for entry in Country.Region
                if entry.value == country.region
            )
            return country
        else:
            return values

    @property
    def countries(self):
        """
        Returns a view on the countries.

        :return: the countries
        """
        return [deepcopy(d) for d in self.__countries]
