# Python 3.8.0 alpha 1 / library / condition notification cancellation

[bpo-32841](https://bugs.python.org/issue?@action=redirect&bpo=32841): Repaired an `asyncio.Condition` issue that quietly swallowed cancellation after a conditional lock was notified and cancelled. Patch by Bar Harel.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
