# Python 3.12.0 alpha 1 / windows / build and platforms

[bpo-46907](https://bugs.python.org/issue?@action=redirect&bpo=46907): Update Windows installer to use SQLite 3.38.4.

[bpo-38704](https://bugs.python.org/issue?@action=redirect&bpo=38704): Prevent installation on unsupported Windows versions.

[gh-90989](https://github.com/python/cpython/issues/90989): The [Python install manager](https://docs.python.org/3.14/using/windows.html#launcher) now defaults to a per-user install (unless an all users install is already present), and some installer wording was made clearer.

[gh-95587](https://github.com/python/cpython/issues/95587): Resolves cases where, during an upgrade, the Windows installer would misjudge particular features belonging to an existing install.

[gh-95285](https://github.com/python/cpython/issues/95285): Repairs the way the [Python install manager](https://docs.python.org/3.14/using/windows.html#launcher) deals with command lines that hand it only a short executable name.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
