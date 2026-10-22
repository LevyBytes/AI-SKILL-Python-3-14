# Affected APIs

### Affected APIs

The cap reaches only the potentially slow conversions between [`int`](https://docs.python.org/3.14/library/functions.html#int) and `str` or `bytes`:

- `int(string)` using the default base 10.

- `int(string, base)` for every base that is not a power of 2.

- `str(integer)`.

- `repr(integer)`.

- every other string conversion targeting base 10, for instance `f"{integer}"`, `"{}".format(integer)`, or `b"%d" % integer`.

The cap does not reach functions whose algorithm is linear:

- `int(string, base)` using base 2, 4, 8, 16, or 32.

- `int.from_bytes()` and `int.to_bytes()`.

- [`hex()`](https://docs.python.org/3.14/library/functions.html#hex), [`oct()`](https://docs.python.org/3.14/library/functions.html#oct), [`bin()`](https://docs.python.org/3.14/library/functions.html#bin).

- [Format specification mini-language](https://docs.python.org/3.14/library/string.html#formatspec) covering hex, octal, and binary numbers.

- `str` to [`float`](https://docs.python.org/3.14/library/functions.html#float).

- `str` to [`decimal.Decimal`](https://docs.python.org/3.14/library/decimal.html#decimal.Decimal).

[Subject index](INDEX.md) · [Previous](integer-string-conversion-length-limitation.md) · [Continue](configuring-the-limit.md)
