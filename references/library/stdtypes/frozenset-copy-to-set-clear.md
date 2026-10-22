# stdtypes: `frozenset.copy()`, `set.copy()`, `set.update()`, `set.intersection_update()`, `set.difference_update()`, `set.symmetric_difference_update()`, `set.add()`, `set.remove()`, `set.discard()`, `set.pop()`, `set.clear()`

frozenset.copy()

 set.copy()

Hand back a shallow copy of the set.

Note that the non-operator forms of `union()`, `intersection()`, `difference()`, `symmetric_difference()`, `issubset()`, and `issuperset()` will take any iterable as an argument. By contrast, the operator-based forms demand that their arguments be sets. That rules out mistake-prone expressions like `set('abc') & 'cbs'` and steers you toward the clearer `set('abc').intersection('cbs')`.

Each of `set` and `frozenset` supports comparisons between one set and another. Two sets are equal exactly when each set's every element is held by the other (each being a subset of the other). One set ranks below another exactly when the first is a proper subset of the second (a subset that is not equal). One set ranks above another exactly when the first is a proper superset of the second (a superset that is not equal).

Comparison between a `set` instance and a `frozenset` instance rests on their members. To illustrate, `set('abc') == frozenset('abc')` returns `True`, as does `set('abc') in set([frozenset('abc')])`.

The subset and equality comparisons do not extend into a total ordering function. As an illustration, any pair of nonempty disjoint sets are neither equal nor subsets of one another, which makes *all* of the following come back `False`: `a<b`, `a==b`, or `a>b`.

Because sets supply only a partial ordering (subset relationships), running `list.sort()` over a list of sets gives an undefined result.

Set elements, like dictionary keys, must be [hashable](https://docs.python.org/3.14/glossary.html#term-hashable).

Binary operations mixing a `set` instance with a `frozenset` yield the type of whichever operand comes first. As an example: `frozenset('ab') | set('bc')` returns an instance of `frozenset`.

The table below lists operations offered for `set` that have no counterpart on the immutable `frozenset` instances:

 set.update(**others*)

 set |= other | ...

Update the set, adding elements from all others.

 set.intersection_update(**others*)

 set &= other & ...

Update the set, keeping only elements found in it and all others.

 set.difference_update(**others*)

 set -= other | ...

Update the set, removing elements found in others.

 set.symmetric_difference_update(*other*, */*)

 set ^= other

Update the set so it retains only those elements present in exactly one of the two sets, never in both.

 set.add(*elem*, */*)

Add element *elem* to the set.

 set.remove(*elem*, */*)

Drop element *elem* out of the set. Should the set not hold *elem*, this raises [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError).

 set.discard(*elem*, */*)

Remove element *elem* from the set if it is present.

 set.pop()

Take out some arbitrary element from the set and return it. Should the set be empty, this raises [`KeyError`](https://docs.python.org/3.14/library/exceptions.html#KeyError).

 set.clear()

Remove all elements from the set.

Note that the non-operator forms of `update()`, `intersection_update()`, `difference_update()`, and `symmetric_difference_update()` will take any iterable as an argument.

Note as well that the *elem* argument passed to the [`__contains__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__contains__), `remove()`, and `discard()` methods is allowed to be a set. So that an equivalent frozenset can be looked up, a temporary one gets built from *elem*.

See also

For detailed information on thread-safety guarantees for `set` objects, see [Thread safety for set objects](https://docs.python.org/3.14/library/threadsafety.html#thread-safety-set).

Sets and frozensets are [generic](https://docs.python.org/3.14/library/typing.html#generics) over the type of their elements.

[Subject index](INDEX.md) · [Previous](set-frozenset-len-to-set-symmetric-difference.md) · [Continue](dict-class-to-dict-class.md) · [Owning module, declaration or section: set; frozenset](set-class-to-frozenset-class.md) · [Owning module, declaration or section: Set Types — `set`, `frozenset`](set-class-to-frozenset-class.md)
