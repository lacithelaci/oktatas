import copy
from operator import neg
from utils import first
from utils import count
from utils import argmin_random_tie
from problem import Problem
from collections import defaultdict
from sortedcontainers import SortedSet


# ---------------------------------------------------------------------------
# -------------------------- KÉNYSZERKIELÉGÍTÉS -----------------------------
# ---------------------------------------------------------------------------

class CSP(Problem):
    """Ez az osztály leír egy véges tartományú kénszerkielégítéses problémát.
    A CSP a következő bemeneti argumentumokkal rendelkezik
        variables   A változók listája; mindegyik atomi (pl. int vagy string).
        domains     Egy szótár objektum a bejegyzések tárolására {var:[possible_value, ...]}.
        neighbors   Egy szótár objektum {var:[var,...]}, amely minden változóhoz listázza
                    a többi változót, amely részt vesz a megszorításokban.
        constraints Egy függvény f(A, a, B, b) ami true (igaz) értéket ad vissza
                    ha a szómszédok (A és B) kielégiíté a megszórítást azaz A=a, B=b
    A legtöbb matematikai definícióban a megszorítások a megengedett értékek explicit párjaként vannak megadva,
    de a megfogalmazás könnyebben is kifejezhető és a legtöbb esetben tömörebb.
    Az osztály támogatja azokat az adatstruktúrákat és metódusokat is, amelyek segítenek a kényszerkielégítéses probléma
    megoldásában egy keresési függvény meghívásával a CSP-n. A metódusokban, ahol az 'a' argumentum egy hozzárendelést jelent,
    amely 'a' {var:val} bejegyzések szótára:
        assign(var, val, a)     a[var] = val; értékadás
        unassign(var, a)        a[var]; értéktörlés
        nconflicts(var, val, a) A var=val paraméterrel ütköző egyéb változók
                                számát adja vissza
        curr_domains[var]       Slot: a var fenmaradó értékei.
                                A megszoritó rutinok használják.
    A következő metódusokat csak a graph_search és a tree_search használja:
        actions(state)          Visszatér a műveletek listáját.
        result(state, action)   Visszatér a cselekvés hatására előálló állapottal
        goal_test(state)        Visszatér igazzal ha az összes megszorítás kielégíthető
    Az alábbiak csak hibakeresési célokat szolgálnak:
        nassigns                Slot: nyomon követi a végrehajtott feladatok számát
        display(a)              Megjelenítés ember által olvasható formában
    """

    def __init__(self, variables, domains, neighbors, constraints):
        """Kényszerkielégítési probléma konstruktora. Ha a változók üresek, akkor domains.keys() lista lesz. """
        super().__init__(())
        variables = variables or list(domains.keys())
        self.variables = variables
        self.domains = domains
        self.neighbors = neighbors
        self.constraints = constraints
        self.curr_domains = None
        self.nassigns = 0

    def assign(self, var, val, assignment):
        """{var: val} hozzárendelés; Régi érték eldobása."""
        assignment[var] = val
        self.nassigns += 1

    def unassign(self, var, assignment):
        """{var: val} törlése.
        Nem kell meghívni ezt a metódust akkor ha egy változó értéke módosul!"""
        if var in assignment:
            del assignment[var]

    def nconflicts(self, var, val, assignment):
        """A var=val és a többi változó közötti ütközések számát adja vissza."""

        # Az alosztályok ezt hatékonyabban tudják megvalósítani
        count=0
        for v in self.neighbors[(var)]: # for v in self.neighbors[str(var)]:
            if len(assignment)==0:
                return count
            else:
                valami = v in assignment and not self.constraints(var, val, v, assignment[v])
            count+=valami

        return count



    def display(self, assignment):
        """CSP megjelenítése olvasható formában"""
        # Az alosztályok szebb módon nyomtathatnak, vagy grafikus felhasználói felülettel jeleníthetnek meg
        print(assignment)

    # -----------------------------------------------------------------------
    # A következő metódusokat csak a graph_search és a tree_search használja:

    def actions(self, state):
        """Az alkalmazható műveletek listájának visszaadása:
        A nem ütköző hozzárendelések a hozzá nem rendelt változóhoz."""
        if len(state) == len(self.variables):
            return []
        else:
            assignment = dict(state)
            var = first([v for v in self.variables if v not in assignment])
            ls=[]
            for val in self.domains[var]:
                if self.nconflicts(var, val, assignment) == 0:
                    ls.append((var,val))


            return ls

    def result(self, state, action):
        """Művelet végrehajtása és új állapot visszaadás"""
        (var, val) = action
        return state + ((var, val),)

    def goal_test(self, state):
        """A cél az összes változó hozzárendelése, minden megkötéssel."""
        assignment = dict(state)
        return (len(assignment) == len(self.variables)
                and all(self.nconflicts(variables, assignment[variables], assignment) == 0
                        for variables in self.variables))

    # -----------------------------------------------------------------------
    # Megszorításokhoz

    def support_pruning(self):
        """Ki tudjuk metszeni az értékeket a tartományokból?"""
        if self.curr_domains is None:
            self.curr_domains = {v: list(self.domains[v]) for v in self.variables}

    def suppose(self, var, value):
        """Következtetések összegyűjtése feltéve ha var=value."""
        self.support_pruning()
        removals = [(var, a) for a in self.curr_domains[var] if a != value]
        self.curr_domains[var] = [value]
        return removals

    def prune(self, var, value, removals):
        """A var=value kizárása."""
        self.curr_domains[var].remove(value)
        if removals is not None:
            removals.append((var, value))

    def choices(self, var):
        """A var összes olyan értékét adja vissza, amely jelenleg nincs kizárva."""
        return (self.curr_domains or self.domains)[var]

    def infer_assignment(self):
        """Vissza adja az aktuális következtetések által feltételezett részleges hozzárendelést."""
        self.support_pruning()
        return {v: self.curr_domains[v][0]
                for v in self.variables if 1 == len(self.curr_domains[v])}

    def restore(self, removals):
        """Egy feltevést és az abból származó összes következtetést visszavonása."""
        for B, b in removals:
            self.curr_domains[B].append(b)

    # -----------------------------------------------------------------------
    # min_conflicts kereséshez

    def conflicted_vars(self, current):
        """Vissza adja az aktuális hozzárendelésben ütköző változók listáját."""
        return [var for var in self.variables if self.nconflicts(var, current[var], current) > 0]


