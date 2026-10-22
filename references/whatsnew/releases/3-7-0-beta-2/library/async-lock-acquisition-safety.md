# Python 3.7.0 beta 2 / library / corrected asyncio lock safety problem permitted acquiring locking one lock

[bpo-32734](https://bugs.python.org/issue?@action=redirect&bpo=32734): Corrected an `asyncio.Lock()` safety problem that permitted acquiring and locking one lock several times over without it ever being freed. Patch by Bar Harel.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
