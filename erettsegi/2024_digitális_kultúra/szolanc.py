def main() -> None:
    db = 1
    elozo = None
    while True:
        a = input(f"{db}. szó: ")
        if db > 1 and a[0] != elozo[-1]:
            print("Nem illeszkedett!")
            break
        elif len(a) != 6:
            print("A karakterek száma téves!")
            break
        db += 1
        elozo = a

    print("Helyes lépések száma:", db - 1)
    if db - 1 <= 2:
        print("Szint: kezdő")
    elif db - 1 <= 5:
        print("Szint: közepes")
    else:
        print("Szint: haladó")


if __name__ == '__main__':
    main()
