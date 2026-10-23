# What's New In Python 3.3 / contextlib - contextlib, threading

### contextlib

For programmatically driving context managers and comparable cleanup work, [`ExitStack`](https://docs.python.org/3.14/library/contextlib.html#contextlib.ExitStack) now offers a sturdy base. The earlier `contextlib.nested` API was deprecated and removed; by contrast, this new API behaves correctly whether a context manager grabs its resources within its `__init__` method (file objects, say) or within its `__enter__` method (for instance synchronisation objects out of the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module).

([bpo-13585](https://bugs.python.org/issue?@action=redirect&bpo=13585))

[Subject index](INDEX.md) · [Previous source section](collections.md) · [Next source section](crypt.md) · [Release/subject declaration](summary-release-highlights.md)
