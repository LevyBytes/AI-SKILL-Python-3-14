# Python 3.11.0 alpha 1 / core and builtins / stdtypes

[bpo-28146](https://bugs.python.org/issue?@action=redirect&bpo=28146): Cleared up a confusing error message inside [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format).

[bpo-43413](https://bugs.python.org/issue?@action=redirect&bpo=43413): Subclass constructors of certain builtin classes (for example [`tuple`](https://docs.python.org/3.14/library/stdtypes.html#tuple), [`list`](https://docs.python.org/3.14/library/stdtypes.html#list), [`frozenset`](https://docs.python.org/3.14/library/stdtypes.html#frozenset)) will no longer take arbitrary keyword arguments. [reverted in 3.11a4] A subclass of [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) is now able to define a `__new__()` method carrying extra keyword parameters without also overriding `__init__()`.

[bpo-45155](https://bugs.python.org/issue?@action=redirect&bpo=45155): [`int.to_bytes()`](https://docs.python.org/3.14/library/stdtypes.html#int.to_bytes) and [`int.from_bytes()`](https://docs.python.org/3.14/library/stdtypes.html#int.from_bytes) now default the `byteorder` argument to `"big"`. The `length` argument of `int.to_bytes()` likewise defaults to `1`.

[bpo-24234](https://bugs.python.org/issue?@action=redirect&bpo=24234): Provide the `__bytes__()` special method on the [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) type, allowing a bytes object `b` to clear an `isinstance(b, typing.SupportsBytes)` check.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
