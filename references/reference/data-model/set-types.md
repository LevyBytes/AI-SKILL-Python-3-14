# 3.2.6. Set types

### 3.2.6. Set types

These stand for unordered, finite collections of unique, immutable objects. Because of that, no subscript can index them. They can, however, be iterated over, and the built-in function [`len()`](https://docs.python.org/3.14/library/functions.html#len) gives back how many items a set holds. Sets are commonly put to use for quick membership testing, stripping duplicates out of a sequence, and carrying out mathematical operations like intersection, union, difference, and symmetric difference.

Set elements follow the same immutability rules that dictionary keys do. Bear in mind that, by the usual conventions of numeric comparison, two numbers found to be equal (say `1` and `1.0`) can never both sit inside a single set — at most one is kept.

At present there are two intrinsic set types:

Sets

These stand for a mutable set. The built-in [`set()`](https://docs.python.org/3.14/library/stdtypes.html#set) constructor creates them, and afterwards several methods, such as [`add()`](https://docs.python.org/3.14/library/stdtypes.html#set.add), can change them.

Frozen sets

These stand for an immutable set. The built-in [`frozenset()`](https://docs.python.org/3.14/library/stdtypes.html#frozenset) constructor creates them. Because a frozenset is immutable and [hashable](https://docs.python.org/3.14/glossary.html#term-hashable), it can serve again as an element within another set, or serve as a dictionary key.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Previous source section](mutable-sequences.md) · [Following source section](mappings.md)
