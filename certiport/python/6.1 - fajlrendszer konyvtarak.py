"""
Alapvető fájlrendszer- és parancssor-műveletek végrehajtása a beépített Python modulok használatával.
"""
import io
import os
import os.path
import sys
# Írás és olvasás StringIO objektumból
string_io = io.StringIO()
string_io.write('Ez egy példa szöveg.')
string_io.seek(0)
content = string_io.read()
print(content)

# Jelenlegi munkakönyvtár lekérdezése
current_directory = os.getcwd()
print("Jelenlegi munkakönyvtár:", current_directory)

# Új könyvtár létrehozása
new_directory = "új_könyvtár"
os.makedirs(new_directory)

# Ellenőrzés, hogy a fájl létezik-e
file_path = 'valamilyen_fajl.txt'
exists = os.path.exists(file_path)
if exists:
    print(f"A '{file_path}' fájl létezik.")
else:
    print(f"A '{file_path}' fájl nem létezik.")
import sys

# Parancssori argumentumok kezelése
arguments = sys.argv
if len(arguments) > 1:
    print("Parancssori argumentumok:")
    for arg in arguments[1:]:
        print(arg)
else:
    print("Nincsenek parancssori argumentumok.")
