# Python 3.7.0 alpha 1 / core and builtins / calling sys getsizeof code object reports size covering code struct

[bpo-12414](https://bugs.python.org/issue?@action=redirect&bpo=12414): Calling sys.getsizeof() on a code object now reports a size covering the code struct together with the sizes of the objects it points at. Donghee Na provided the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
