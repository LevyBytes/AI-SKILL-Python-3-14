# Python 3.9.0 alpha 5 / library / sys

[bpo-35370](https://bugs.python.org/issue?@action=redirect&bpo=35370): A denied "sys.setprofile" or "sys.settrace" audit event is now correctly surfaced as a [`PySys_Audit()`](https://docs.python.org/3.14/c-api/sys.html#c.PySys_Audit) error by sys.settrace(), sys.setprofile() and _lsprof.Profiler.enable().

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
