# Python 3.14.0 beta 4 / library / sys

[gh-135645](https://github.com/python/cpython/issues/135645): A `supports_isolated_interpreters` field was added to [`sys.implementation`](https://docs.python.org/3.14/library/sys.html#sys.implementation).

[gh-135487](https://github.com/python/cpython/issues/135487): `reprlib.Repr.repr_int()` was fixed for integers carrying more than [`sys.get_int_max_str_digits()`](https://docs.python.org/3.14/library/sys.html#sys.get_int_max_str_digits) digits. Bénédikt Tran authored this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
