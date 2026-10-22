# Python 3.6.5 release candidate 1 / core and builtins / build and platforms

[bpo-32650](https://bugs.python.org/issue?@action=redirect&bpo=32650): Pdb, and the other debuggers that build on bpo bdb.py, will step over (the next command) native coroutines correctly. Pablo Galindo wrote the patch.

[bpo-27169](https://bugs.python.org/issue?@action=redirect&bpo=27169): At compile time the `__debug__` constant now gets optimized away. As a side effect this also resolves [bpo-22091](https://bugs.python.org/issue?@action=redirect&bpo=22091).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
