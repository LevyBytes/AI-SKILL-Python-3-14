# Python 3.12.0 alpha 4 / library / calling inspect signature mock objects used raise typeerror

[gh-96127](https://github.com/python/cpython/issues/96127): Calling `inspect.signature` on mock objects used to raise `TypeError`. It now properly returns the inferred signature `(*args, **kwargs)`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
