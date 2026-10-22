# Python 3.11.0 alpha 2 / c api / intro

[bpo-35134](https://bugs.python.org/issue?@action=redirect&bpo=35134): The non-limited API headers `cellobject.h`, `classobject.h`, `context.h`, `funcobject.h`, `genobject.h` and `longintrepr.h` now reside in the `Include/cpython` directory. On top of that, the `eval.h` header was deleted. You should not include these files on their own, since `Python.h` already pulls them in: [Include Files](https://docs.python.org/3.14/c-api/intro.html#api-includes). Where such a direct include exists, switch to including `Python.h` instead. Victor Stinner contributed the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
