# NaN comparison and IEEE floating-point semantics

Represents a floating-point “not a number”, or NaN, identical to whatever `float('nan')` yields. Since the [IEEE-754 standard](https://en.wikipedia.org/wiki/IEEE_754) demands it, both `math.nan` and `float('nan')` fail to compare as equal against any numeric value whatsoever — themselves included. When you want to determine if some value is NaN, rely on the `isnan()` function to screen for NaNs rather than reaching for `is` or `==`. Example:

```python
>>> import math
>>> math.nan == math.nan
False
>>> float('nan') == float('nan')
False
>>> math.isnan(math.nan)
True
>>> math.isnan(float('nan'))
True

```

Added in version 3.5.

Changed in version 3.11: From this release onward it is provided unconditionally.

**CPython implementation detail:** For the most part, the `math` module is a collection of slim shims over whatever C math routines the underlying platform supplies. In unusual situations its behavior tracks Annex F of the C99 standard wherever that applies. As things stand now, the code raises [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) when an operation is invalid — `sqrt(-1.0)` or `log(0.0)`, say, cases where C99 Annex F suggests flagging an invalid operation or a divide-by-zero — and raises [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) whenever a result is too large to represent (`exp(1000.0)`, for instance). None of the functions listed above hands back a NaN unless at least one supplied argument already was a NaN; when that happens, the typical outcome is a NaN, though (once more in line with C99 Annex F) a handful of cases break that pattern, such as `pow(float('nan'), 0.0)` or `hypot(float('nan'), float('inf'))`.

Keep in mind that Python does nothing to tell signaling NaNs apart from quiet NaNs, and what happens with signaling NaNs is left undefined. In practice, all NaNs tend to be handled as if they were quiet.

See also

Module [`cmath`](https://docs.python.org/3.14/library/cmath.html#module-cmath)

Provides complex-number counterparts for a good many of the functions here.

[Subject index](INDEX.md)
