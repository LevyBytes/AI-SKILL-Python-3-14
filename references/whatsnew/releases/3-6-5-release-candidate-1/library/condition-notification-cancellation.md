# Python 3.6.5 release candidate 1 / library / condition notification cancellation

[bpo-32841](https://bugs.python.org/issue?@action=redirect&bpo=32841): Repaired an `asyncio.Condition` defect that quietly dropped cancellation once a conditional lock had been notified and then cancelled. Bar Harel sent the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
