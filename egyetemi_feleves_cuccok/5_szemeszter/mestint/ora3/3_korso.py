from keres import *


class Korso(Feladat):

    def __init__(self, kezdő: tuple[int, int, int], cél: int):
        super().__init__(kezdő, cél)
        self.H = (3, 5, 8)

    def célteszt(self, állapot: tuple[int, int, int]) -> bool:
        if állapot[1] == 4 or állapot[2] == 4:
            return True
        return False

    def rákövetkező(self, állapot: tuple[int, int, int]) -> list[tuple[str, tuple[int, int, int]]]:
        lepesek = []
        for i in range(3):
            for j in range(3):
                if i != j:
                    m = min(állapot[i], self.H[j] - állapot[j])
                    if állapot[i] > 0 and állapot[j] < self.H[j]:
                        tmp_str = f'{i + 1} korsóból az {j + 1} korsóba {m} litert'
                        tmp_all = list(állapot)
                        for k in range(3):
                            if k == i:
                                tmp_all[k] -= m
                            elif k == j:
                                tmp_all[k] += m
                        lepesek.append((tmp_str, tuple(tmp_all)))
        return lepesek


k = Korso((0, 0, 8), 4)
csúcs = mélységi_fakeresés(k)
print(len(csúcs.út())-1)