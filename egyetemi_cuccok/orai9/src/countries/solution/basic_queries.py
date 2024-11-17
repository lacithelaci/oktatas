from typing import Optional

from countries.base.model import Country
from countries.base.queries import BasicCountryQueries
from countries.base.repository import CountryRepository


class BasicCountryRepository(CountryRepository, BasicCountryQueries):

    def get_greatest_population(self) -> int:
        return max(i.population for i in self.countries)

    def get_average_population(self) -> float:
        return sum(i.population for i in self.countries) / len(self.countries)

    def get_count_of_european_countries(self) -> int:
        return len([i for i in self.countries if i.region == i.Region.EUROPE])

    def get_count_of_countries_of_region(self, region: Country.Region) -> int:
        return len([i for i in self.countries if i.region == region])

    def get_population_by_region(self, region: Country.Region) -> int:
        return sum([i.population for i in self.countries if i.region == region])

    def is_population_exists(self, population: int) -> bool:
        return bool([i for i in self.countries if i.population == population])

    def get_country_by_code(self, code: str) -> Optional[Country]:
        return next(i for i in self.countries if i.code == code)

    def get_most_populous_country_by_region(self, region: Country.Region) -> Country:
        maximum = max(i.population for i in self.countries if i.region == region)
        return next(i for i in self.countries if maximum == i.population and region == i.region)

    def get_first_country_by_starting_letter(self, letter: str) -> Optional[Country]:
        return next(i for i in self.countries if i.name[0] == letter)

    def get_distinct_names(self) -> set[str]:
        return set(i.name for i in self.countries)

    def get_distinct_capitals(self) -> set[str]:
        return set(i.capital for i in self.countries)

    def get_countries_below_population_limit(self, limit: int) -> set[Country]:
        return set(i for i in self.countries if i.population < limit)

    def get_distinct_populations_by_region(self, region: Country.Region) -> set[int]:
        return set(i.population for i in self.countries if region == i.region)

    def get_countries_by_population(self, lower_bound: int, upper_bound: int = None) -> set[Country]:
        return set(i for i in self.countries if i.population >= lower_bound) if not upper_bound else set(
            i for i in self.countries if upper_bound >= i.population >= lower_bound)


def main() -> None:
    repository = BasicCountryRepository('../../../data/countries.json')
    print(repository.get_countries_by_population(100, 200))


if __name__ == '__main__':
    main()
