from playground.queries import Exercises


class MyExcercises(Exercises):
    @staticmethod
    def odd_numbers_between(start: int, end: int) -> set[int]:
        return set(i for i in range(start, end + 1) if i % 2 == 1)

    @staticmethod
    def is_prime(number: int) -> bool:
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    @staticmethod
    def prime_numbers_between(start: int, end: int) -> set[int]:
        return set(i for i in range(start, end + 1) if MyExcercises.is_prime(i))

    @staticmethod
    def squares_between(start: int, end: int) -> dict[int, int]:
        return {i: i * i for i in range(start, end + 1)}

    @staticmethod
    def filter_primes(numbers: set[int]) -> set[int]:
        return set(i for i in numbers if MyExcercises.is_prime(i))


def main() -> None:
    print(MyExcercises.odd_numbers_between(10, 15))


if __name__ == '__main__':
    main()
