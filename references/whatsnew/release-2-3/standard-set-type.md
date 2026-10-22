# Python 2.3 changes: Set datatype introduction and operations

### What’s New in Python 2.3

Author:

A.M. Kuchling

The features that arrived with Python 2.3 are described here. The release date for Python 2.3 was July 29, 2003.

Python 2.3 had three central goals: refining the capabilities first introduced in 2.2, layering in a range of modest yet handy improvements to the core language, and growing the standard library. After 18 months of bug fixes plus tuning work that sped up new-style classes, the object model from the prior release came out the stronger for it. The set of built-in functions gained a couple of entries, among them [`sum()`](https://docs.python.org/3.14/library/functions.html#sum) and [`enumerate()`](https://docs.python.org/3.14/library/functions.html#enumerate). You can now apply the [`in`](https://docs.python.org/3.14/reference/expressions.html#in) operator to look for substrings (for instance, `"ab" in "abc"` evaluates to [`True`](https://docs.python.org/3.14/library/constants.html#True)).

Among the numerous additions to the library are Boolean, set, heap, and date/time data types, support for loading modules out of ZIP-format archives, metadata handling for the long-awaited Python catalog, a refreshed IDLE, plus modules covering log messages, text wrapping, CSV parsing, command-line option handling, and BerkeleyDB databases — and the roster of fresh and improved modules runs on from there.

Rather than laying out a full specification of every addition, this article aims to give a handy survey instead. The Python 2.3 documentation — including the Python Library Reference and the Python Reference Manual — is where to look for full details. To grasp the entire implementation and the reasoning behind a given new feature’s design, consult that feature’s PEP.

### PEP 218: A Standard Set Datatype

A set datatype implementation ships inside the brand-new `sets` module. Mutable sets — ones whose members you can add and drop — are handled by the `Set` class. Sets that cannot be altered fall under the `ImmutableSet` class, and because of that an `ImmutableSet` instance may serve as a dictionary key. Because sets sit atop dictionaries, every element you place in a set has to be hashable.

A short example follows:

```python
>>> import sets
>>> S = sets.Set([1,2,3])
>>> S
Set([1, 2, 3])
>>> 1 in S
True
>>> 0 in S
False
>>> S.add(5)
>>> S.remove(3)
>>> S
Set([1, 2, 5])
>>>

```

To find the union and the intersection of sets you use the [`union()`](https://docs.python.org/3.14/library/stdtypes.html#frozenset.union) and [`intersection()`](https://docs.python.org/3.14/library/stdtypes.html#frozenset.intersection) methods; as a second option, the bitwise operators `&` and `|` do the same job. For mutable sets there are in-place counterparts of those methods too, `union_update()` and [`intersection_update()`](https://docs.python.org/3.14/library/stdtypes.html#set.intersection_update).

```python
>>> S1 = sets.Set([1,2,3])
>>> S2 = sets.Set([4,5,6])
>>> S1.union(S2)
Set([1, 2, 3, 4, 5, 6])
>>> S1 | S2                  # Alternative notation
Set([1, 2, 3, 4, 5, 6])
>>> S1.intersection(S2)
Set([])
>>> S1 & S2                  # Alternative notation
Set([])
>>> S1.union_update(S2)
>>> S1
Set([1, 2, 3, 4, 5, 6])
>>>

```

Two sets can also yield their symmetric difference. That result holds every element of the union except those sitting in the intersection. Put differently, the symmetric difference gathers each element belonging to precisely one of the two sets. Once more there is a second notation (`^`) to reach for, plus an in-place form carrying the clumsy label [`symmetric_difference_update()`](https://docs.python.org/3.14/library/stdtypes.html#set.symmetric_difference_update).

```python
>>> S1 = sets.Set([1,2,3,4])
>>> S2 = sets.Set([3,4,5,6])
>>> S1.symmetric_difference(S2)
Set([1, 2, 5, 6])
>>> S1 ^ S2
Set([1, 2, 5, 6])
>>>

```

To test whether a given set is a subset or a superset of some other set, the `issubset()` and `issuperset()` methods are provided as well:

[Subject index](INDEX.md) · [Next source section](pep-218-a-standard-set-datatype-see-also.md)
