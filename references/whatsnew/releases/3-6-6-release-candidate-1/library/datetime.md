# Python 3.6.6 release candidate 1 / library / datetime

[bpo-33812](https://bugs.python.org/issue?@action=redirect&bpo=33812): A datetime instance d whose tzinfo is not None, yet where d.tzinfo.utcoffset(d) yields None, is now handled as naive by the astimezone() method.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
