import random


def main():
    # === KULCSGENERÁLÁS ===
    print("RSA kulcsgenerálás folyamatban...")

    # 1. Két különböző prím
    while True:
        p = random.randint(50, 200)
        if miller_rabin(p):
            break
    while True:
        q = random.randint(50, 200)
        if miller_rabin(q) and q != p:
            break
    
    '''
    hány bites randomot generáljak
    '''

    n = p * q
    phi = (p - 1) * (q - 1)

    # 2. Nyílt kitevő (e)
    e = 13
    if e >= phi or euklideszi(e, phi) != 1:
        # ha nem jó, keresünk másikat
        e = 3
        while e < phi and euklideszi(e, phi) != 1:
            e += 2

    # 3. Titkos kitevő (d)
    lnko, x, y = k_euklideszi(e, phi)
    d = x % phi

    print(f"p = {p}, q = {q}")
    print(f"n = {n}")
    print(f"φ(n) = {phi}")
    print(f"e = {e}")
    print(f"d = {d}")

    # === TITKOSÍTÁS / VISSZAFEJTÉS ===
    message = 85
    print(f"\nEredeti üzenet: {message}")

    # titkosítás: c = m^e mod n
    c = gyorshatvany2(message, e, n)
    print(f"Titkosított üzenet: {c}")

    # visszafejtés (CRT-vel)
    m = kinai(c, d, p, q, n)
    print(f"Visszafejtett üzenet: {m}")

    # === ALÁÍRÁS / ELLENŐRZÉS ===
    print("\nDigitális aláírás teszt:")
    msg = 47
    signature = kinai(msg, d, p, q, n)
    print(f"Aláírás: {signature}")

    check = gyorshatvany2(signature, e, n)
    print(f"Ellenőrzött üzenet: {check}")

    if check == msg:
        print("Az aláírás érvényes!")
    else:
        print("Az aláírás hibás!")


def euklideszi(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def k_euklideszi(a, b):
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
        if k & 1:
            res = (res * a) % m
        a = (a * a) % m
        k >>= 1
    return res


def miller_rabin(n, k=10):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # n-1 = 2^r * d, ahol d páratlan
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)  # a^d mod n

        if x == 1 or x == n - 1:
            continue

        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


def kinai(c, d, p, q, n):
    c1 = gyorshatvany2(c, d % (p - 1), p)
    c2 = gyorshatvany2(c, d % (q - 1), q)

    lnko, x, y = k_euklideszi(p, q)

    m = (c1 * y * q + c2 * x * p) % n
    return m


if __name__ == '__main__':
    main()

'''
print(euklideszi(5, 120, 1))
print(k_euklideszi(544, 119))
print(gyorshatvany2(6, 73, 100))
print(miller_rabin(13))  # True (prím)
print(miller_rabin(111))  # False (nem prím)
print(kinai(85, 47, 7, 13, 91))
'''
