# Python 3.10.0 alpha 2 / core and builtins / typeobj

[bpo-41902](https://bugs.python.org/issue?@action=redirect&bpo=41902): A small optimization when computing [`sq_item`](https://docs.python.org/3.14/c-api/typeobj.html#c.PySequenceMethods.sq_item) and [`mp_subscript`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyMappingMethods.mp_subscript) for [`range`](https://docs.python.org/3.14/library/stdtypes.html#range). Donghee Na supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
