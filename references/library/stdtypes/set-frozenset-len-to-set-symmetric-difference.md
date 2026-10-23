# stdtypes / set, frozenset: Set membership, relations and nonmutating set algebra

len(s)

Hand back how many elements set *s* holds (the cardinality of *s*).

 x in s

Test *x* for membership in *s*.

 x not in s

Test *x* for non-membership in *s*.

 frozenset.isdisjoint(*other*, */*)

 set.isdisjoint(*other*, */*)

Hand back `True` when the set shares no elements with *other*. Two sets are disjoint exactly when their intersection comes out empty.

 frozenset.issubset(*other*, */*)

 set.issubset(*other*, */*)

 set <= other

Test whether every element in the set is in *other*.

 set < other

Test whether the set is a proper subset of *other*, that is, `set <= other and set != other`.

 frozenset.issuperset(*other*, */*)

 set.issuperset(*other*, */*)

 set >= other

Test whether every element in *other* is in the set.

 set > other

Test whether the set is a proper superset of *other*, that is, `set >= other and set != other`.

 frozenset.union(**others*)

 set.union(**others*)

 set | other | ...

Hand back a fresh set holding the elements from the set together with every one of the others.

 frozenset.intersection(**others*)

 set.intersection(**others*)

 set & other & ...

Hand back a fresh set holding the elements shared by the set and every one of the others.

 frozenset.difference(**others*)

 set.difference(**others*)

 set - other - ...

Hand back a fresh set holding the set's elements that are absent from the others.

 frozenset.symmetric_difference(*other*, */*)

 set.symmetric_difference(*other*, */*)

 set ^ other

Hand back a fresh set holding the elements found in either the set or *other* but not in both.

[Subject index](INDEX.md) · [Previous](set-class-to-frozenset-class.md) · [Continue](frozenset-copy-to-set-clear.md) · [Owning module, declaration or section: set; frozenset](set-class-to-frozenset-class.md) · [Owning module, declaration or section: Set Types - `set`, `frozenset`](set-class-to-frozenset-class.md)
