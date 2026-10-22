# Python 3.10.0 alpha 1 / core and builtins / type

[bpo-40217](https://bugs.python.org/issue?@action=redirect&bpo=40217): Objects of types built with [`PyType_FromSpecWithBases()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromSpecWithBases) will no longer visit their class object automatically while the garbage collector traverses references. Visiting that object's class is now the user's responsibility. Pablo Galindo authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
