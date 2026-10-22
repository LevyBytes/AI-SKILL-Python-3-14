# Python 3.6.2 release candidate 1 / core and builtins / code object sys getsizeof reports sizes covering code struct together

[bpo-12414](https://bugs.python.org/issue?@action=redirect&bpo=12414): For a code object, sys.getsizeof() now reports sizes covering the code struct together with the sizes of the objects it points to. Donghee Na wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
