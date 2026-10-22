# Python 3.5.2 release candidate 1 / idle / warnings

[bpo-27196](https://bugs.python.org/issue?@action=redirect&bpo=27196): Silenced the "ThemeChanged" warnings raised while IDLE tests run. They lingered even after #20567 had quieted other warnings. Serhiy Storchaka's update_idletasks fix was applied across four test files. The extra guidance is noted in idle_test/README.txt

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
