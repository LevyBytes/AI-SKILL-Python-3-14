# Python 3.11.0 alpha 1 / library / numbers

[bpo-45034](https://bugs.python.org/issue?@action=redirect&bpo=45034): Reworks how the error reads for `struct.pack` under the `'H'` and `'h'` modes when the supplied numbers are too large or too small. The message now spells out the genuine numeric limits, whereas before it displayed arithmetic expressions.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
