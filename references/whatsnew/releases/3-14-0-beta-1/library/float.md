# Python 3.14.0 beta 1 / library / float

[gh-130317](https://github.com/python/cpython/issues/130317): [`PyFloat_Pack2()`](https://docs.python.org/3.14/c-api/float.html#c.PyFloat_Pack2) and [`PyFloat_Unpack2()`](https://docs.python.org/3.14/c-api/float.html#c.PyFloat_Unpack2) are fixed for NaN's carrying a payload. The round-trip through [`struct.unpack()`](https://docs.python.org/3.14/library/struct.html#struct.unpack) and [`struct.pack()`](https://docs.python.org/3.14/library/struct.html#struct.pack) is corrected for the IEEE 754 binary16 "half precision" type. Sergey B Kirpichev wrote this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
