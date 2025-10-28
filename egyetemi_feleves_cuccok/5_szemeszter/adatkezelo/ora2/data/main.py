import oracledb
from basic.handler import sql
from ora2.data.basic.model_dataclasses import Car, Airport, Person
from ora2.data.basic.generator import generate_people, generate_cars, generate_airports


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


# --- Főprogram ---
def main():
    connection = get_connection()

    # Tesztadatok
    people = generate_people(100)

    cars = generate_cars(100)

    airports = generate_airports(100)

    print("\n--- 👩‍🦰 People teszt ---")
    sql.write_people(people, connection)
    print("Beolvasva:", sql.read_people(connection))

    print("\n--- 🚗 Cars teszt ---")
    sql.write_cars(cars, connection)
    print("Beolvasva:", sql.read_cars(connection))

    print("\n--- 🛫 Airports teszt ---")
    sql.write_airports(airports, connection)
    print("Beolvasva:", sql.read_airports(connection))

    print("\n--- 🔁 Általános write/read ---")
    sql.write(people, connection, table_name="people_copy")
    print("People copy:", sql.read(Person, connection, table_name="people_copy"))

    connection.close()
    print("\n✅ Program vége – kapcsolat lezárva.")


if __name__ == "__main__":
    main()
