# What's New In Python 3.0 / Ordering Comparisons

### Ordering Comparisons

The way Python 3.0 handles ordering comparisons has been streamlined:

- When operands lack a meaningful natural ordering, the ordering comparison operators (`<`, `<=`, `>=`, `>`) now throw a TypeError exception. So forms such as `1 < ''`, `0 > None` or `len <= len` have stopped being valid, and for instance `None < None` now throws [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) rather than handing back `False`. It follows that ordering a list of mixed kinds is meaningless now; each element has to be mutually comparable. Be aware that the `==` and `!=` operators are exempt: instances of differing incomparable kinds always evaluate as unequal to one another.

- The functions [`sorted()`](https://docs.python.org/3.14/library/functions.html#sorted) and [`list.sort()`](https://docs.python.org/3.14/library/stdtypes.html#list.sort) have stopped honoring the *cmp* argument that supplied a comparison function. Reach for the *key* argument in its place. N.B. the *key* and *reverse* arguments are ?keyword-only? now.

- Regard the `cmp()` function as removed, and the `__cmp__()` special method as no longer supported. For sorting reach for [`__lt__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__lt__), pair [`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__) with [`__hash__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__hash__), and supply the other rich comparisons where you need them. (Should you truly want the `cmp()` behavior back, the expression `(a > b) - (a < b)` serves as the stand-in for `cmp(a, b)`.)

[Subject index](INDEX.md) · [Previous source section](views-and-iterators-instead-of-lists.md) · [Next source section](integers.md) · [Release/subject declaration](common-stumbling-blocks.md)
