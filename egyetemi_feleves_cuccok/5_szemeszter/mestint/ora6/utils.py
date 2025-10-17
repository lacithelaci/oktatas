import random

identity = lambda x: x # azonosság

def shuffled(iterable):
    """Véletlenszerűen össze keveri az iterálható objektumot."""
    items = list(iterable)
    random.shuffle(items)
    return items

def argmin_random_tie(seq, key=identity):
    """Adja vissza a seq legkisebb elemét; véletlenszerűen szakítsa meg a kapcsolatokat."""
    return min(shuffled(seq), key=key)

def count(seq):
    """Meg számolja az igazként értelmezett tételek számát."""
    return sum(map(bool, seq))

def first(iterable, default=None):
    """Egy iterálható elem első elemét adja vissza; vagy a default-ot."""
    return next(iter(iterable), default)