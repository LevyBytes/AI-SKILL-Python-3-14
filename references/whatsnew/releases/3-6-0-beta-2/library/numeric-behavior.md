# Python 3.6.0 beta 2 / library / numeric behavior

[bpo-28253](https://bugs.python.org/issue?@action=redirect&bpo=28253): Corrected the calendar functions at the boundary months 0001-01 and 9999-12. The itermonthdays() and itermonthdays2() methods were rewritten to avoid calling itermonthdates(), which could trigger datetime.date under/overflow.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
