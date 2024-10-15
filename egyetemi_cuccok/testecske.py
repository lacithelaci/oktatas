import sys

from prog2.zoo import Zoo, Emlos


def main() -> None:
    lista = []
    try:
        for i in range(int(sys.argv[1])):
            a = input().split(";")
            if len(a) == 3:
                lista.append(Zoo(a[0], float(a[2]), float(a[1])))
            if len(a) == 4:
                lista.append(Emlos(a[0], float(a[2]), int(a[3]), float(a[1])))
        lista.sort()
        for i in lista:
            print(i)
    except IndexError:
        print("Hiányzó parancssori argumentum")
    except ValueError:
        print("Értékhiba")


if __name__ == '__main__':
    main()
