# Python 3.8.0 beta 1 / library / sys

[bpo-36829](https://bugs.python.org/issue?@action=redirect&bpo=36829): Introduces the [`sys.unraisablehook()`](https://docs.python.org/3.14/library/sys.html#sys.unraisablehook) function, overridable to govern the treatment of "unraisable exceptions". The hook fires whenever an exception arises yet Python has no path to deal with it — say, when a destructor throws or while garbage collection runs ([`gc.collect()`](https://docs.python.org/3.14/library/gc.html#gc.collect)).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
