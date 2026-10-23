# What's New In Python 3.7 / Notable changes in Python 3.7.1 - tokenize

### Notable changes in Python 3.7.1

Beginning with 3.7.1, [`Py_Initialize()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Initialize) at present reliably reads and honors the very same environment settings as [`Py_Main()`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_Main) (under earlier Python releases it honored a poorly defined subset of those environment variables, whereas in Python 3.7.0 it read none of them owing to [bpo-34247](https://bugs.python.org/issue?@action=redirect&bpo=34247)). Should this behavior be undesirable, assign 1 to [`Py_IgnoreEnvironmentFlag`](https://docs.python.org/3.14/c-api/interp-lifecycle.html#c.Py_IgnoreEnvironmentFlag) before you call `Py_Initialize()`.

Within 3.7.1 the C API governing Context Variables [was updated](https://docs.python.org/3.14/c-api/contextvars.html#contextvarsobjects-pointertype-change) so it now uses [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) pointers. Consult also [bpo-34762](https://bugs.python.org/issue?@action=redirect&bpo=34762).

Within 3.7.1 the [`tokenize`](https://docs.python.org/3.14/library/tokenize.html#module-tokenize) module at present silently produces a `NEWLINE` token when handed input lacking a trailing new line. Such behavior at this point lines up with what the C tokenizer carries out internally. Ammar Askar contributed this through [bpo-33899](https://bugs.python.org/issue?@action=redirect&bpo=33899).

[Subject index](INDEX.md) · [Previous source section](cpython-implementation-migration.md) · [Next source section](notable-changes-in-python-3-7-2.md) · [Release/subject declaration](summary-release-highlights.md)
