# How do I convert between tuples and lists?

### Sequences (tuples/lists)

### How do I convert between tuples and lists?

The type constructor `tuple(seq)` turns any sequence (actually, any iterable) into a tuple holding the same items in the same order.

By way of example, `tuple([1, 2, 3])` produces `(1, 2, 3)` and `tuple('abc')` produces `('a', 'b', 'c')`. When the argument is already a tuple, no copy is made and the very same object comes back, so calling [`tuple()`](https://docs.python.org/3.14/library/stdtypes.html#tuple) is inexpensive even when you aren’t certain an object is already a tuple.

The type constructor `list(seq)` turns any sequence or iterable into a list holding the same items in the same order. By way of example, `list((1, 2, 3))` produces `[1, 2, 3]` and `list('abc')` produces `['a', 'b', 'c']`. When the argument is already a list, it makes a copy exactly as `seq[:]` would.

[Subject index](INDEX.md)
