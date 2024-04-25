import unittest


def add_numbers(a, b):
    return a + b


def test_add_numbers():
    result = add_numbers(2, 3)
    assert result == 5


def test_add_method():
    math = MathOperations()
    result = math.add(2, 3)
    assert result == 5


def test_instance():
    value = 42
    assert isinstance(value, int)

def test_identity():
    value1 = [1, 2, 3]
    value2 = value1
    assertIs(value1, value2)

def test_inclusion():
    values = [1, 2, 3, 4]
    assertIn(3, values)