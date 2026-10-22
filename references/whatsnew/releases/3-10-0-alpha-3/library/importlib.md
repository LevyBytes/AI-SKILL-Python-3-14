# Python 3.10.0 alpha 3 / library / importlib

[bpo-42403](https://bugs.python.org/issue?@action=redirect&bpo=42403): Streamline the [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) external bootstrap code: `importlib._bootstrap_external` now relies on ordinary imports for pulling in builtin modules. By the time it is imported, the builtin [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__) function already works completely and can therefore load builtin modules such as [`sys`](https://docs.python.org/3.14/library/sys.html#module-sys). Victor Stinner contributed the patch.

[bpo-26131](https://bugs.python.org/issue?@action=redirect&bpo=26131): The `load_module()` methods within `importlib` now raise a `DeprecationWarning`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
