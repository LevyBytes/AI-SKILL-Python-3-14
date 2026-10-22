# Python 3.13.0 alpha 2 / library / functions and types

[gh-110771](https://github.com/python/cpython/issues/110771): Surface the setup and teardown halves of `asyncio.run_forever()` through the standalone `asyncio.run_forever_setup()` and `asyncio.run_forever_cleanup()` methods. With these, GUI event loops can integrate more closely.

[gh-110196](https://github.com/python/cpython/issues/110196): Give `IPv6Address` a `__reduce__` method so that `scope_id` is retained

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
