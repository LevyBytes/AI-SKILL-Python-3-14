# Python 3.14.6 final / core and builtins / sys

[gh-150633](https://github.com/python/cpython/issues/150633): Repair the frozen importer, which used to accept module names holding embedded null bytes; that flaw let it skip the [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules) cache and spawn duplicate module objects.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
