from countries.base.model import Country
from countries.base.queries import AggregationCountryQueries
from countries.base.repository import CountryRepository


class AggregationCountryRepository(CountryRepository, AggregationCountryQueries):

    def get_countries_by_codes(self) -> dict[str, Country]:
        return {country.code: country for country in self.countries}

    def get_count_of_countries_by_regions(self) -> dict[Country.Region, int]:
        return {region: len([country.region for country in self.countries if country.region == region]) for region in
                {country.region for country in self.countries}}

    def get_countries_by_regions(self) -> dict[Country.Region, set[Country]]:
        return {region: {country for country in self.countries if country.region == region} for region in
                {country.region for country in self.countries}}

    def get_most_populous_country_by_regions(self) -> dict[Country.Region, Country]:
        return {region: next(country for country in self.countries if
                             country.region == region and country.population == max(
                                 {country.population for country in self.countries if country.region == region})) for
                region in {country.region for country in self.countries}}

    def get_countries_by_regions_order_by_capitals(self) -> dict[Country.Region, list[Country]]:
        return {region: sorted([i for i in self.countries if i.region == region], key=lambda i: i.capital) for region
                in {country.region for country in self.countries}}

    def get_countries_by_regions_filter_by_population(self, lower_bound: int, upper_bound: int) -> dict[
        Country.Region, set[Country]]:
        return {region: {i for i in self.countries if lower_bound <= i.population <= upper_bound} for region in
                {country.region for country in self.countries}}

    def get_countries_by_regions_and_codes(self) -> dict[Country.Region, dict[str, Country]]:
        return {region: {i.code: i for i in self.countries} for region in
                {country.region for country in self.countries}}

    def get_countries_by_regions_and_first_letters(self):
        return {
            region: {
                letter: [
                    country
                    for country in self.countries
                    if country.region == region and country.name[0] == letter
                ]
                for letter in {
                    country.name[0]
                    for country in self.countries
                    if country.region == region
                }
            }
            for region in {
                country.region
                for country in self.countries
            }
        }

    def get_countries_by_first_letters_and_regions(self):
        return {
            letter: {
                region: [
                    country
                    for country in self.countries
                    if country.region == region and country.name[0] == letter
                ]
                for region in {
                    country.region
                    for country in self.countries
                    if country.name[0] == letter
                }
            }
            for letter in {
                country.name[0]
                for country in self.countries
            }
        }

    def get_localized_country_names_by_regions(self, locale: str) -> dict[Country.Region, set[str]]:
        return {
            region: {
                country.translations[locale]
                for country in self.countries
                if country.region == region
            }
            for region in {
                country.region
                for country in self.countries
            }
        }

    def get_first_localized_country_names_by_regions(self, locale: str) -> dict[Country.Region, str]:
        return {
            region: next(
                country.name
                for country in self.countries
                if country.region == region and locale in country.translations
            )
            for region in {
                country.region
                for country in self.countries
            }
        }

    def get_first_localized_countries_by_regions(self, locale: str) -> dict[Country.Region, Country]:
        return {
            region: next(
                country
                for country in self.countries
                if country.region == region and locale in country.translations
            )
            for region in {
                country.region
                for country in self.countries
            }
        }


def main():
    repository = AggregationCountryRepository('../../../data/countries.json')
    print(repository.get_first_localized_countries_by_regions('hu'))


if __name__ == '__main__':
    main()
