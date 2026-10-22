# Python 3.11.0 beta 1 / core and builtins / pickle

[bpo-46962](https://bugs.python.org/issue?@action=redirect&bpo=46962): Some classes and functions used to declare their docstrings without regard to the `--without-doc-strings` compilation flag; that unconditional behavior is gone.

The classes that changed are `ctypes.UnionType`, [`pickle.PickleBuffer`](https://docs.python.org/3.14/library/pickle.html#pickle.PickleBuffer), `testcapi.RecursingInfinitelyError`, and [`types.GenericAlias`](https://docs.python.org/3.14/library/types.html#types.GenericAlias).

Among the functions, 24 methods in [`ctypes`](https://docs.python.org/3.14/library/ctypes.html#module-ctypes) are affected.

Oleg Iarygin authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
