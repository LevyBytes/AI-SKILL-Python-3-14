# Python 3.10.0 alpha 5 / library / sys

[bpo-42955](https://bugs.python.org/issue?@action=redirect&bpo=42955): Introduce [`sys.stdlib_module_names`](https://docs.python.org/3.14/library/sys.html#sys.stdlib_module_names), which holds the names of the standard library modules. Victor Stinner contributed the patch.

[bpo-42923](https://bugs.python.org/issue?@action=redirect&bpo=42923): On a fatal error, both the [`Py_FatalError()`](https://docs.python.org/3.14/c-api/sys.html#c.Py_FatalError) function and the [`faulthandler`](https://docs.python.org/3.14/library/faulthandler.html#module-faulthandler) module now dump out the extension modules that are loaded.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
