# Python 3.14.3 final / tests / resource

[gh-65784](https://github.com/python/cpython/issues/65784): regrtests gain a parametrized resource named `wantobjects`, letting Tkinter tests run under a chosen value of `tkinter.wantobjects`, such as `-u wantobjects=0`.

[bpo-31391](https://bugs.python.org/issue?@action=redirect&bpo=31391): test_xpickle was forward-ported from Python 2 into Python 3, and the resource was restored to the test's command line.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
