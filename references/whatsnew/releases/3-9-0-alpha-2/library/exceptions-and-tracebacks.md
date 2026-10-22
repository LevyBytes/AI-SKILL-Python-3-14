# Python 3.9.0 alpha 2 / library / exceptions and tracebacks

[bpo-38859](https://bugs.python.org/issue?@action=redirect&bpo=38859): When a side_effects iterable is used up, AsyncMock now hands back StopAsyncIteration. Ever since PEP-479 it has been impossible to raise a StopIteration exception out of a coroutine.

[bpo-36820](https://bugs.python.org/issue?@action=redirect&bpo=36820): Break the cycle created when an exception is stored in socket.py, codeop.py and dyld.py, since via the `__traceback__` attribute they preserve not only the exception but user objects as well. Mario Corchero wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
