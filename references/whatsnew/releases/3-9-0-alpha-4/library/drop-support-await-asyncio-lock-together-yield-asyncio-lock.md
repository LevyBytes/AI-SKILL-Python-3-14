# Python 3.9.0 alpha 4 / library / drop support await asyncio lock together yield asyncio lock

[bpo-34793](https://bugs.python.org/issue?@action=redirect&bpo=34793): Drop support for `with (await asyncio.lock):` together with `with (yield from asyncio.lock):`. The same holds for `asyncio.Condition` and `asyncio.Semaphore`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
