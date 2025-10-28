import oracledb
from ora2.data.basic.model_dataclasses import Person, Car, Airport


# -----------------------
# People
# -----------------------
def write_people(people: list[Person], connection, table_name: str = "people") -> None:
    cursor = connection.cursor()
    try:
        cursor.execute(f"DROP TABLE {table_name} PURGE")
    except oracledb.DatabaseError:
        print(f"ℹ️ Tábla '{table_name}' nem létezett, létrehozás folytatódik.")
        pass

    cursor.execute(f"""
        CREATE TABLE {table_name} (
            ID VARCHAR2(10) PRIMARY KEY,
            NAME VARCHAR2(50),
            AGE NUMBER(3),
            MALE NUMBER(1)
        )
    """)

    cursor.executemany(
        f"INSERT INTO {table_name} (id, name, age, male) VALUES (:1, :2, :3, :4)",
        [(p.id, p.name, p.age, int(p.male)) for p in people]
    )
    connection.commit()


def read_people(connection, table_name: str = "people") -> list[Person]:
    cursor = connection.cursor()
    cursor.execute(f"SELECT id, name, age, male FROM {table_name}")
    rows = cursor.fetchall()
    return [Person(id=r[0], name=r[1], age=r[2], male=bool(r[3])) for r in rows]


# -----------------------
# Cars
# -----------------------
def write_cars(cars: list[Car], connection, table_name: str = "cars") -> None:
    cursor = connection.cursor()
    try:
        cursor.execute(f"DROP TABLE {table_name} PURGE")
    except oracledb.DatabaseError:
        print(f"ℹ️ Tábla '{table_name}' nem létezett, létrehozás folytatódik.")
        pass

    cursor.execute(f"""
        CREATE TABLE {table_name} (
            PLATE VARCHAR2(10) PRIMARY KEY,
            TYPE VARCHAR2(50),
            YEAR NUMBER(4),
            AUTOMATIC NUMBER(1)
        )
    """)

    cursor.executemany(
        f"INSERT INTO {table_name} (plate, type, year, automatic) VALUES (:1, :2, :3, :4)",
        [(c.plate, c.type, c.year, int(c.automatic)) for c in cars]
    )
    connection.commit()


def read_cars(connection, table_name: str = "cars") -> list[Car]:
    cursor = connection.cursor()
    cursor.execute(f"SELECT plate, type, year, automatic FROM {table_name}")
    rows = cursor.fetchall()
    return [Car(plate=r[0], type=r[1], year=r[2], automatic=bool(r[3])) for r in rows]


# -----------------------
# Airports
# -----------------------
def write_airports(airports: list[Airport], connection, table_name: str = "airports") -> None:
    # Kiszűrjük a duplikált repülőtereket
    seen = set()
    unique_airports = []
    for airport in airports:
        if airport.code not in seen:
            unique_airports.append(airport)
            seen.add(airport.code)

    # Most az 'airports' lista az egyedi repülőtereket tartalmazza
    airports = unique_airports

    cursor = connection.cursor()
    try:
        cursor.execute(f"DROP TABLE {table_name} PURGE")
    except oracledb.DatabaseError:
        print(f"ℹ️ Tábla '{table_name}' nem létezett, létrehozás folytatódik.")
        pass

    cursor.execute(f"""
        CREATE TABLE {table_name} (
            CODE VARCHAR2(10) PRIMARY KEY,
            NAME VARCHAR2(100),
            CITY VARCHAR2(50),
            STATE VARCHAR2(50),
            COUNTRY VARCHAR2(50)
        )
    """)

    cursor.executemany(
        f"INSERT INTO {table_name} (code, name, city, state, country) VALUES (:1, :2, :3, :4, :5)",
        [(a.code, a.name, a.city, a.state, a.country) for a in airports]
    )
    connection.commit()


def read_airports(connection, table_name: str = "airports") -> list[Airport]:
    cursor = connection.cursor()
    cursor.execute(f"SELECT code, name, city, state, country FROM {table_name}")
    rows = cursor.fetchall()
    return [Airport(code=r[0], name=r[1], city=r[2], state=r[3], country=r[4]) for r in rows]


# -----------------------
# Általános write/read (dataclass alapú) - javított
# -----------------------
def write(items: list, connection, table_name: str):
    if not items:
        return

    cls = type(items[0])
    fields = [f.name for f in cls.__dataclass_fields__.values()]

    cursor = connection.cursor()
    try:
        cursor.execute(f"DROP TABLE {table_name} PURGE")
    except oracledb.DatabaseError:
        pass

    # oszlopok létrehozása a dataclass típusainak megfelelően
    columns = []
    for f in cls.__dataclass_fields__.values():
        if f.type == int or f.type == bool:
            columns.append(f"{f.name.upper()} NUMBER")
        else:
            columns.append(f"{f.name.upper()} VARCHAR2(100)")
    cursor.execute(f"CREATE TABLE {table_name} ({', '.join(columns)})")

    # insert
    values = []
    for i in items:
        row = []
        for f in fields:
            val = getattr(i, f)
            if isinstance(val, bool):
                val = int(val)  # bool -> 0/1
            row.append(val)
        values.append(row)

    placeholders = ", ".join([f":{n + 1}" for n in range(len(fields))])
    cursor.executemany(
        f"INSERT INTO {table_name} ({', '.join([f.upper() for f in fields])}) VALUES ({placeholders})",
        values
    )
    connection.commit()


def read(cls, connection, table_name: str):
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    fields = [f.name for f in cls.__dataclass_fields__.values()]
    types = [f.type for f in cls.__dataclass_fields__.values()]
    result = []

    for r in rows:
        kwargs = {}
        for i, field_name in enumerate(fields):
            value = r[i]
            if value is not None:
                if types[i] == int:
                    value = int(value)
                elif types[i] == bool:
                    value = bool(int(value))
            kwargs[field_name] = value
        result.append(cls(**kwargs))

    return result

# --- Oracle kapcsolat létrehozása ---
def get_connection():
    # Saját Oracle belépési adataid
    user = "U_NEPTONKÓD"
    password = "jelszó"
    dsn = "codd.inf.unideb.hu:1521/ora21cp.inf.unideb.hu"

    print("🔌 Kapcsolódás az Oracle szerverhez (oracledb)...")
    connection = oracledb.connect(user=user, password=password, dsn=dsn)
    print("✅ Oracle kapcsolat sikeres!")
    return connection
