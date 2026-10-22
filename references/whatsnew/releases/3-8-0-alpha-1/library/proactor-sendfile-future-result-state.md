# Python 3.8.0 alpha 1 / library / corrected asyncio proactoreventloop sendfile refrain setting result internal future future already

[bpo-35682](https://bugs.python.org/issue?@action=redirect&bpo=35682): Corrected `asyncio.ProactorEventLoop.sendfile()`: refrain from setting the result of an internal future when that future is already done.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
