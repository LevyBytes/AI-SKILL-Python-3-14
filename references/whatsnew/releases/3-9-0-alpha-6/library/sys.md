# Python 3.9.0 alpha 6 / library / sys

[bpo-40050](https://bugs.python.org/issue?@action=redirect&bpo=40050): Repair `importlib._bootstrap_external`: skip building a fresh `winreg` builtin module when one is already present in [`sys.modules`](https://docs.python.org/3.14/library/sys.html#sys.modules), and strip out duplicate imports.

[bpo-38410](https://bugs.python.org/issue?@action=redirect&bpo=38410): Handle [`sys.audit()`](https://docs.python.org/3.14/library/sys.html#sys.audit) failures correctly within [`sys.set_asyncgen_hooks()`](https://docs.python.org/3.14/library/sys.html#sys.set_asyncgen_hooks).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
