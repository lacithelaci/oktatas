import random


def benne_van(betu, kivalasztott_szo) -> bool:
    return betu in kivalasztott_szo


def kirajzolo(kirajzolt, kivalasztott_szo, betu) -> str:
    return ''.join(k if k == b or k == betu else '-' for k, b in zip(kivalasztott_szo, kirajzolt))


def beolvas() -> list[str]:
    with open("szavak.txt", encoding="utf-8") as f:
        lista = [i.strip() for i in f]
    return lista


import random


def main() -> None:
    talalat = 1
    kivalasztott_szo = random.choice(beolvas())
    kirajzolt = '_' * len(kivalasztott_szo)
    print(f"A kitalálandó szó {len(kivalasztott_szo)} karakter hosszú: {kirajzolt}\n")

    while True:
        betu = input()
        if len(betu) > 1:
            if betu == kivalasztott_szo:
                print(f"Ügyes vagy, kitaláltad {talalat} próbálkozásból!\n")
            else:
                print(f"Sajnálom, vesztettél\nA kitalálandó szó nem volt más mint: {kivalasztott_szo}\n")
            break

        if benne_van(betu, kivalasztott_szo):
            kirajzolt = kirajzolo(kirajzolt, kivalasztott_szo, betu)

        print(kirajzolt + '\n')

        if kirajzolt == kivalasztott_szo:
            print(f"Ügyes vagy, kitaláltad {talalat} próbálkozásból!\n")
            break

        talalat += 1


if __name__ == '__main__':
    main()
