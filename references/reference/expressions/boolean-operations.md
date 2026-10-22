# 6.11. Boolean operations

### 6.11. Boolean operations

```text

or_test:  and_test | or_test "or" and_test
and_test: not_test | and_test "and" not_test
not_test: comparison | "not" not_test
```

Within Boolean operations, and likewise where control flow statements make use of expressions, these values count as false: `False`, `None`, numeric zero across every type, and empty strings and containers (which covers strings, tuples, lists, dictionaries, sets and frozensets). Everything else counts as true. A user-defined object can tailor its own truth value by supplying a [`__bool__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__bool__) method.

When its argument is false the `not` operator gives `True`, and otherwise `False`.

For the expression `x and y`, *x* is evaluated first; should *x* be false, that value is returned; if not, *y* is evaluated and its result is returned.

For the expression `x or y`, *x* is evaluated first; should *x* be true, that value is returned; if not, *y* is evaluated and its result is returned.

Keep in mind that neither `and` nor `or` confine the value and type they hand back to `False` and `True`; instead they return whichever argument was evaluated last. Now and then that proves handy: if `s` names a string you want swapped for a default whenever it is empty, the expression `s or 'foo'` delivers what you want. Since `not` must produce a fresh value, it returns a boolean no matter the type of its argument (for instance, `not 'foo'` gives `False` instead of `''`.)

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Previous source section](identity-comparisons.md) · [Following source section](assignment-expressions.md)
