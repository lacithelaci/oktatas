def main():
    pass


def euklideszi(a, b, lnko):
    while b != 0:
        lnko = a
        a = b
        b = lnko % a

    return a


def k_euklideszi(a, b, d, x, y):
    x0 = 1
    x1 = 0
    y0 = 0
    y1 = 1
    s = 1
    while b != 0:
        r = a % b
        q = a // b
        a = b
        b = r
        x = x1
        y = y1
        x1 = q * x1 + x0
        y1 = q * y1 + y0
        x0 = x
        y0 = y
        s = -s
    x = s * x0
    y = (-s) * y0
    d, x, y = a, x, y
    return d, x, y


def gyorshatvany(alap, exp, mod):
    alap = alap % mod
    if exp == 0:
        return 1
    elif exp == 1:
        return alap
    elif exp % 2 == 0:
        return gyorshatvany((alap * alap) % mod, exp // 2, mod)
    return (alap * gyorshatvany(alap, exp - 1, mod)) % mod


def gyorshatvany2(a, k, m):
    res = 1
    a = a % m
    while k > 0:
        if k & 1 == 1:
            res = res * a % m

        k = k >> 1
        a = a ** a % m

    return res


if __name__ == '__main__':
    main()

print(euklideszi(5, 120, 1))
print(k_euklideszi(544, 119, 2, 1, 1))
print(gyorshatvany2(6, 73, 100))
