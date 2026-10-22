# Python 3.12.0 alpha 2 / core and builtins / future

[gh-98811](https://github.com/python/cpython/issues/98811): Rely on full source positions to make it easier to spot `__future__` imports placed somewhere other than the file's start. This also fixes a one-off error in the offset of the exception raised in a particular scenario, which had been blocking correct highlighting.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
