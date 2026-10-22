# 6.10.2. Membership test operations

### 6.10.2. Membership test operations

Membership is what the `in` and `not in` operators check. `x in s` comes out `True` when *x* belongs to *s*, and `False` if not. `x not in s` gives back the negation of `x in s`. Every built-in sequence and set type supports this, and so does dictionary, where `in` checks whether a given key is present. Among container types like list, tuple, set, frozenset, dict, or collections.deque, the expression `x in y` amounts to `any(x is e or x == e for e in y)`.

With the string and bytes types, `x in y` holds `True` exactly when *x* is a substring of *y*. The check `y.find(x) != -1` does the same job. An empty string always counts as a substring of any other string, hence `"" in "abc"` gives `True`.

When a user-defined class supplies the [`__contains__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__contains__) method, `x in y` gives back `True` provided `y.__contains__(x)` produces a true value, and `False` if not.

When a user-defined class omits [`__contains__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__contains__) yet provides [`__iter__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__iter__), `x in y` is `True` whenever iterating across `y` turns up some value `z` for which `x is z or x == z` evaluates true. Should the iteration throw an exception, the effect is the same as if `in` itself had thrown it.

Finally, the legacy iteration protocol gets a try: should a class define [`__getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getitem__), then `x in y` holds `True` exactly when some non-negative integer index *i* satisfies `x is y[i] or x == y[i]` while no smaller integer index triggers the [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError) exception. (Any other exception raised behaves as though `in` had raised it.)

By definition, the `not in` operator carries the opposite truth value to `in`.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](comparisons.md) · [Previous source section](value-comparisons.md) · [Following source section](identity-comparisons.md)
