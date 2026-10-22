# Python 3.8.0 alpha 1 / library / multiprocessing pool enter raises pool not running pool raises if entered

[bpo-35477](https://bugs.python.org/issue?@action=redirect&bpo=35477): `multiprocessing.Pool.__enter__()` now raises when the pool is not running: `with pool:` raises if it is entered more than once.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
