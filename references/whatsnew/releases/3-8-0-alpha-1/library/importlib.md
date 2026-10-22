# Python 3.8.0 alpha 1 / library / importlib

[bpo-21446](https://bugs.python.org/issue?@action=redirect&bpo=21446): The `reload` fixer has switched to [`importlib.reload()`](https://docs.python.org/3.14/library/importlib.html#importlib.reload) in place of the deprecated `imp.reload()`.

[bpo-35024](https://bugs.python.org/issue?@action=redirect&bpo=35024): `importlib` no longer redundantly logs `wrote <bytecode path>` once `(created|could not create) <bytecode path>` has already been logged. Patch by Quentin Agren.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
