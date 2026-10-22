# Python 3.14.0 alpha 2 / library / asyncio future

[gh-125984](https://github.com/python/cpython/issues/125984): Resolve use-after-free crashes affecting [`asyncio.Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future) objects whose backing event loop carries a malicious [`__getattribute__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__getattribute__). Nico-Posada filed the report; Bénédikt Tran wrote the patch.

[gh-125966](https://github.com/python/cpython/issues/125966): Resolve a use-after-free crash within [`asyncio.Future.remove_done_callback()`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future.remove_done_callback). Bénédikt Tran wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
