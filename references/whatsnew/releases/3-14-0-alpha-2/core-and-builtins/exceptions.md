# Python 3.14.0 alpha 2 / core and builtins / exceptions

[gh-123930](https://github.com/python/cpython/issues/123930): Sharpen the message reported when a script that shadows a standard library module triggers [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError) during a "from" import. In the same spirit, sharpen the message when a script that shadows a third party module tries to "from" import an attribute out of that third party module before it has finished initialising.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
