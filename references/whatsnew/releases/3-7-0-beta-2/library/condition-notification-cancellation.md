# Python 3.7.0 beta 2 / library / condition notification cancellation

[bpo-32841](https://bugs.python.org/issue?@action=redirect&bpo=32841): Corrected an `asyncio.Condition` issue that quietly disregarded cancellation following the notify-and-cancel of a conditional lock. Patch by Bar Harel.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
