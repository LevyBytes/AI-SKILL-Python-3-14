# Python 3.11.0 alpha 4 / library / functools

[bpo-46032](https://bugs.python.org/issue?@action=redirect&bpo=46032): For [`functools.singledispatch()`](https://docs.python.org/3.14/library/functools.html#functools.singledispatch) functions, the `registry()` method now inspects the first argument or the first parameter annotation and raises a TypeError when it is unsupported. Formerly the unsupported “types” were either silently skipped (for example `typing.List[int]`) or produced an error only at call time (for example `list[int]`).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
