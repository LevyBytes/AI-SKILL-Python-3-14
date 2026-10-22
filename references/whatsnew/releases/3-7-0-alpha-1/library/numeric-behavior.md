# Python 3.7.0 alpha 1 / library / numeric behavior

[bpo-28253](https://bugs.python.org/issue?@action=redirect&bpo=28253): Repaired calendar routines for the extreme months 0001-01 and 9999-12. The itermonthdays() and itermonthdays2() methods were rewritten so they avoid calling itermonthdates(), which is capable of producing datetime.date under/overflow.

[bpo-18219](https://bugs.python.org/issue?@action=redirect&bpo=18219): Made csv.DictWriter faster when there are a large number of columns. Mariatta Wijaya provided the patch.

[bpo-27863](https://bugs.python.org/issue?@action=redirect&bpo=27863): A number of ElementTree crashes stemming from race conditions and incorrect types were corrected.

[bpo-28740](https://bugs.python.org/issue?@action=redirect&bpo=28740): Introduced sys.getandroidapilevel(), which returns Android's build-time API version as an integer. The function exists only on Android.

[bpo-27939](https://bugs.python.org/issue?@action=redirect&bpo=27939): Repaired defects in tkinter.ttk.LabeledScale plus tkinter.Scale that stemmed from holding the scale internally as a float in Tk. tkinter.IntVar now functions whenever a float value gets assigned to the backing Tk variable.

[bpo-24700](https://bugs.python.org/issue?@action=redirect&bpo=24700): Tune array.array comparison. Comparing arrays that hold values of the same integer type is now anywhere from 10x up to 70x faster.

[bpo-26732](https://bugs.python.org/issue?@action=redirect&bpo=26732): Repair the excess of fds in processes launched through the "forkserver" method. A child process would inherit fds equal in number to the still-running children.

[bpo-30589](https://bugs.python.org/issue?@action=redirect&bpo=30589): With the “forkserver” method, multiprocessing.Process.exitcode was corrected so that a process terminated by a signal yields the negated signal number rather than 255.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
