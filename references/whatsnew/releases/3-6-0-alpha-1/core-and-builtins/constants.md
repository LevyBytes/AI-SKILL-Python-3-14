# Python 3.6.0 alpha 1 / core and builtins / constants

[bpo-26204](https://bugs.python.org/issue?@action=redirect&bpo=26204): The compiler now disregards every constant statement, not merely str and int — the full set being bytes, str, int, float, complex, the name constants None, False and True, plus Ellipsis and ast.Constant. As an illustration, `1.0` is now ignored in `def f(): 1.0`.

[bpo-25843](https://bugs.python.org/issue?@action=redirect&bpo=25843): During code compilation, refrain from merging constants whenever they are equal yet carry different types. For instance, `f1, f2 = lambda: 1, lambda: 1.0` now compiles correctly into two separate functions: `f1()` returns `1` (`int`) while `f2()` returns `1.0` (`float`), even though `1` and `1.0` compare equal.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
