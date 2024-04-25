"""
Ez a rész arról szól, hogy hogyan hozhatunk létre és vizsgálhatunk olyan kódrészleteket,
amelyek függvények definiálását tartalmazzák Pythonban.
A függvénydefiníciók magukban foglalják a hívási aláírásokat (azaz a függvény paramétereit és azok típusait),
alapértelmezett értékeket a paraméterek számára, valamint a visszatérési értéket, amelyet a függvény visszaad.
A def kulcsszó használata a függvények definiálására szolgál, míg a pass utasítás lehetővé teszi,
 hogy üresen hagyjuk egy függvény testét anélkül, hogy hibát generálnánk.
"""
# Függvény definíció alapértelmezett értékekkel
def greet(name="Vendég"):
    print(f"Hello, {name}!")

# Függvény hívása alapértelmezett értékkel
greet()  # Kimenet: Hello, Vendég!
greet("John")  # Kimenet: Hello, John!
# Függvény definíció visszatérési értékkel
def add(a, b):
    return a + b

# Függvény hívása és visszatérési értékének felhasználása
result = add(5, 3)
print(f"Az összeg: {result}")  # Kimenet: Az összeg: 8
# Függvény definíció a pass utasítással
def my_function():
    pass  # Ebben a függvényben nincs művelet definiálva

# Függvény hívása, amely üresen marad
my_function()
