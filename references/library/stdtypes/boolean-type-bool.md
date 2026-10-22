# Boolean Type - `bool`

### Boolean Type - [`bool`](https://docs.python.org/3.14/library/functions.html#bool)

Booleans stand for truth values. There are precisely two constant instances of the [`bool`](https://docs.python.org/3.14/library/functions.html#bool) type: `True` and `False`.

The [`bool()`](https://docs.python.org/3.14/library/functions.html#bool) built-in turns any value into a boolean whenever that value can be read as a truth value (refer to the Truth Value Testing section above).

For logic, reach for the boolean operators `and`, `or` and `not`. Applying the bitwise operators `&`, `|`, `^` to a pair of booleans yields a bool matching the logical "and", "or", "xor" results. Even so, favour the logical operators `and`, `or` and `!=` ahead of `&`, `|` and `^`.

Deprecated since version 3.12: Applying the bitwise inversion operator `~` is now deprecated; doing so will trigger an error once Python 3.16 arrives.

[`bool`](https://docs.python.org/3.14/library/functions.html#bool) is a subclass of [`int`](https://docs.python.org/3.14/library/functions.html#int) (see Numeric Types — int, float, complex). Across many numeric settings, `False` and `True` act like the integers 0 and 1 respectively. Leaning on that, though, is not recommended; perform an explicit conversion with [`int()`](https://docs.python.org/3.14/library/functions.html#int) instead.

[Subject index](INDEX.md) · [Previous](hashing-of-numeric-types.md) · [Continue](container-iter-to-iterator-next.md)
