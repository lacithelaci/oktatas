
"""A tesztek célja általában az, hogy ellenőrizzék a kódunk működését, és biztosítsák, hogy a várt eredményeket kapjuk.
Ezeket a teszteket gyakran fejlesztés közben írjuk meg, hogy biztosak lehessünk abban, hogy a kódunk megfelelően működik. 
Az unittest modul segítségével Pythonban teszteket írhatunk, amelyek automatikusan futtathatók, és jelzik, ha valami nem úgy működik, ahogy kellene."""
import unittest

# Teszt az add_numbers függvényhez
def test_add_numbers():
    result = add_numbers(2, 3)
    assert result == 5

# Teszt az add metódushoz egy MathOperations osztályban
def test_add_method():
    # MathOperations osztály példányosítása
    math = MathOperations()
    # Az add metódus meghívása
    result = math.add(2, 3)
    assert result == 5

# Teszt a típusellenőrzéshez
def test_instance():
    # Egy integer típusú érték létrehozása
    value = 42
    # Ellenőrzés, hogy az érték integer típusú-e
    assert isinstance(value, int)

# Teszt az azonos objektumokra mutatás ellenőrzéséhez
def test_identity():
    # Egy lista létrehozása
    value1 = [1, 2, 3]
    # value2-nek ugyanarra az objektumra való hivatkozását beállítjuk, mint value1-nek
    value2 = value1
    # Ellenőrzés, hogy value1 és value2 ugyanarra az objektumra mutat-e
    assertIs(value1, value2)

# Teszt az érték benne lévőségének ellenőrzéséhez
def test_inclusion():
    # Egy lista létrehozása
    values = [1, 2, 3, 4]
    # Ellenőrzés, hogy a 3 benne van-e a listában
    assertIn(3, values)
