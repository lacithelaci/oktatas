"""
Az "4.1 Document code segments" rész Pythonban arról szól, hogy hogyan dokumentáljuk a kódrészleteket.
Ennek részeként fontos a megfelelő behúzás, szóközök és kommentek használata a kódban,
hogy az könnyen érthető legyen más fejlesztők számára. A docstrings vagy dokumentációs karakterláncok használata szintén
elengedhetetlen, mivel ezek a részletes leírások segítik a kód értelmezését és a modulok, függvények vagy osztályok működésének dokumentálását.
Ezenkívül a pydoc segítségével generálhatunk dokumentációt a Python kódunkból,
ami könnyen hozzáférhetővé és értelmezhetővé teszi azokat más fejlesztők vagy a dokumentációt
olvasó személyek számára. A jó dokumentáció növeli a kód érthetőségét és karbantarthatóságát,
segítve ezzel a kód hosszú távú fejlesztését és karbantartását.
"""
def factorial(n):
    """
    Calculate the factorial of a number.

    Args:
    n (int): The integer to calculate the factorial for.

    Returns:
    int: The factorial of the input integer.
    """
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
    #linuxban érdemes kipróbálni