from __future__ import annotations

from dataclasses import field, dataclass
from enum import Enum


@dataclass
class Country:
    """
    Represents a country.
    """

    name: str = field(compare=False)
    """name of the country"""
    code: str = field(hash=True)
    """code of the country"""
    population: int = field(compare=False)
    """population of the country"""
    translations: dict[str, str] = field(compare=False)
    """translations of the name"""
    timezones: list[str] = field(compare=False)
    """timezones of the country"""
    independent: bool = field(compare=False)
    """whether the country is independent or not"""
    area: int = field(compare=False, default=None)
    """area of the country"""
    capital: str = field(compare=False, default='')
    """capital of the country"""
    region: Region = field(compare=False, default=None)
    """region of the country"""

    def __hash__(self):
        return hash(self.code)  # Hash számítása csak a code alapján

    class Region(Enum):
        """
        Represents regions.

        * AFRICA = "Africa"
        * AMERICAS = "Americas"
        * ANTARCTIC = "Antarctic"
        * ANTARCTIC_OCEAN = "Antarctic Ocean"
        * ASIA = "Asia"
        * EUROPE = "Europe"
        * OCEANIA = "Oceania"
        * POLAR = "Polar"
        """
        AFRICA = "Africa"
        AMERICAS = "Americas"
        ANTARCTIC = "Antarctic"
        ANTARCTIC_OCEAN = "Antarctic Ocean"
        ASIA = "Asia"
        EUROPE = "Europe"
        OCEANIA = "Oceania"
        POLAR = "Polar"
