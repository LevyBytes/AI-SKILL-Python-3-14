# Python 3.14.0 alpha 3 / core and builtins / stdtypes

[gh-127740](https://github.com/python/cpython/issues/127740): The [`bytes.fromhex()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.fromhex) error text now states clearly that an even count of hexadecimal digits is needed, fixing the wording shown for an odd number of digits.

[gh-127085](https://github.com/python/cpython/issues/127085): On the [free-threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) build, close the race that arose while exporting a buffer out of a [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) object.

[gh-126980](https://github.com/python/cpython/issues/126980): Stop [`__buffer__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__buffer__) on a [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) from crashing whenever [`READ`](https://docs.python.org/3.14/library/inspect.html#inspect.BufferFlags.READ) or [`WRITE`](https://docs.python.org/3.14/library/inspect.html#inspect.BufferFlags.WRITE) is supplied as a flag.

[gh-125420](https://github.com/python/cpython/issues/125420): Give [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) objects a new [`memoryview.index()`](https://docs.python.org/3.14/library/stdtypes.html#memoryview.index). Bénédikt Tran supplied the patch.

[gh-125420](https://github.com/python/cpython/issues/125420): Give [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) objects a new [`memoryview.count()`](https://docs.python.org/3.14/library/stdtypes.html#memoryview.count). Bénédikt Tran supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
