# Python 3.10.0 alpha 1 / core and builtins / imports and modules

[bpo-41631](https://bugs.python.org/issue?@action=redirect&bpo=41631): The `_ast` module reverts to a global state. A per-instance module state introduces subtle, real-world breakage. As one case, the Mercurial project swaps out the `__import__()` function to provide lazy import, while Python assumed that running `import _ast` would always hand back a fully initialized `_ast` module.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
