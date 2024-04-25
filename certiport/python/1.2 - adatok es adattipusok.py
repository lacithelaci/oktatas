"""
Adattípus átalakítás: Adott típusú adatok átkonvertálása más típusú adatokká, például számokat stringgé alakítani vagy stringeket számmá alakítani.
Indexelés és szeletelés: Az adatok elemének vagy részének hozzáférése az indexük alapján, illetve az adatok részeinek vágása (szeletelése).
Adatszerkezetek létrehozása: Különböző adatszerkezetek, például listák létrehozása, amelyek lehetnek változtatható
és tetszőleges típusú elemeket tartalmaznak.
Lista műveletek: Listákkal végzett műveletek, mint például rendezés, összefűzés más listákkal,
új elemek hozzáadása vagy beszúrása, meglévő elemek eltávolítása, maximum és minimum keresése, valamint lista megfordítása.
"""
# Adattípus átalakítás
number_as_string = "123"
number = int(number_as_string)
print("Szám stringből int típusúvá alakítva:", number)

# Indexelés és szeletelés
my_string = "Hello, World!"
print("A string első karaktere:", my_string[0])
print("A string utolsó 5 karaktere:", my_string[-5:])

# Adatszerkezetek létrehozása (lista)
my_list = [1, 5, 2, 7, 4]
print("Eredeti lista:", my_list)

# Lista műveletek
my_list.sort()  # rendezés
print("Rendezett lista:", my_list)

my_list.append(10)  # hozzáadás
print("Elem hozzáadva a listához:", my_list)

my_list.remove(2)  # eltávolítás
print("Elem eltávolítva a listából:", my_list)

max_value = max(my_list)  # maximum keresése
min_value = min(my_list)  # minimum keresése
print("Maximum érték:", max_value)
print("Minimum érték:", min_value)

my_list.reverse()  # megfordítás
print("Megfordított lista:", my_list)