# stdtypes: `set`, `frozenset`

### Set Types — `set`, `frozenset`

A *set* object is an unordered grouping of distinct [hashable](https://docs.python.org/3.14/glossary.html#term-hashable) objects. Typical applications are checking membership, stripping duplicates out of a sequence, and computing math-style results such as union, intersection, symmetric difference, and difference. (Regarding other containers, consult the built-in `dict`, `list`, and `tuple` classes together with the [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module.)

As with other collections, sets handle `x in set`, `len(set)`, and `for x in set`. Because they are unordered, sets keep no track of where an element sits or the order it was added. As a result, sets offer no indexing, slicing, or other behavior typical of sequences.

At present there are two built-in set types, `set` and `frozenset`. A `set` is mutable — you can alter its contents through methods such as `add()` and `remove()`. Being mutable, it carries no hash value and therefore cannot serve as a dictionary key or as a member of another set. A `frozenset` is immutable and [hashable](https://docs.python.org/3.14/glossary.html#term-hashable) — once built, its contents are fixed; that lets it act as a dictionary key or as a member of another set.

Sets that are not empty (and not frozensets) may be built by writing a comma-separated list of elements inside braces, such as `{'jack', 'sjoerd'}`, on top of the `set` constructor.

Both classes share the same constructors:

 *class *set(*iterable=()*, */*)

 *class *frozenset(*iterable=()*, */*)

Hand back a fresh set or frozenset whose elements come from *iterable*. A set's elements have to be [hashable](https://docs.python.org/3.14/glossary.html#term-hashable). For sets containing sets, the nested sets need to be `frozenset` objects. When *iterable* is left out, a fresh empty set comes back.

Sets can be created by several means:

- Use a comma-separated list of elements within braces: `{'jack', 'sjoerd'}`

- Use a set comprehension: `{c for c in 'abracadabra' if c not in 'abc'}`

- Use the type constructor: `set()`, `set('foobar')`, `set(['a', 'b', 'foo'])`

Instances of `set` and `frozenset` provide the following operations:

[Subject index](INDEX.md) · [Previous](memory-views.md) · [Continue](set-frozenset-len-to-set-symmetric-difference.md)
