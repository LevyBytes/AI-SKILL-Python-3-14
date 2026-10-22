# Python 3.11.0 alpha 5 / core and builtins / functions

[bpo-46527](https://bugs.python.org/issue?@action=redirect&bpo=46527): The `iterable` argument may once more be supplied to [`enumerate()`](https://docs.python.org/3.14/library/functions.html#enumerate) by keyword. Jelle Zijlstra wrote the patch.

[bpo-46564](https://bugs.python.org/issue?@action=redirect&bpo=46564): Skip building frame objects while constructing a [`super`](https://docs.python.org/3.14/library/functions.html#super) object. Kumar Aditya wrote the patch.

[bpo-44977](https://bugs.python.org/issue?@action=redirect&bpo=44977): Handing [`int()`](https://docs.python.org/3.14/library/functions.html#int) off to `__trunc__()` is now deprecated. Invoking `int(a)` where `type(a)` provides `__trunc__()` yet lacks `__int__()` or `__index__()` now triggers a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