class UniversalDict:
    """Az univerzális szótár bármely kulcsot ugyanarra az értékre képez le. Itt használjuk tartományként olyan CSP-k esetében,
    amelyekben minden változónak ugyanaz a tartománya.
    >>> d = UniversalDict(42)
    >>> d['life']
    42
    """

    def __init__(self, value): self.value = value

    def __getitem__(self, key): return self.value

    def __repr__(self): return '{{Any: {0!r}}}'.format(self.value)


class InstruCSP(CSP):

    def __init__(self, variables, domains, neighbors, constraints):
        super().__init__(variables, domains, neighbors, constraints)
        self.assignment_history = []

    def assign(self, var, val, assignment):
        super().assign(var, val, assignment)
        self.assignment_history.append(copy.deepcopy(assignment))

    def unassign(self, var, assignment):
        super().unassign(var, assignment)
        self.assignment_history.append(copy.deepcopy(assignment))


def different_values_constraint(A, a, B, b):
    """A megszorítás, amely szerint két szomszédos változónak különböznie kell az értékben."""
    return a != b


def MapColoringCSP(colors, neighbors):
    """
    Képezen CSP-t a színezési problémára, úgy, hogy bármely két szomszédos régió térképét különböző színekkel színezze.
    Az argumentumok színek listája, és a {region: [neighbor,...]} bejegyzések szótára.
    Ez a dict a parse_neighbors által meghatározott formátumú string-ként is megadható.
    """
    if isinstance(neighbors, str):
        neighbors = parse_neighbors(neighbors)
    return CSP(list(neighbors.keys()), UniversalDict(colors), neighbors, different_values_constraint)


def parse_neighbors(neighbors):
    """
    Konvertálja az 'X: Y Z; Y: Z' egy szótárba, amely a régiókat a szomszédokhoz képzi le.
    A szintaxis egy régiónév, amelyet egy ':' jel követ, majd nulla vagy több régiónév, majd ezt követi a ';', minden régiónévnél megismétlve.
    Ha azt mondjuk, hogy 'X: Y', nincs szüksége 'Y: X'-re.
    parse_neighbors('X: YZ; Y: Z') == {'Y': ['X', 'Z'], 'X': ['Y', 'Z'], 'Z': ['X' ', 'I']}
    True (igaz)
    """
    dic = defaultdict(list)
    specs = [spec.split(':') for spec in neighbors.split(';')]
    for (A, Aneighbors) in specs:
        A = A.strip()
        for B in Aneighbors.split():
            dic[A].append(B)
            dic[B].append(A)
    return dic


