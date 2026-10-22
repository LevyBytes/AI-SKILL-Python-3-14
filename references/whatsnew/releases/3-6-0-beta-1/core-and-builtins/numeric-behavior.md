# Python 3.6.0 beta 1 / core and builtins / numeric behavior

[bpo-25604](https://bugs.python.org/issue?@action=redirect&bpo=25604): Corrects a small integer-true-division bug that might have yielded off-by-one-ulp results on platforms whose ldexp implementations are unreliable.

[bpo-27662](https://bugs.python.org/issue?@action=redirect&bpo=27662): Corrects an overflow check within `List_New`: the original code compared against `Py_SIZE_MAX` rather than the proper upper bound `Py_SSIZE_T_MAX`. Xiang Zhang wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
