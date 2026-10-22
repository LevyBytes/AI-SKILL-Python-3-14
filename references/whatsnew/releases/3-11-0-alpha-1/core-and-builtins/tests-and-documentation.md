# Python 3.11.0 alpha 1 / core and builtins / tests and documentation

[bpo-43918](https://bugs.python.org/issue?@action=redirect&bpo=43918): Documented the signature plus the `default` argument inside the docstring of the new `anext` builtin.

[bpo-44636](https://bugs.python.org/issue?@action=redirect&bpo=44636): Equal types in a union now collapse together. For instance, `int | int` now yields `int`. Comparison of the union type against non-hashable values is also fixed. For example, `int | str == {}` no longer raises a TypeError.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
