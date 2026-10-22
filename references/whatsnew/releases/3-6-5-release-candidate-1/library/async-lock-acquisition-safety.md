# Python 3.6.5 release candidate 1 / library / repaired asyncio lock safety flaw permitted acquiring locking one lock

[bpo-32734](https://bugs.python.org/issue?@action=redirect&bpo=32734): Repaired an `asyncio.Lock()` safety flaw that permitted acquiring and locking one lock repeatedly even while it was not free. Bar Harel supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
