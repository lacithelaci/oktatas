import sys
from seged import *


class Feladat:

    def __init__(self, kezdő, cél=None):
        self.kezdő = kezdő
        self.cél = cél

    def rákövetkező(self, állapot):
        raise NotImplementedError

    def célteszt(self, állapot):
        return állapot == self.cél
        # raise NotImplementedError

    def érték(self):
        raise NotImplementedError

    def útköltség(self, c, állapot1, lépés, állapot2):
        return c + 1


class Csúcs:

    def __init__(self, állapot, szülő=None, lépés=None, útköltség=0):
        self.állapot = állapot
        self.szülő = szülő
        self.lépés = lépés
        self.útköltség = útköltség
        if szülő:
            self.mélység = szülő.mélység + 1
        else:
            self.mélység = 0

    def __repr__(self):
        return "<Csúcs: %s>" % (self.állapot,)

        # return "%s" % (list(self.állapot),)

    def út(self):
        x, válasz = self, [self]
        while x.szülő:
            válasz.append(x.szülő)
            x = x.szülő
        return válasz

    def megoldás(self):
        utam = self.út()
        utam.reverse()
        return [csúcs.lépés for csúcs in utam[1:]]

    def kiterjeszt(self, feladat):
        for (művelet, következő) in feladat.rákövetkező(self.állapot):
            if következő not in [csúcs.állapot for csúcs in self.út()]:
                yield Csúcs(következő, self, művelet,
                            feladat.útköltség(self.útköltség, self.állapot, művelet,
                                              következő))


def fakeresés(feladat, perem) -> Csúcs:
    global meglátogatott_csúcsok
    perem.append(Csúcs(feladat.kezdő))
    while perem:
        meglátogatott_csúcsok += 1;
        csúcs = perem.pop()
        if feladat.célteszt(csúcs.állapot):
            return csúcs
        perem.extend(csúcs.kiterjeszt(feladat))
    return None


def szélességi_fakeresés(feladat):
    return fakeresés(feladat, Sor())


def mélységi_fakeresés(feladat):
    return fakeresés(feladat, Verem())


# ezt érdemes tudni
def gráfkeresés(feladat, perem):
    global meglátogatott_csúcsok
    zárt = set()
    perem.append(Csúcs(feladat.kezdő))
    while perem:
        meglátogatott_csúcsok += 1;
        csúcs = perem.pop()
        if feladat.célteszt(csúcs.állapot):
            return csúcs
        if csúcs.állapot not in zárt:
            zárt.add(csúcs.állapot)
            perem.extend(csúcs.kiterjeszt(feladat))
    return None


def szélességi_gráfkeresés(feladat):
    return gráfkeresés(feladat, Sor())


def mélységi_gráfkeresés(feladat):
    return gráfkeresés(feladat, Verem())


def best_first(feladat, f):
    return gráfkeresés(feladat, RendezettLista(f))


def a_csillag(feladat, h):
    def f(n):
        return n.útköltség + h(n)

    return best_first(feladat, f)


def csúcsok_statisztika():
    global meglátogatott_csúcsok
    tmp = meglátogatott_csúcsok
    meglátogatott_csúcsok = 0
    return tmp


meglátogatott_csúcsok = 0;
