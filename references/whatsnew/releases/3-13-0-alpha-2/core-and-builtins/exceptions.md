# Python 3.13.0 alpha 2 / core and builtins / exceptions

[gh-111666](https://github.com/python/cpython/issues/111666): Make [`BaseExceptionGroup.derive()`](https://docs.python.org/3.14/library/exceptions.html#BaseExceptionGroup.derive), [`BaseExceptionGroup.subgroup()`](https://docs.python.org/3.14/library/exceptions.html#BaseExceptionGroup.subgroup), and [`BaseExceptionGroup.split()`](https://docs.python.org/3.14/library/exceptions.html#BaseExceptionGroup.split) faster by altering the way their passed arguments are parsed.

[gh-111380](https://github.com/python/cpython/issues/111380): Fix a defect making [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning) show up twice during parsing when invalid syntax turns up later. Pablo galindo wrote the patch

[gh-110912](https://github.com/python/cpython/issues/110912): Render the traceback for [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) exceptions correctly via the [`traceback`](https://docs.python.org/3.14/library/traceback.html#module-traceback) module. Pablo Galindo wrote the patch

[gh-109894](https://github.com/python/cpython/issues/109894): Fixed a crash stemming from an improperly initialized static [`MemoryError`](https://docs.python.org/3.14/library/exceptions.html#MemoryError) inside a subinterpreter.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
