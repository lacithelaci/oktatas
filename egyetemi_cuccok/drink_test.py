import sys

from prog2.drink import Drink, Szeszesital


def main() -> None:
    lista = []
    try:
        for i in range(int(sys.argv[1])):
            a = input().split(";")
            if len(a) == 3:
                lista.append(Drink(a[0], int(a[2]), a[1]))
            if len(a) == 4:
                lista.append(Szeszesital(a[0], int(a[2]), float(a[3]), a[1]))
        lista.sort()
        for i in lista:
            print(i)
    except IndexError:
        print("Hiányzó parancssori argumentum")
    except ValueError:
        print("Értékhiba")


if __name__ == '__main__':
    main()
