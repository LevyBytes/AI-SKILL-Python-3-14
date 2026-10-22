# random — Recipes

### Recipes

The recipes that follow demonstrate drawing random picks efficiently out of the combinatoric iterators found in the [`itertools`](https://docs.python.org/3.14/library/itertools.html#module-itertools) module:

```python
import random

def random_product(*iterables, repeat=1):
    "Random selection from itertools.product(*iterables, repeat=repeat)"
    pools = tuple(map(tuple, iterables)) * repeat
    return tuple(map(random.choice, pools))

def random_permutation(iterable, r=None):
    "Random selection from itertools.permutations(iterable, r)"
    pool = tuple(iterable)
    r = len(pool) if r is None else r
    return tuple(random.sample(pool, r))

def random_combination(iterable, r):
    "Random selection from itertools.combinations(iterable, r)"
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.sample(range(n), r))
    return tuple(pool[i] for i in indices)

def random_combination_with_replacement(iterable, r):
    "Choose r elements with replacement.  Order the result to match the iterable."
    # Result will be in set(itertools.combinations_with_replacement(iterable, r)).
    pool = tuple(iterable)
    n = len(pool)
    indices = sorted(random.choices(range(n), k=r))
    return tuple(pool[i] for i in indices)

def random_derangement(iterable):
    "Choose a permutation where no element stays in its original position."
    seq = tuple(iterable)
    if len(seq) < 2:
        if not seq:
            return ()
        raise IndexError('No derangments to choose from')
    perm = list(range(len(seq)))
    start = tuple(perm)
    while True:
        random.shuffle(perm)
        if all(p != q for p, q in zip(start, perm)):
            return tuple([seq[i] for i in perm])

```

Out of the box, `random()` yields multiples of 2⁻⁵³ across *0.0 ≤ x < 1.0*. Every value of that kind sits at a uniform interval and maps precisely onto a Python float. Even so, plenty of the other floats you could represent inside that span never come up as candidates. To illustrate, `0.05954861408025609` is not a whole-number multiple of 2⁻⁵³.

A separate technique is shown by the recipe below, under which any float within the span becomes a viable pick. Its mantissa is drawn uniformly from integers spanning *2⁵² ≤ mantissa < 2⁵³*, while its exponent follows a geometric distribution in which an exponent below *-53* shows up half as frequently as the exponent one step above it.

```python
from random import Random
from math import ldexp

class FullRandom(Random):

    def random(self):
        mantissa = 0x10_0000_0000_0000 | self.getrandbits(52)
        exponent = -53
        x = 0
        while not x:
            x = self.getrandbits(32)
            exponent += x.bit_length() - 32
        return ldexp(mantissa, exponent)

```

Each real-valued distribution provided by the class then relies on this fresh method:

```python
>>> fr = FullRandom()
>>> fr.random()
0.05954861408025609
>>> fr.expovariate(0.25)
8.87925541791544

```

In spirit, this recipe matches an algorithm that picks among every multiple of 2⁻¹⁰⁷⁴ across *0.0 ≤ x < 1.0*. Those values are uniformly spaced too, yet the bulk of them end up rounded down toward the closest Python float that can be represented. (That quantity 2⁻¹⁰⁷⁴ denotes the tiniest positive unnormalized float and matches `math.ulp(0.0)`.)

See also

[Generating Pseudo-random Floating-Point Values](https://allendowney.com/research/rand/downey07randfloat.pdf) — Allen B. Downey's paper laying out techniques for producing floats at a finer granularity than `random()` normally delivers.

[Subject index](INDEX.md) · [Previous](examples-code-example-from-statistics-import-fmean-as-mean.md) · [Owning module, declaration or section: random](random-generate-pseudo-random-numbers.md) · [Continue](command-line-usage.md)
