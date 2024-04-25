"""
Ez a rész arról szól, hogyan készíthetünk és elemezhetünk olyan kódrészleteket,
amelyek ismétlődő tevékenységeket hajtanak végre. A Pythonban az iteráció azt jelenti,
hogy bizonyos utasításokat többször ismételünk meg. Ennek különböző módjai lehetnek,
mint például a while és for ciklusok, melyek segítségével ismételt műveleteket hajtunk végre addig,
amíg bizonyos feltétel teljesül vagy egy adott iterálható elem összesen feldolgozásra kerül.
Ezenkívül az iterációs folyamatot tovább befolyásolják különféle vezérlőutasítások,
mint például a break, continue, pass, amelyek lehetővé teszik a ciklusok futásának
szabályozását vagy az iterációs folyamat megszakítását bizonyos feltételek alapján.
Emellett az egymásba ágyazott (nested) ciklusok is fontosak, amikor egy ciklus másik ciklussal van beágyazva,
valamint az összetett feltételes kifejezések használata is előfordulhat a ciklusokban,
ami összetettebb logikai vizsgálatokat tesz lehetővé az iteráció során.
"""
# while ciklus példa
counter = 0
while counter < 5:
    print(f"A ciklus értéke: {counter}")
    counter += 1

# for ciklus példa
fruits = ["alma", "körte", "banán"]
for fruit in fruits:
    print(f"Gyümölcs: {fruit}")

# break és continue példa
for i in range(10):
    if i == 3:
        print("Az iteráció megáll a 'break' utasításnál.")
        break
    if i == 5:
        print("Az iteráció 'continue' utasításnál folytatódik.")
        continue
    print(f"A ciklus értéke: {i}")

# pass példa
for letter in 'Python':
    if letter == 'h':
        pass
        print('Ez a "pass" utasításnál van')
    print('Aktuális betű:', letter)