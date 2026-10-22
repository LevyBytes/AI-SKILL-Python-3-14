# Python 3.6.0 alpha 1 / library / imports and modules

[bpo-25771](https://bugs.python.org/issue?@action=redirect&bpo=25771): Adjusted how the error message reads for importlib.util.resolve_name() in the situation where "package" goes unspecified yet is required.

[bpo-25203](https://bugs.python.org/issue?@action=redirect&bpo=25203): A failed readline.set_completer_delims() call no longer leaves the module sitting in an inconsistent state.

[bpo-26367](https://bugs.python.org/issue?@action=redirect&bpo=26367): Just like builtins.__import__(), importlib.__import__() now raises ImportError whenever `level` is supplied without a companion package being supplied.

[bpo-26069](https://bugs.python.org/issue?@action=redirect&bpo=26069): Took out the deprecated apis from the trace module.

[bpo-25584](https://bugs.python.org/issue?@action=redirect&bpo=25584): Within the glob module, "escape" was added onto the __all__ list.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
