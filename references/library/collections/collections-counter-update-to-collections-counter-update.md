# collections`Counter` objects - Signature and initial contract

update(***kwargs*)

 update(*iterable*, */*, ***kwargs*)

 update(*mapping*, */*, ***kwargs*)

Counts come from an *iterable* or are folded in from another *mapping* (or counter). It behaves like [`dict.update()`](https://docs.python.org/3.14/library/stdtypes.html#dict.update) but adds counts in place of replacing them. Note too that the *iterable* should be a sequence of elements rather than a sequence of `(key, value)` pairs.

Counters offer rich comparison operators covering equality, subset, and superset relations: `==`, `!=`, `<`, `<=`, `>`, `>=`. Each of those checks regards absent elements as carrying zero counts, so that `Counter(a=1) == Counter(a=1, b=0)` comes out true.

Changed in version 3.10: Rich comparison operations were added.

Changed in version 3.10: When checking equality, an absent element now counts as zero. Earlier on, `Counter(a=3)` along with `Counter(a=3, b=0)` were held to be different.

Typical patterns when handling `Counter` objects:

```python
c.total()                       # total of all counts
c.clear()                       # reset all counts
list(c)                         # list unique elements
set(c)                          # convert to a set
dict(c)                         # convert to a regular dictionary
c.items()                       # access the (elem, cnt) pairs
Counter(dict(list_of_pairs))    # convert from a list of (elem, cnt) pairs
c.most_common()[:-n-1:-1]       # n least common elements
+c                              # remove zero and negative counts

```

A handful of mathematical operations let you merge `Counter` objects into multisets (counters whose counts exceed zero). Addition and subtraction join counters by summing or deducting the counts of matching elements. Intersection and union hand back the minimum and maximum of matching counts. Equality and inclusion weigh matching counts against each other. Every operation tolerates inputs bearing signed counts, yet the output drops any result whose count is zero or below.

```pycon
>>> c = Counter(a=3, b=1)
>>> d = Counter(a=1, b=2)
>>> c + d                       # add two counters together:  c[x] + d[x]
Counter({'a': 4, 'b': 3})
>>> c - d                       # subtract (keeping only positive counts)
Counter({'a': 2})
>>> c & d                       # intersection:  min(c[x], d[x])
Counter({'a': 1, 'b': 1})
>>> c | d                       # union:  max(c[x], d[x])
Counter({'a': 3, 'b': 2})
>>> c == d                      # equality:  c[x] == d[x]
False
>>> c <= d                      # inclusion:  c[x] <= d[x]
False

```

Adding or subtracting in unary form is shorthand for adding an empty counter or subtracting from an empty counter.

```python
>>> c = Counter(a=2, b=-4)
>>> +c
Counter({'a': 2})
>>> -c
Counter({'b': 4})

```

Added in version 3.3: Gained support for unary plus and unary minus, plus in-place multiset operations.

Note

Counters were chiefly built to handle positive integers standing for running counts; even so, deliberate care kept the door open for use cases that call for other types or negative values. To assist with those use cases, the following text spells out the minimum range and type restrictions.

- The `Counter` class is itself a dictionary subclass that puts no constraints on its keys and values. Although the values are meant to be numbers standing for counts, you *could* place anything inside the value field.

- All that the `most_common()` method asks is that the values be orderable.

- When doing in-place operations like `c[key] += 1`, the value type merely has to support addition and subtraction. Thus fractions, floats, and decimals all function, and negative values are allowed. The very same holds for `update()` and `subtract()`, which permit negative and zero values across both inputs and outputs.

- The multiset methods target use cases with positive values exclusively. While the inputs may be negative or zero, only outputs carrying positive values get produced. No type restrictions apply, though the value type has to support addition, subtraction, and comparison.

-

[Subject index](INDEX.md) · [Previous](counter-elements-and-frequency-methods.md) · [Continue](counter-elements-integer-count-contract.md) · [Owning module, declaration or section: collections](collections-container-datatypes.md) · [Owning module, declaration or section: collections.Counter; collections.Counter; collections.Counter](collections-counter-class-to-collections-counter-class.md) · [Owning module, declaration or section: `Counter` objects](collections-counter-class-to-collections-counter-class.md)
