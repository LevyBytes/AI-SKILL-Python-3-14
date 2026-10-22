# Python 3.13.0 alpha 4 / library / threading

[gh-109653](https://github.com/python/cpython/issues/109653): Trim the import time of the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module by roughly 50%. Daniel Hollas wrote the patch.

[gh-114315](https://github.com/python/cpython/issues/114315): Turn [`threading.Lock`](https://docs.python.org/3.14/library/threading.html#threading.Lock) into a genuine class instead of a factory function. A `__new__` was added to the `_thread.lock` type.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
