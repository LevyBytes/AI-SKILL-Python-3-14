# Python 3.14.0 alpha 2 / core and builtins / stdtypes

[gh-126012](https://github.com/python/cpython/issues/126012): Subscription is now accepted by the [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) type, turning it into a [generic type](https://docs.python.org/3.14/glossary.html#term-generic-type).

[gh-126341](https://github.com/python/cpython/issues/126341): Attempting to iterate across a released [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) object now throws [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) in place of [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
