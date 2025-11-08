import random


# ===========================
# FŐ PROGRAM
# ===========================
def main():
    """
    Fő program, amely:
    1. Generál RSA kulcsokat a felhasználó által megadott bit hossz alapján.
    2. Titkosít és visszafejt egy számot.
    3. Digitális aláírást készít és ellenőriz.
    """

    print("RSA kulcsgenerálás folyamatban...")

    # --- Kulcsméret bekérése ---
    bits = int(input("Add meg a kulcsméretet bitben (pl. 512, 1024): "))
    half = bits // 2  # p és q kb. fele-fele legyen

    # --- 1. Két különböző prím generálása p és q ---
    while True:
        p = random.getrandbits(half)  # half bites random szám
        if miller_rabin(p):  # Miller-Rabin prímteszt
            break

    while True:
        q = random.getrandbits(half)
        if miller_rabin(q) and q != p:  # biztosítjuk, hogy p ≠ q
            break

    n = p * q  # RSA modulus
    phi = (p - 1) * (q - 1)  # Euler-függvény értéke φ(n)

    # --- 2. Nyílt kitevő (e) kiválasztása ---
    e = 65537  # Standard ajánlott érték RSA-hoz
    if e >= phi or euklideszi(e, phi) != 1:
        # Ha e nem jó, keresünk egy páratlan e-t
        e = 3
        while e < phi and euklideszi(e, phi) != 1:
            e += 2

    # --- 3. Titkos kitevő (d) számítása ---
    lnko, x, y = k_euklideszi(e, phi)  # kiterjesztett euklideszi algoritmus
    d = x % phi  # d ≡ e^-1 mod φ(n)

    # --- Kulcsok kiírása ---
    print("\n=== GENERÁLT RSA KULCSOK ===")
    print(f"p = {p}")
    print(f"q = {q}")
    print(f"n = {n}")
    print(f"φ(n) = {phi}")
    print(f"e = {e}")
    print(f"d = {d}")

    # ===========================
    # TITKOSÍTÁS / VISSZAFEJTÉS
    # ===========================
    message = int(input("\nAdj meg egy üzenetet számként titkosításhoz: "))
    print(f"Eredeti üzenet: {message}")

    # Titkosítás: c = m^e mod n
    c = gyorshatvany2(message, e, n)
    print(f"Titkosított üzenet: {c}")

    # Visszafejtés (CRT-vel, gyorsabb)
    m = kinai(c, d, p, q, n)
    print(f"Visszafejtett üzenet: {m}")

    # ===========================
    # DIGITÁLIS ALÁÍRÁS / ELLENŐRZÉS
    # ===========================
    print("\nDigitális aláírás teszt:")
    msg = int(input("Add meg az aláírandó üzenetet: "))

    # Aláírás készítése: sig = msg^d mod n (titkosított hash / üzenet)
    signature = kinai(msg, d, p, q, n)
    print(f"Aláírás (msg^d mod n): {signature}")

    # Ellenőrzés: sig^e mod n = eredeti üzenet
    check = gyorshatvany2(signature, e, n)
    print(f"Ellenőrzött üzenet (sig^e mod n): {check}")

    if check == msg:
        print("✅ Az aláírás érvényes!")
    else:
        print("❌ Az aláírás hibás!")


# ===========================
# SEGÉDFÜGGVÉNYEK
# ===========================

def euklideszi(a, b):
    """
    Klasszikus euklideszi algoritmus LNKO számításához.
    """
    while b != 0:
        a, b = b, a % b
    return a


def k_euklideszi(a, b):
    """
    Kiterjesztett euklideszi algoritmus.
    Visszaadja:
    d, x, y értékeket, ahol d = gcd(a, b), és x, y teljesítik:
    a*x + b*y = d
    """
    x0, x1 = 1, 0
    y0, y1 = 0, 1
    s = 1
    while b != 0:
        r = a % b
        q = a // b
        a, b = b, r
        x, y = x1, y1
        x1 = q * x1 + x0
        y1 = q * y1 + y0
        x0, y0 = x, y
        s = -s
    x = s * x0
    y = (-s) * y0
    d, x, y = a, x, y
    return d, x, y


def gyorshatvany(alap, exp, mod):
    """
    Rekurzív gyors hatványozás: alap^exp mod mod
    (nem túl nagy kitevő esetén, demonstrációs cél)
    """
    alap %= mod
    if exp == 0:
        return 1
    elif exp == 1:
        return alap
    elif exp % 2 == 0:
        return gyorshatvany((alap * alap) % mod, exp // 2, mod)
    return (alap * gyorshatvany(alap, exp - 1, mod)) % mod


def gyorshatvany2(a, k, m):
    """
    Iteratív gyors hatványozás: a^k mod m
    Nagy számokhoz és RSA-hoz ajánlott.
    """
    res = 1
    a %= m
    while k > 0:
        if k & 1:
            res = (res * a) % m
        a = (a * a) % m
        k >>= 1
    return res


def miller_rabin(n, k=10):
    """
    Miller-Rabin prímteszt.
    n: tesztelendő szám
    k: iterációk száma, növeli a pontosságot
    Visszaadja True-t, ha n valószínűleg prímszám, False-t, ha nem.
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    # n-1 = 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2

    for _ in range(k):
        a = random.randrange(2, n - 1)
        x = pow(a, d, n)
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
    """
    Kínai maradék tétel (CRT) használata RSA visszafejtéshez.
    Gyorsabb, mint sima m = c^d mod n.
    """
    c1 = gyorshatvany2(c, d % (p - 1), p)
    c2 = gyorshatvany2(c, d % (q - 1), q)
    lnko, x, y = k_euklideszi(p, q)
    m = (c1 * y * q + c2 * x * p) % n
    return m


# ===========================
# PROGRAM INDÍTÁS
# ===========================
if __name__ == '__main__':
    main()
