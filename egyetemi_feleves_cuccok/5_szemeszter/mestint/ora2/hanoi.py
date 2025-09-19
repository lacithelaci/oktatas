from typing import NamedTuple
from keres import *

Act = NamedTuple('Act', [('korong', int), ('rud', str)])


class Hanoi(Feladat):
    def __init__(self, n: int):
        super().__init__('1' * n, '3' * n)  # 111 -> 333

    def result(self, állapot: str, action: Act) -> str:
        korong, rud = action

        return állapot[0:korong] + rud + állapot[korong + 1:]  # 111 -> 3 -> 311
        # Ez a függvény alakítja át egyik állapotból a másikba az állapotunkat

    def rákövetkező(self, állapot: str) -> list[tuple[str, str]]:
        lepesek = []
        f1 = állapot.find('1')  # melyik koring a legkisebb az 1-es rúdon
        f2 = állapot.find('2')  # melyik koring a legkisebb az 2-es rúdon
        f3 = állapot.find('3')  # melyik koring a legkisebb az 3-as rúdon ha nincs, akkor -1

        if f1 > -1 and (f1 < f2 or f2 == -1):
            t = f'1. rúdrúl a {f1 + 1} korongot a 2. rúdra teszem.'
            act = Act(f1, '2')
            lepesek.append((t, self.result(állapot, act)))

        if f1 > -1 and (f1 < f3 or f3 == -1):
            t = f'1. rúdrúl a {f1 + 1} korongot a 3. rúdra teszem.'
            act = Act(f1, '3')
            lepesek.append((t, self.result(állapot, act)))

        if f2 > -1 and (f2 < f3 or f3 == -1):
            t = f'2. rúdrúl a {f1 + 1} korongot a 3. rúdra teszem.'
            act = Act(f2, '3')
            lepesek.append((t, self.result(állapot, act)))
        if f2 > -1 and (f2 < f1 or f1 == -1):
            t = f'2. rúdrúl a {f1 + 1} korongot a 1. rúdra teszem.'
            act = Act(f2, '1')
            lepesek.append((t, self.result(állapot, act)))
        if f3 > -1 and (f3 < f1 or f1 == -1):
            t = f'3. rúdrúl a {f1 + 1} korongot a 1. rúdra teszem.'
            act = Act(f3, '1')
            lepesek.append((t, self.result(állapot, act)))
        if f3 > -1 and (f3 < f2 or f2 == -1):
            t = f'3. rúdrúl a {f1 + 1} korongot a 2. rúdra teszem.'
            act = Act(f3, '2')
            lepesek.append((t, self.result(állapot, act)))

        return lepesek

    def célteszt(self, állapot):
        return super().célteszt(állapot)


H = Hanoi(3)

all = H.kezdő

while True:
    ls = H.rákövetkező(all)
    print(ls)
    i = int(input('Válassza ki a lépést'))
    all = ls[i - 1][1]
    if H.célteszt(all):
        print(all)
        break

