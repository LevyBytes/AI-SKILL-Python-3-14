# Python 3.6.0 alpha 2 / idle / warnings

[bpo-27196](https://bugs.python.org/issue?@action=redirect&bpo=27196): Silence the "ThemeChanged" warnings that appeared while the IDLE test suite ran. They lingered even after #20567 quieted the other warnings. The fix applies Serhiy Storchaka's update_idletasks approach across four of the test modules, and the extra guidance went into idle_test/README.txt.

[bpo-20567](https://bugs.python.org/issue?@action=redirect&bpo=20567): Rework idle_test/README.txt so it explains how to keep tk from emitting warnings during tests. That guidance then gets applied across several of the IDLE tests.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
