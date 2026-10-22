# Python 3.7.0 alpha 4 / library / speed up asyncio future schedule add remove callback

[bpo-32348](https://bugs.python.org/issue?@action=redirect&bpo=32348): Speed up asyncio.Future schedule/add/remove callback. That optimization yields 3-6% performance gains for async/await code.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
