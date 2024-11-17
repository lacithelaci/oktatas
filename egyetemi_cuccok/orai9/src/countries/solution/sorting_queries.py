from countries.base.model import Country
from countries.base.queries import SortingCountryQueries
from countries.base.repository import CountryRepository


class SortingCountryRepository(CountryRepository, SortingCountryQueries):
    def get_countries_order_by_population_desc(self) -> list[Country]:
        return sorted(self.countries, key=lambda i: -i.population)

    def get_countries_order_by_length_of_capital_then_by_population_desc(self) -> list[Country]:
        return sorted(self.countries, key=lambda country: (len(country.capital), -country.population))

    def get_countries_order_by_length_of_capital_then_by_capital(self) -> list[Country]:
        return sorted(self.countries, key=lambda country: (len(country.capital), country.capital))

    def get_capitals_order_by_name_desc(self) -> list[str]:
        return [country.capital for country in
                sorted(self.countries, key=lambda country: country.capital, reverse=True)]


def main() -> None:
    repository = SortingCountryRepository('../../../data/countries.json')
    print(repository.get_capitals_order_by_name_desc())


if __name__ == '__main__':
    main()
