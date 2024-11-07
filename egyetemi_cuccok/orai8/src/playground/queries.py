from abc import ABC, abstractmethod


class Exercises(ABC):
    """
    Defines exercises that deal with integers.
    """

    @staticmethod
    @abstractmethod
    def odd_numbers_between(start: int, end: int) -> set[int]:
        """
        Returns the set of odd integers between start and end (inclusive).

        :param start: the start of the interval
        :param end: the end of the interval
        :return: the set of odd integers
        """

    @staticmethod
    @abstractmethod
    def is_prime(number: int) -> bool:
        """
        Returns whether the given number is prime or not.

        :param number: the number
        :return: the result
        """

    @staticmethod
    @abstractmethod
    def prime_numbers_between(start: int, end: int) -> set[int]:
        """
        Returns the set of prime integers between start and end (inclusive).

        :param start: the start of the interval
        :param end: the end of the interval
        :return: the set of odd integers
        """

    @staticmethod
    @abstractmethod
    def squares_between(start: int, end: int) -> dict[int, int]:
        """
        Returns a dictionary which maps the integers of interval [start, end] to their squares.

        :param start: the start of the interval
        :param end: the end of the interval
        :return: the integers and their squares
        """

    @staticmethod
    @abstractmethod
    def filter_primes(numbers: set[int]) -> set[int]:
        """
        Returns a set which contains the prime integers of the given set.

        :param numbers: the integers
        :return: the prime integers
        """
