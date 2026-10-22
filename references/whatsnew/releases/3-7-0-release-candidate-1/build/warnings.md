# Python 3.7.0 release candidate 1 / build / warnings

[bpo-5755](https://bugs.python.org/issue?@action=redirect&bpo=5755): Relocate the `-Wstrict-prototypes` option into `CFLAGS_NODIST` away from `OPT`. That option threw irritating warnings while building extension modules authored in C++.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
