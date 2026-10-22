# Python 3.11.0 alpha 5 / library / asyncio future

[bpo-26552](https://bugs.python.org/issue?@action=redirect&bpo=26552): Corrected the situation where a failing [`asyncio.ensure_future()`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.ensure_future) left the coroutine unclosed. Kumar Aditya supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
