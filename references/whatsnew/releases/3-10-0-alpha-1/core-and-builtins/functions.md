# Python 3.10.0 alpha 1 / core and builtins / functions

[bpo-40636](https://bugs.python.org/issue?@action=redirect&bpo=40636): [`zip()`](https://docs.python.org/3.14/library/functions.html#zip) now honors the `strict` parameter from [**PEP 618**](https://peps.python.org/pep-0618/), raising a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) should the arguments run out at unequal lengths. Brandt Bucher contributed the patch.

[bpo-41909](https://bugs.python.org/issue?@action=redirect&bpo=41909): Repaired a stack overflow in [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass) and [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) arising when reading the `__bases__` attribute spirals into infinite recursion.

[bpo-41342](https://bugs.python.org/issue?@action=redirect&bpo=41342): When handed an integer, [`round()`](https://docs.python.org/3.14/library/functions.html#round) now runs faster (9–60%).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
