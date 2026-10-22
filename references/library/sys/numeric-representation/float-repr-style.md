# sys.float_repr_style

sys.float_repr_style

A string reporting how the [`repr()`](https://docs.python.org/3.14/library/functions.html#repr) function handles floats. When that string equals `'short'`, then given a finite float `x`, `repr(x)` tries to emit a short string satisfying `float(repr(x)) == x`. That has been the standard behaviour since Python 3.1. In the other case, `float_repr_style` equals `'legacy'` and `repr(x)` acts just as it used to in Python releases before 3.1.

Added in version 3.1.

[API family](INDEX.md) · [sys context index](../INDEX.md).
