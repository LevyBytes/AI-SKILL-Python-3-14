# 3.2.7.1. Dictionaries

#### 3.2.7.1. Dictionaries

These stand for finite collections of objects keyed by values that are very nearly anything. The only values forbidden as keys are those that contain lists or dictionaries or further mutable types judged by value rather than by object identity; this restriction exists because dictionaries can only be implemented efficiently when a key keeps a hash value that never varies. Where numeric types act as keys, the customary numeric-comparison conventions hold: two numbers that test equal (say `1` and `1.0`) point to the very same dictionary entry and may stand in for each other.

Insertion order is preserved by dictionaries, which means keys come back out in the same sequence they were added one after another into the dictionary. Overwriting a key already present leaves the order untouched, whereas deleting a key and inserting it afresh appends it at the end rather than restoring its former position.

Dictionaries are mutable; the `{}` notation creates them (refer to the section [Dictionary displays](https://docs.python.org/3.14/reference/expressions.html#dict)).

More illustrations of mapping types are offered by the extension modules [`dbm.ndbm`](https://docs.python.org/3.14/library/dbm.html#module-dbm.ndbm) and [`dbm.gnu`](https://docs.python.org/3.14/library/dbm.html#module-dbm.gnu), and by the [`collections`](https://docs.python.org/3.14/library/collections.html#module-collections) module as well.

Changed in version 3.7: Across Python releases earlier than 3.6, dictionaries kept no insertion order. With CPython 3.6 that order began to be kept, though back then it ranked as an implementation detail and not as a guarantee made by the language.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](mappings.md) · [Previous source section](mappings.md) · [Following source section](callable-types.md)
