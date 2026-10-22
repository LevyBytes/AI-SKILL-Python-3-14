# Python 3.10.0 alpha 7 / core and builtins / imports and modules

[bpo-42134](https://bugs.python.org/issue?@action=redirect&bpo=42134): The import system now raises ImportWarning whenever it calls find_module().

[bpo-42137](https://bugs.python.org/issue?@action=redirect&bpo=42137): For `ModuleType.__repr__`, the import system now favors `__spec__` ahead of `module_repr()`.

[bpo-43517](https://bugs.python.org/issue?@action=redirect&bpo=43517): Corrected a misdetection of circular imports triggered by `from pkg.mod import attr`, which produced false positives in non-trivial multi-threaded code.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
