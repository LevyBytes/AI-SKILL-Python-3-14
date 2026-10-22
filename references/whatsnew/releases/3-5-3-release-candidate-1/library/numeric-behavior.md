# Python 3.5.3 release candidate 1 / library / numeric behavior

[bpo-27760](https://bugs.python.org/issue?@action=redirect&bpo=27760): Closed a possible integer overflow within binascii.b2a_qp.

[bpo-27939](https://bugs.python.org/issue?@action=redirect&bpo=27939): Repair defects in tkinter.ttk.LabeledScale and tkinter.Scale that stemmed from holding the scale as a float internally in Tk. tkinter.IntVar now functions when a float value is assigned to the underlying Tk variable.

[bpo-28253](https://bugs.python.org/issue?@action=redirect&bpo=28253): Repair calendar functions for the extreme months 0001-01 and 9999-12. The itermonthdays() and itermonthdays2() methods are rewritten so they avoid calling itermonthdates(), which could provoke a datetime.date under/overflow.

[bpo-28019](https://bugs.python.org/issue?@action=redirect&bpo=28019): itertools.count() no longer rounds a non-integer step that falls between 1.0 and 2.0 down to 1.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
