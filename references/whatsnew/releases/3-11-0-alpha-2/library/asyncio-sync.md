# Python 3.11.0 alpha 2 / library / asyncio sync

[bpo-45416](https://bugs.python.org/issue?@action=redirect&bpo=45416): Repair the use of [`asyncio.Condition`](https://docs.python.org/3.14/library/asyncio-sync.html#asyncio.Condition) together with explicit [`asyncio.Lock`](https://docs.python.org/3.14/library/asyncio-sync.html#asyncio.Lock) objects, a regression stemming from the removal of explicit loop arguments. Joongi Kim wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
