# Python 3.10.0 alpha 6 / security / functions and types

[bpo-36346](https://bugs.python.org/issue?@action=redirect&bpo=36346): The `PyArg_Parse*()` functions now raise `DeprecationWarning` whenever the `u` or `Z` format appears. Consult [**PEP 623**](https://peps.python.org/pep-0623/) for the details.

[bpo-42990](https://bugs.python.org/issue?@action=redirect&bpo=42990): A new `__builtins__` attribute on functions is now consulted to resolve builtin symbols during a function's execution, rather than peering into `__globals__['__builtins__']`. Mark Shannon and Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
