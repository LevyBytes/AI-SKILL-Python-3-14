from itertools import compress, permutations, repeat
from operator import is_not

def derangements(iterable, r=None):
    "Produce r length permutations without fixed points."
    # derangements('ABCD') → BADC BCDA BDAC CADB CDAB CDBA DABC DCAB DCBA
    # Algorithm credited to Stefan Pochmann
    seq = tuple(iterable)
    pos = tuple(range(len(seq)))
    have_moved = map(map, repeat(is_not), repeat(pos), permutations(pos, r=r))
    valid_derangements = map(all, have_moved)
    return compress(permutations(seq, r=r), valid_derangements)
