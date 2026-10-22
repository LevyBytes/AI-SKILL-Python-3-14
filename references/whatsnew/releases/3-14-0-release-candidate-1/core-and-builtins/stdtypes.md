# Python 3.14.0 release candidate 1 / core and builtins / stdtypes

[gh-91153](https://github.com/python/cpython/issues/91153): Stop a crash that arose when a [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) is mutated concurrently during item assignment.

[gh-132661](https://github.com/python/cpython/issues/132661): Mirror a recent [**PEP 750**](https://peps.python.org/pep-0750/) change.

Forbid joining `string.templatelib.Template` with [`str`](https://docs.python.org/3.14/library/stdtypes.html#str). On top of that, forbid the implicit joining of t-string literals together with string or f-string literals.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
