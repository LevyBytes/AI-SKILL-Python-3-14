# Python 3.14.0 beta 2 / library / math

[gh-132876](https://github.com/python/cpython/issues/132876): On Windows prior to Windows 11, `ldexp()` fails to round subnormal results even though it ought to. Python's [`math.ldexp()`](https://docs.python.org/3.14/library/math.html#math.ldexp) wrapper now performs that rounding, so for the rare very small results outcomes can shift slightly on Windows releases before 11.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
