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


def main2() -> None:
    lista = []
    while True:
        try:
            a = input().split(";")
            if len(a) == 3:
                lista.append(Drink(a[0], int(a[2]), a[1]))
            if len(a) == 4:
                lista.append(Szeszesital(a[0], int(a[2]), float(a[3]), a[1]))
        except EOFError:
            break

    lista.sort()
    for i in lista:
        print(i)


def main3() -> None:
    lista = []
    while True:
        a = input().split(";")
        if int(a[2]) <= 0:
            break
        if len(a) == 3:
            lista.append(Drink(a[0], int(a[2]), a[1]))
        if len(a) == 4:
            lista.append(Szeszesital(a[0], int(a[2]), float(a[3]), a[1]))

    lista.sort()
    for i in lista:
        print(i)


def main4():
    lista = []
    while True:
        a = input().split(";")
        if int(sys.argv[1]) < int(a[2]):
            break
        if len(a) == 3:
            lista.append(Drink(a[0], int(a[2]), a[1]))
        if len(a) == 4:
            lista.append(Szeszesital(a[0], int(a[2]), float(a[3]), a[1]))

    lista.sort()
    for i in lista:
        print(i)


def main5():
    lista = []
    with open(f"{sys.argv[1]}",encoding="utf-8") as f:
        for a in f:
            a = a.split(";")
            if len(a) == 3:
                lista.append(Drink(a[0], int(a[2]), a[1]))
            if len(a) == 4:
                lista.append(Szeszesital(a[0], int(a[2]), float(a[3]), a[1]))
    lista.sort()
    for i in lista:
        print(i)


if __name__ == '__main__':
    main5()
