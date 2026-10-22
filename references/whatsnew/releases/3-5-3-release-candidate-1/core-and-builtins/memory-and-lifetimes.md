# Python 3.5.3 release candidate 1 / core and builtins / memory and lifetimes

[bpo-27942](https://bugs.python.org/issue?@action=redirect&bpo=27942): Repair a memory leak in codeobject.c

[bpo-28147](https://bugs.python.org/issue?@action=redirect&bpo=28147): Repair a memory leak affecting split-table dictionaries: setattr() must avoid converting a combined table into a split one.

[bpo-23782](https://bugs.python.org/issue?@action=redirect&bpo=23782): Repair a possible memory leak in _PyTraceback_Add() along with exception loss in PyTraceBack_Here().

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
