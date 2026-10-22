# Python 3.11.0 alpha 2 / library / inspect

[bpo-45406](https://bugs.python.org/issue?@action=redirect&bpo=45406): Have [`inspect.getmodule()`](https://docs.python.org/3.14/library/inspect.html#inspect.getmodule) trap the `FileNotFoundError` thrown by `inspect.getabsfile()` and return `None` to signal that the module was indeterminate.

[bpo-45320](https://bugs.python.org/issue?@action=redirect&bpo=45320): Dropped from the [`inspect`](https://docs.python.org/3.14/library/inspect.html#module-inspect) module:

  - the `getargspec` function, marked deprecated since Python 3.0;

reach for [`inspect.signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature) or [`inspect.getfullargspec()`](https://docs.python.org/3.14/library/inspect.html#inspect.getfullargspec) in its place.

  - the `formatargspec` function, marked deprecated since Python 3.5; rely on the [`inspect.signature()`](https://docs.python.org/3.14/library/inspect.html#inspect.signature) function and a `Signature` object directly.

  - the undocumented `Signature.from_builtin` and `Signature.from_function` functions, marked deprecated since Python 3.5; reach for the [`Signature.from_callable()`](https://docs.python.org/3.14/library/inspect.html#inspect.Signature.from_callable) method in their place.

Hugo van Kemenade wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
