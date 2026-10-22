# Python 3.13.0 alpha 1 / core and builtins / exceptions and tracebacks

[gh-106898](https://github.com/python/cpython/issues/106898): Supply the exception via the third positional argument to `PY_UNIND` callbacks under `sys.monitoring`. With this, the `PY_UNWIND` callback now lines up with the remaining exception-handling callbacks.

[gh-105979](https://github.com/python/cpython/issues/105979): Fix crash in `_imp.get_frozen_object()` traced to faulty exception handling.

[gh-110696](https://github.com/python/cpython/issues/110696): The wrong error message produced for invalid argument unpacking was corrected. Pablo Galindo wrote the patch

[gh-108654](https://github.com/python/cpython/issues/108654): Locals that an inlined comprehension had shadowed are now restored if that comprehension raises an exception.

[gh-107944](https://github.com/python/cpython/issues/107944): The error message for function calls that carry bad keyword arguments was improved. Pablo Galindo wrote the patch

[gh-96663](https://github.com/python/cpython/issues/96663): Provide a clearer, more introspect-able error message when assigning attributes on classes that have neither a `__dict__` nor a slot member for the attribute.

[gh-108390](https://github.com/python/cpython/issues/108390): An exception is now raised when a non-local event (`RAISE`, `EXCEPTION_HANDLED`, etc.) is set within `sys.monitoring.set_local_events`.

This also fixes a crash that occurred while tracing during recursive calls to Python classes.

[gh-100964](https://github.com/python/cpython/issues/100964): A generator's exception state is now cleared after `return` so that reference cycles are broken.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
