# itertools: `itertools.permutations()`, `itertools.product()`

itertools.permutations(*iterable*, *r=None*)

Return successive *r* length [permutations of elements](https://www.britannica.com/science/permutation) from the *iterable*.

Where *r* is left unspecified or set to `None`, *r* takes on the length of the *iterable*, and every possible full-length permutation gets produced.

What comes out is a subsequence of `product()` from which entries containing repeated elements have been removed. How long the output is comes from [`math.perm()`](https://docs.python.org/3.14/library/math.html#math.perm), which evaluates `n! / (n - r)!` for `0 ≤ r ≤ n` and zero once `r > n`.

These permutation tuples come out in lexicographic order, following the ordering of the input *iterable*. Should that input *iterable* already be sorted, the resulting output tuples emerge sorted too.

An element's uniqueness is judged by where it sits, not by what it holds. So when the input elements are all distinct, no permutation will contain duplicate values.

Roughly equivalent to:

```python
def permutations(iterable, r=None):
    # permutations('ABCD', 2) → AB AC AD BA BC BD CA CB CD DA DB DC
    # permutations(range(3)) → 012 021 102 120 201 210

    pool = tuple(iterable)
    n = len(pool)
    r = n if r is None else r
    if r > n:
        return

    indices = list(range(n))
    cycles = list(range(n, n-r, -1))
    yield tuple(pool[i] for i in indices[:r])

    while n:
        for i in reversed(range(r)):
            cycles[i] -= 1
            if cycles[i] == 0:
                indices[i:] = indices[i+1:] + indices[i:i+1]
                cycles[i] = n - i
            else:
                j = cycles[i]
                indices[i], indices[-j] = indices[-j], indices[i]
                yield tuple(pool[i] for i in indices[:r])
                break
        else:
            return

```

 itertools.product(**iterables*, *repeat=1*)

[Cartesian product](https://en.wikipedia.org/wiki/Cartesian_product) of the input iterables.

This mirrors nested for-loops written inside a generator expression. For instance, `product(A, B)` gives back the same thing as `((x,y) for x in A for y in B)`.

Those nested loops turn over the way an odometer does, with the rightmost element stepping forward on each iteration. That arrangement yields a lexicographic ordering, so whenever the input's iterables are sorted, the product tuples come out sorted.

If you want the product of an iterable taken with itself, state how many repetitions you need through the optional *repeat* keyword argument. For instance, `product(A, repeat=4)` amounts to the same thing as `product(A, A, A, A)`.

The following code is roughly equivalent to this function, aside from the fact that the real implementation never accumulates intermediate results in memory:

```python
def product(*iterables, repeat=1):
    # product('ABCD', 'xy') → Ax Ay Bx By Cx Cy Dx Dy
    # product(range(2), repeat=3) → 000 001 010 011 100 101 110 111

    if repeat < 0:
        raise ValueError('repeat argument cannot be negative')
    pools = [tuple(pool) for pool in iterables] * repeat

    result = [[]]
    for pool in pools:
        result = [x+[y] for x in result for y in pool]

    for prod in result:
        yield tuple(prod)

```

Ahead of running, `product()` fully drains the input iterables, holding pools of values in memory so it can build the products. For that reason, it pays off only with finite inputs.

[Subject index](INDEX.md) · [Previous](itertools-islice-to-itertools-pairwise.md) · [Continue](itertools-repeat-to-itertools-takewhile.md) · [Owning module, declaration or section: itertools](itertools-functions-creating-iterators-for-efficient-looping.md) · [Owning module, declaration or section: Itertool Functions](itertools-accumulate.md)
