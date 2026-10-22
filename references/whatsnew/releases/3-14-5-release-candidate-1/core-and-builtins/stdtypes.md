# Python 3.14.5 release candidate 1 / core and builtins / stdtypes

[gh-148390](https://github.com/python/cpython/issues/148390): Correct undefined behavior in [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) involving the native boolean format (`?`) passed to [`cast()`](https://docs.python.org/3.14/library/stdtypes.html#memoryview.cast). Formerly, on several widespread platforms, `memoryview(b).cast("?").tolist()` wrongly gave `[False]` rather than `[True]` for any even byte *b*. Bénédikt Tran wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
