# Python 3.7.0 beta 1 / library / collections and iteration

[bpo-30306](https://bugs.python.org/issue?@action=redirect&bpo=30306): contextlib.contextmanager now frees the arguments handed to the underlying generator the moment the context manager is entered. Formerly it would hold them alive as long as the context manager stayed alive, even while it was not serving as a function decorator. Patch by Martin Teichmann.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
