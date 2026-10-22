# Python 3.14.0 alpha 3 / security / asyncio protocol

[gh-127655](https://github.com/python/cpython/issues/127655): Resolved a problem in which the `asyncio.selector_events._SelectorSocketTransport` transport neglected to pause protocol writes once the buffer hit the high water mark while [`asyncio.WriteTransport.writelines()`](https://docs.python.org/3.14/library/asyncio-protocol.html#asyncio.WriteTransport.writelines) was in use.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
