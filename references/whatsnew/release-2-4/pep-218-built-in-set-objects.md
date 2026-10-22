# What’s New in Python 2.4 / PEP 218: Built-In Set Objects

### What’s New in Python 2.4

Author:

A.M. Kuchling

The following write-up walks through the capabilities added in Python 2.4.1, which shipped on March 30, 2005.

As releases go, Python 2.4 falls in the middle range. It carries fewer alterations than the sweeping Python 2.2 did, yet it adds more than the cautious 2.3 release did. On the language side, the two standout additions are function decorators along with generator expressions; the remaining updates mostly land in the standard library.

The CVS change logs record 481 patches that were applied and 502 bugs that were resolved across the span from Python 2.3 to 2.4. In all likelihood, each of those counts runs low.

Rather than laying out an exhaustive specification covering each individual addition, this piece offers a short orientation to every one of them. To get the complete picture, turn to the Python 2.4 documentation — for instance the Python Library Reference together with the Python Reference Manual. In many cases you’ll be pointed at the PEP covering a given addition for its implementation notes and design reasoning.

### PEP 218: Built-In Set Objects

The `sets` module first appeared back in Python 2.3. The Python core now ships C implementations of set data structures, exposed as a pair of fresh built-in types, `set(iterable)` plus `frozenset(iterable)`. These deliver fast operations for testing membership, for stripping repeated entries out of sequences, and for set algebra such as unions, intersections, differences, and symmetric differences.

```python
>>> a = set('abracadabra')              # form a set from a string
>>> 'z' in a                            # fast membership testing
False
>>> a                                   # unique letters in a
set(['a', 'r', 'b', 'c', 'd'])
>>> ''.join(a)                          # convert back into a string
'arbcd'

>>> b = set('alacazam')                 # form a second set
>>> a - b                               # letters in a but not in b
set(['r', 'd', 'b'])
>>> a | b                               # letters in either a or b
set(['a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'])
>>> a & b                               # letters in both a and b
set(['a', 'c'])
>>> a ^ b                               # letters in a or b but not both
set(['r', 'd', 'b', 'm', 'z', 'l'])

>>> a.add('z')                          # add a new element
>>> a.update('wxy')                     # add multiple new elements
>>> a
set(['a', 'c', 'b', 'd', 'r', 'w', 'y', 'x', 'z'])
>>> a.remove('x')                       # take one element out
>>> a
set(['a', 'c', 'b', 'd', 'r', 'w', 'y', 'z'])

```

As an unchangeable counterpart to [`set()`](https://docs.python.org/3.14/library/stdtypes.html#set), the [`frozenset()`](https://docs.python.org/3.14/library/stdtypes.html#frozenset) type exists. Because it’s both immutable and hashable, you can hand it to a dictionary as a key or store it inside another set.

The standard library still carries the `sets` module, which can come in handy whenever you’d like to derive a subclass from the `Set` or `ImmutableSet` classes. As things stand, nobody intends to deprecate it.

See also

[**PEP 218**](https://peps.python.org/pep-0218/) - Adding a Built-In Set Object Type

Greg Wilson floated the original proposal, and Raymond Hettinger carried it through to implementation.

[Subject index](INDEX.md) · [Next source section](pep-237-unifying-long-integers-and-integers.md)
