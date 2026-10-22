# stdtypes: `list`

### Lists

Lists are mutable sequences, generally serving to hold collections of homogeneous items (the exact extent of that homogeneity varying from application to application).

 *class *list(*iterable=()*, */*)

There are several ways to construct lists:

- Writing a pair of square brackets for the empty list: `[]`

- Writing square brackets and separating items with commas: `[a]`, `[a, b, c]`

- Writing a list comprehension: `[x for x in iterable]`

- Calling the type constructor: `list()` or `list(iterable)`

The constructor produces a list with the same items, in the same order, as *iterable*'s items. *iterable* can be a sequence, a container that allows iteration, or an iterator object. Where *iterable* is itself a list, a copy gets made and returned, akin to `iterable[:]`. To illustrate, `list('abc')` returns `['a', 'b', 'c']` and `list( (1, 2, 3) )` returns `[1, 2, 3]`. With no argument supplied, the constructor makes a new empty list, `[]`.

A great many other operations turn out lists too, the [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted) built-in among them.

Lists are [generic](https://docs.python.org/3.14/library/typing.html#generics) over the types of their items.

Lists carry out all the common and mutable sequence operations. On top of that, lists offer the following extra method:

[Subject index](INDEX.md) · [Previous](sequence-append-to-sequence-reverse.md) · [Continue](list-sort.md)
