# Python 3.8.0 alpha 1 / library / functions

[bpo-33251](https://bugs.python.org/issue?@action=redirect&bpo=33251): `ConfigParser.items()` got corrected so that key-value pairs supplied through [`vars()`](https://docs.python.org/3.14/library/functions.html#vars) stay out of the produced output.

[bpo-34441](https://bugs.python.org/issue?@action=redirect&bpo=34441): Corrected a crash that occurred when an `ABC`-derived class carrying an invalid `__subclasses__` was given as the second argument to [`issubclass()`](https://docs.python.org/3.14/library/functions.html#issubclass). Alexey Izbyshev wrote the patch.

[bpo-35619](https://bugs.python.org/issue?@action=redirect&bpo=35619): Strengthened handling of custom data descriptors throughout [`help()`](https://docs.python.org/3.14/library/functions.html#help) and [`pydoc`](https://docs.python.org/3.14/library/pydoc.html#module-pydoc).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
