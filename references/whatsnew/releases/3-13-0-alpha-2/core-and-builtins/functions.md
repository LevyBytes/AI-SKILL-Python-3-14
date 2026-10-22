# Python 3.13.0 alpha 2 / core and builtins / functions

[gh-89519](https://github.com/python/cpython/issues/89519): Took out the chained [`classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod) descriptors that [bpo-19072](https://bugs.python.org/issue?@action=redirect&bpo=19072) had added. Wrapping other descriptors such as [`property`](https://docs.python.org/3.14/library/functions.html#property) with it is no longer possible. The feature's underlying design was flawed and spawned numerous downstream issues. For a "pass-through" `classmethod`, look to the `__wrapped__` attribute that arrived in Python 3.10.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