def make_instru(csp):
    return InstruCSP(csp.variables, csp.domains, csp.neighbors, csp.constraints)


# ---------------------------------------------------------------------------
# --------------------------------- AC3 -------------------------------------
# ---------------------------------------------------------------------------

def revise(csp, Xi, Xj, removals):
    """Igaz értéket ad vissza, ha eltávolítunk egy értéket."""
    revised = False
    for x in csp.curr_domains[Xi][:]:
        # If Xi=x conflicts with Xj=y for every possible y, eliminate Xi=x
        if all(not csp.constraints(Xi, x, Xj, y) for y in csp.curr_domains[Xj]):
            csp.prune(Xi, x, removals)
            revised = True
    return revised


def dom_j_up(csp, queue):
    csp=csp
    queue=queue
    ss=SortedSet(queue, key=lambda t: neg(len(csp.curr_domains[t[1]])))


    return ss


def AC3(csp, queue=None, removals=None, arc_heuristic=dom_j_up):
    if queue is None:
        queue = set()
        for Xi in csp.variables:
            for Xk in csp.neighbors[(Xi)]: #for Xk in csp.neighbors[str(Xi)]:
                queue.add((Xi,(Xk))) ##queue.add((Xi,int(Xk)))


    csp.support_pruning()
    queue = arc_heuristic(csp, queue)
    while queue:
        (Xi, Xj) = queue.pop()
        if revise(csp, Xi, Xj, removals):
            if not csp.curr_domains[Xi]:
                return False
            for Xk in csp.neighbors[Xi]:
                if Xk != Xj:
                    queue.add((Xk, Xi))
    return True


# ---------------------------------------------------------------------------
# ------------------------------ BACKTRACKING -------------------------------
# ---------------------------------------------------------------------------

def first_unassigned_variable(assignment, csp):
    """Az alapértelmezett értéksorrend."""
    return first([var for var in csp.variables if var not in assignment])


def unordered_domain_values(var, assignment, csp):
    """Az alapértelmezett értéksorrend."""
    return csp.choices(var)


def no_inference(csp, var, value, assignment, removals):
    return True


def backtracking_search(csp, select_unassigned_variable=first_unassigned_variable,
                        order_domain_values=unordered_domain_values, inference=no_inference):
    def backtrack(assignment):
        if len(assignment) == len(csp.variables):
            return assignment
        var = select_unassigned_variable(assignment, csp)
        for value in order_domain_values(var, assignment, csp):
            nulla=csp.nconflicts(var, value, assignment)
            if 0 == nulla:
                csp.assign(var, value, assignment)
                removals = csp.suppose(var, value)
                if inference(csp, var, value, assignment, removals):
                    result = backtrack(assignment)
                    if result is not None:
                        return result
                csp.restore(removals)
        csp.unassign(var, assignment)
        return None

    result = backtrack({})
    assert result is None or csp.goal_test(result)
    return result


def num_legal_values(csp, var, assignment):
    if csp.curr_domains:
        return len(csp.curr_domains[var])
    else:
        return count(csp.nconflicts(var, val, assignment) == 0
                     for val in csp.domains[var])


def nconflicts(self, var, val, assignment):
    """A var=val és a többi változó közötti ütközések számát adja vissza."""

    # Subclasses may implement this more efficiently
    def conflict(var2):
        return (var2 in assignment and
                not self.constraints(var, val, var2, assignment[var2]))

    return count(conflict(v) for v in self.neighbors[var])


def mrv(assignment, csp):
    """Minimum-remaining-values heuristic."""
    return argmin_random_tie(
        [v for v in csp.variables if v not in assignment],
        key=lambda var: num_legal_values(csp, var, assignment))


def lcv(var, assignment, csp):
    """Legkevésbé korlátozó érték heuristic."""
    return sorted(csp.choices(var),
                  key=lambda val: csp.nconflicts(var, val, assignment))


def mac(csp, var, value, assignment, removals, constraint_propagation=AC3):
    """Ív konzisztencia megszorítás"""
    return constraint_propagation(csp, {(X, var) for X in csp.neighbors[var]}, removals)