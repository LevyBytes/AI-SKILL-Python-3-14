# What’s New in Python 2.6 / New and Improved Modules - heapq, http.client, inspect, itertools

```python
>>> list(heapq.merge([1, 3, 5, 9], [2, 8, 16]))
[1, 2, 3, 5, 8, 9, 16]

```

There is also a second new function, `heappushpop(heap, item)`, which puts *item* onto *heap* and then pops and returns the smallest item. Doing it this way is more efficient than separately calling `heappush()` followed by `heappop()`.

[`heapq`](https://docs.python.org/3.14/library/heapq.html#module-heapq) is now built to rely only on less-than comparison rather than the less-than-or-equal comparison it leaned on before. That brings `heapq`’s handling of a type in line with the [`list.sort()`](https://docs.python.org/3.14/library/stdtypes.html#list.sort) method. (Contributed by Raymond Hettinger.)

- An optional `timeout` parameter, given as a count of seconds, was added to the constructors of the [`httplib.HTTPConnection`](https://docs.python.org/3.14/library/http.client.html#http.client.HTTPConnection) and [`HTTPSConnection`](https://docs.python.org/3.14/library/http.client.html#http.client.HTTPSConnection) classes. (Added by Facundo Batista.)

- The bulk of the [`inspect`](https://docs.python.org/3.14/library/inspect.html#module-inspect) module’s functions, `getmoduleinfo()` and `getargs()` among them, now hand back named tuples. On top of acting like tuples, the pieces of the returned value can additionally be reached as attributes. (Contributed by Raymond Hettinger.)

A few new functions in the module are `isgenerator()`, `isgeneratorfunction()`, and `isabstract()`.

- The [`itertools`](https://docs.python.org/3.14/library/itertools.html#module-itertools) module picked up several new functions.

`izip_longest(iter1, iter2, ...[, fillvalue])` assembles tuples out of each of the elements; when some of the iterables run shorter than the rest, the absent values are filled in with *fillvalue*. As an example:

```python
>>> tuple(itertools.izip_longest([1,2,3], [1,2,3,4,5]))
((1, 1), (2, 2), (3, 3), (None, 4), (None, 5))

```

`product(iter1, iter2, ..., [repeat=N])` yields the Cartesian product of the iterables passed in, a collection of tuples holding every conceivable combination of the elements drawn from each iterable.

```python
>>> list(itertools.product([1,2,3], [4,5,6]))
[(1, 4), (1, 5), (1, 6),
 (2, 4), (2, 5), (2, 6),
 (3, 4), (3, 5), (3, 6)]

```

The optional *repeat* keyword argument serves to take the product of an iterable, or a group of iterables, against themselves, repeated *N* times. Given a lone iterable argument, *N*-tuples come back:

```python
>>> list(itertools.product([1,2], repeat=3))
[(1, 1, 1), (1, 1, 2), (1, 2, 1), (1, 2, 2),
 (2, 1, 1), (2, 1, 2), (2, 2, 1), (2, 2, 2)]

```

Given two iterables, *2N*-tuples come back.

```python
>>> list(itertools.product([1,2], [3,4], repeat=2))
[(1, 3, 1, 3), (1, 3, 1, 4), (1, 3, 2, 3), (1, 3, 2, 4),
 (1, 4, 1, 3), (1, 4, 1, 4), (1, 4, 2, 3), (1, 4, 2, 4),
 (2, 3, 1, 3), (2, 3, 1, 4), (2, 3, 2, 3), (2, 3, 2, 4),
 (2, 4, 1, 3), (2, 4, 1, 4), (2, 4, 2, 3), (2, 4, 2, 4)]

```

`combinations(iterable, r)` hands back sub-sequences of length *r* taken from the elements of *iterable*.

```python
>>> list(itertools.combinations('123', 2))
[('1', '2'), ('1', '3'), ('2', '3')]
>>> list(itertools.combinations('123', 3))
[('1', '2', '3')]
>>> list(itertools.combinations('1234', 3))
[('1', '2', '3'), ('1', '2', '4'),
 ('1', '3', '4'), ('2', '3', '4')]

```

`permutations(iter[, r])` hands back every permutation of length *r* drawn from the iterable’s elements. When *r* goes unspecified, it falls back to the count of elements the iterable yields.

[Subject index](INDEX.md) · [Previous source section](new-and-improved-modules-and-affecting-the-rest-of-the-line.md) · [Next source section](itertools-through-operator-module-changes.md) · [Release/subject declaration](python-3-0.md) · [Release/subject declaration](standard-library-module-changes.md)
