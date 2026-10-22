# Python 3.12.0 alpha 1 / core and builtins / whenever package does not match spec parent deprecationwarning raised place

[gh-65961](https://github.com/python/cpython/issues/65961): Whenever `__package__` does not match `__spec__.parent`, a `DeprecationWarning` is now raised in place of an `ImportWarning`.

Additionally, `importlib.util.set_package()`, which had been slated for removal, is now gone.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
