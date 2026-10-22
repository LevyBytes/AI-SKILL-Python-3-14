# Thread safety for set objects — Section introduction and initial examples

### Thread safety for set objects

The [`len()`](https://docs.python.org/3.14/library/functions.html#len) function is lock-free and [atomic](https://docs.python.org/3.14/glossary.html#term-atomic-operation).

The read operation below is lock-free. It places no block on concurrent edits and can witness intermediate states left by operations that hold the per-object lock:

```python
elem in s    # set.__contains__

```

This operation might compare elements through [`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__), which is capable of running arbitrary Python code. While such a comparison runs, another thread may edit the set. For built-in types such as [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), [`int`](https://docs.python.org/3.14/library/functions.html#int), and [`float`](https://docs.python.org/3.14/library/functions.html#float), `__eq__()` keeps the underlying lock held throughout comparisons and so there is nothing to worry about.

From this point onward, all remaining operations hold the per-object lock.

Adding or dropping one element is fine to invoke across several threads and leaves the set uncorrupted:

```python
s.add(elem)      # add element
s.remove(elem)   # remove element, raise if missing
s.discard(elem)  # remove element if present
s.pop()          # remove and return arbitrary element

```

These operations compare elements as well, so the same [`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__) caveats from above apply.

The [`copy()`](https://docs.python.org/3.14/library/stdtypes.html#set.copy) method builds a new object and keeps the per-object lock held throughout, which keeps it atomic in every case.

The [`clear()`](https://docs.python.org/3.14/library/stdtypes.html#set.clear) method keeps the lock held throughout. No other thread can witness elements while they are being dropped.

The operations below take only [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) or [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset) as operands and lock the pair of objects in every case:

```python
s |= other                   # other must be set/frozenset
s &= other                   # other must be set/frozenset
s -= other                   # other must be set/frozenset
s ^= other                   # other must be set/frozenset
s & other                    # other must be set/frozenset
s | other                    # other must be set/frozenset
s - other                    # other must be set/frozenset
s ^ other                    # other must be set/frozenset

```

[`set.update()`](https://docs.python.org/3.14/library/stdtypes.html#set.update), [`set.union()`](https://docs.python.org/3.14/library/stdtypes.html#set.union), [`set.intersection()`](https://docs.python.org/3.14/library/stdtypes.html#set.intersection) and [`set.difference()`](https://docs.python.org/3.14/library/stdtypes.html#set.difference) accept several iterables as arguments. Each of them walks through every iterable passed and carries out the following:

>
- [`set.update()`](https://docs.python.org/3.14/library/stdtypes.html#set.update) and [`set.union()`](https://docs.python.org/3.14/library/stdtypes.html#set.union) lock both objects only when

the other operand is a [`set`](https://docs.python.org/3.14/library/stdtypes.html#set), [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset), or [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict).

- [`set.intersection()`](https://docs.python.org/3.14/library/stdtypes.html#set.intersection) and [`set.difference()`](https://docs.python.org/3.14/library/stdtypes.html#set.difference) always try to lock

all objects.

[`set.symmetric_difference()`](https://docs.python.org/3.14/library/stdtypes.html#set.symmetric_difference) tries to lock both objects.

Among the update variants of those methods there are also a few differences:

>
- [`set.difference_update()`](https://docs.python.org/3.14/library/stdtypes.html#set.difference_update) and [`set.intersection_update()`](https://docs.python.org/3.14/library/stdtypes.html#set.intersection_update) try

to lock all objects one-by-one.

- [`set.symmetric_difference_update()`](https://docs.python.org/3.14/library/stdtypes.html#set.symmetric_difference_update) only locks the arguments if it is

of type [`set`](https://docs.python.org/3.14/library/stdtypes.html#set), [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset), or [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict).

The methods below always try to lock both objects:

[Subject index](INDEX.md) · [Previous](dictionary-nonatomic-operations.md) · [Continue](set-disjoint-operation-locking-example.md)
