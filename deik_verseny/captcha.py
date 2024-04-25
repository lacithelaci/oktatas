def hibakereso_max_5(helyes, bekert):
    db = 0
    for i in range(len(helyes)):
        if helyes[i].lower() in ["c", "k", "s", "v", "y", "e", "o", "t", "w", "z", "f", "p", "u", "x", "l"]:
            if helyes[i].lower() != bekert[i].lower():
                db += 1
        else:
            if helyes[i] != bekert[i]:
                db += 1

    if db != 0:
        return f"WRONG {db}"
    else:
        return f"Right 0"


def hibakereso_min_6(helyes, bekert):
    db = 0
    for i in range(len(helyes)):
        if helyes[i].lower() in ["c", "k", "s", "v", "y", "e", "o", "t", "w", "z", "f", "p", "u", "x", "l"]:
            if helyes[i].lower() != bekert[i].lower():
                db += 1
        else:
            if helyes[i] != bekert[i]:
                db += 1

    if db > 2:
        return f"WRONG {db}"
    else:
        return f"Right {db}"


while True:
    try:
        a = input().split()
        if len(a[0]) <= 5:
            print(hibakereso_max_5(a[0], a[1]))
        else:
            print(hibakereso_min_6(a[0], a[1]))
    except EOFError:
        break
    except IndexError:
        break
