# Python 3.9.0 alpha 5 / windows / distutils

[bpo-38597](https://bugs.python.org/issue?@action=redirect&bpo=38597): When no redistributable version is on hand, `distutils` will from now on stop statically linking `vcruntime140.dll`. Every future CPython release will bundle a copy of this DLL so distributed extensions keep loading.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
