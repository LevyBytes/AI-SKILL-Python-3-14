# itertools: `itertools.combinations()`, `itertools.combinations_with_replacement()`

itertools.combinations(*iterable*, *r*)

Return *r* length subsequences of elements from the input *iterable*.

What comes out is a subsequence of `product()`, retaining only those entries that are themselves subsequences of the *iterable*. How long the output is comes from [`math.comb()`](https://docs.python.org/3.14/library/math.html#math.comb), which evaluates `n! / r! / (n - r)!` for `0 ≤ r ≤ n` and zero once `r > n`.

These combination tuples come out in lexicographic order, following the ordering of the input *iterable*. Should that input *iterable* already be sorted, the resulting output tuples emerge sorted too.

An element's uniqueness is judged by where it sits, not by what it holds. So when the input elements are all distinct, no combination will contain duplicate values.

Roughly equivalent to:

```python
def combinations(iterable, r):
    # combinations('ABCD', 2) → AB AC AD BC BD CD
    # combinations(range(4), 3) → 012 013 023 123

    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = list(range(r))

    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)

```

 itertools.combinations_with_replacement(*iterable*, *r*)

Return *r* length subsequences of elements drawn from the input *iterable*, with each individual element permitted to recur more than a single time.

What comes out is a subsequence of `product()` that retains only entries which are subsequences (possibly carrying repeated elements) of the *iterable*. The count of subsequences handed back is `(n + r - 1)! / r! / (n - 1)!` whenever `n > 0`.

These combination tuples come out in lexicographic order, following the ordering of the input *iterable*. should that input *iterable* already be sorted, the resulting output tuples emerge sorted too.

An element's uniqueness is judged by where it sits, not by what it holds. So when the input elements are all distinct, the combinations produced will be distinct as well.

Roughly equivalent to:

```python
def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) → AA AB AC BB BC CC

    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r

    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)

```

Added in version 3.1.

[Subject index](INDEX.md) · [Previous](itertools-batched-to-itertools-chain.md) · [Continue](itertools-compress-to-itertools-dropwhile.md) · [Owning module, declaration or section: itertools](itertools-functions-creating-iterators-for-efficient-looping.md) · [Owning module, declaration or section: Itertool Functions](itertools-accumulate.md)
