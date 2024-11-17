from abc import abstractmethod, ABC
from typing import Optional

from countries.base.model import Country


class BasicCountryQueries(ABC):
    """
    Defines basic queries for class CountryRepository.
    """

    @abstractmethod
    def get_greatest_population(self) -> int:
        """
        Returns the value of the greatest population.

        :return: the greatest population
        """

    @abstractmethod
    def get_average_population(self) -> float:
        """
        Returns the value of the average population.

        :return: the average population
        """

    @abstractmethod
    def get_count_of_european_countries(self) -> int:
        """
        Returns the count of European countries.

        :return: the count of countries
        """

    @abstractmethod
    def get_count_of_countries_of_region(self, region: Country.Region) -> int:
        """
        Returns the count of countries that are located in the given continent.

        :param region: the continent
        :return: the count of countries
        """

    @abstractmethod
    def get_population_by_region(self, region: Country.Region) -> int:
        """
        Returns the population of the given continent.

        :param region: the continent
        :return: the population
        """

    @abstractmethod
    def is_population_exists(self, population: int) -> bool:
        """
        Returns whether a country exists having the given population.

        :param population: the population
        :return: the result
        """

    @abstractmethod
    def get_country_by_code(self, code: str) -> Optional[Country]:
        """
        Returns the country which has the given code.

        :param code: the country code
        :return: the country
        """

    @abstractmethod
    def get_most_populous_country_by_region(self, region: Country.Region) -> Country:
        """
        Returns the country which has the greatest population of its continent.

        :param region: the continent
        :return: the country
        """

    @abstractmethod
    def get_first_country_by_starting_letter(self, letter: str) -> Optional[Country]:
        """
        Returns the first country which name starts with the given letter.

        :param letter: the letter
        :return: the country
        """

    @abstractmethod
    def get_distinct_names(self) -> set[str]:
        """
        Returns a set containing all the distinct country names;

        :return: the names
        """

    @abstractmethod
    def get_distinct_capitals(self) -> set[str]:
        """
        Returns a set containing all the distinct capitals.

        :return: the capitals
        """

    @abstractmethod
    def get_countries_below_population_limit(self, limit: int) -> set[Country]:
        """
        Returns the set of countries which population is less than the given limit.

        :param limit: the limit
        :return: the set of countries
        """

    @abstractmethod
    def get_distinct_populations_by_region(self, region: Country.Region) -> set[int]:
        """
        Returns all the population values that belong to the given continent.

        :param region: the continent
        :return: the set of populations
        """

    @abstractmethod
    def get_countries_by_population(self, lower_bound: int, upper_bound: int = None) -> set[Country]:
        """
        Returns each country which has a population which is between the given bounds (inclusive).

        :param lower_bound: the lower bound
        :param upper_bound: the upper bound (optional)
        :return: the set of countries
        """


class SortingCountryQueries(ABC):
    """
    Defines sorting queries for class CountryRepository.
    """

    @abstractmethod
    def get_countries_order_by_population_desc(self) -> list[Country]:
        """
        Returns the list of countries ordered by:

        * their populations in descending order

        :return: the sorted list of countries
        """

    @abstractmethod
    def get_countries_order_by_length_of_capital_then_by_population_desc(self) -> list[Country]:
        """
        Returns the list of countries ordered by:

        * the names of their capitals
        * their population in descending order

        :return: the sorted list of countries
        """

    @abstractmethod
    def get_countries_order_by_length_of_capital_then_by_capital(self) -> list[Country]:
        """
        Returns the list of countries ordered by:

        * the length of the names of their capitals
        * their capitals

        :return: the sorted list of countries
        """

    @abstractmethod
    def get_capitals_order_by_name_desc(self) -> list[str]:
        """
        Returns the capital of each country in descending order.

        :return: the capitals
        """


class AggregationCountryQueries(ABC):
    """
    Defines queries for class CountryRepository that deal with aggregation.
    """

    @abstractmethod
    def get_countries_by_codes(self) -> dict[str, Country]:
        """
        Returns a dictionary which maps each country code to the corresponding country.

        :return: the dictionary
        """

    @abstractmethod
    def get_count_of_countries_by_regions(self) -> dict[Country.Region, int]:
        """
        Returns a dictionary which maps each region to the count of its countries.

        :return: the dictionary
        """

    @abstractmethod
    def get_countries_by_regions(self) -> dict[Country.Region, set[Country]]:
        """
        Returns a dictionary which maps each region to its countries.

        :return: the dictionary
        """

    @abstractmethod
    def get_most_populous_country_by_regions(self) -> dict[Country.Region, Country]:
        """
        Returns a dictionary which maps each region to its most populous country.

        :return: the dictionary
        """

    @abstractmethod
    def get_countries_by_regions_order_by_capitals(self) -> dict[Country.Region, list[Country]]:
        """
        Returns a dictionary which maps each region the list of its countries ordered by their capital names to their continent.

        :return: the dictionary
        """

    @abstractmethod
    def get_countries_by_regions_filter_by_population(self, lower_bound: int, upper_bound: int) \
            -> dict[Country.Region, set[Country]]:
        """
        Returns a dictionary which maps each region to the corresponding countries which population is between the given bounds (inclusive) to their continent.

        :param lower_bound: the lower bound
        :param upper_bound: the upper bound
        :return: the dictionary
        """

    @abstractmethod
    def get_countries_by_regions_and_codes(self) -> dict[Country.Region, dict[str, Country]]:
        """
        Returns a dictionary which maps each region to the corresponding country codes, then each country code to the corresponding country.

        :return: the dictionary
        """

    @abstractmethod
    def get_countries_by_regions_and_first_letters(self) -> dict[Country.Region, dict[str, set[Country]]]:
        """
        Returns a dictionary which maps region to the letters that occur in the first place of corresponding country names, then each letter to the corresponding countries.

        :return: the dictionary
        """

    @abstractmethod
    def get_countries_by_first_letters_and_regions(self) -> dict[str, dict[Country.Region, set[Country]]]:
        """
        Returns a dictionary which maps the letters that occur in the first place of corresponding country names to regions, then each letter to the corresponding countries.

        :return: the dictionary
        """

    @abstractmethod
    def get_localized_country_names_by_regions(self, locale: str) -> dict[Country.Region, set[str]]:
        """
        Returns a dictionary which maps each region to the set of country names, using the given locale.

        :param locale: the locale
        :return: the dictionary
        """

    @abstractmethod
    def get_first_localized_country_names_by_regions(self, locale: str) -> dict[Country.Region, str]:
        """
        Returns a dictionary which maps each region to the country name which is the first in the given locale.

        :param locale: the locale
        :return: the dictionary
        """

    @abstractmethod
    def get_first_localized_countries_by_regions(self, locale: str) -> dict[Country.Region, Country]:
        """
        Returns a dictionary which maps each region to the country which name is the first in the given locale.

        :param locale: the locale
        :return: the dictionary
        """
