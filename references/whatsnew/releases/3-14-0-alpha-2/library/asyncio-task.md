# Python 3.14.0 alpha 2 / library / asyncio task

[gh-126138](https://github.com/python/cpython/issues/126138): Resolve a use-after-free crash affecting [`asyncio.Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) objects whose wrapped coroutine yields some object carrying a malicious [`__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__). Nico Posada authored the patch.

[gh-126080](https://github.com/python/cpython/issues/126080): Resolve a use-after-free crash affecting [`asyncio.Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) objects whose backing event loop carries a malicious [`__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__). Nico-Posada filed the report; Bénédikt Tran wrote the patch.

[gh-126083](https://github.com/python/cpython/issues/126083): Closed a reference leak affecting [`asyncio.Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) objects whenever the same object is reinitialized using a non-`None` context. Nico Posada authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
