# system interface C API: `Py_fclose()`

FILE *Py_fopen([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *path, const char *mode)

Comparable to `fopen()`, except that *path* is a Python object and an exception gets set when something goes wrong.

*path* has to be a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object, a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) object, or a [path-like object](https://docs.python.org/3.14/glossary.html#term-path-like-object).

When it succeeds, the new file pointer comes back. When it fails, an exception is set and `NULL` comes back.

Closing the file has to be done with `Py_fclose()` instead of calling `fclose()` directly.

The file descriptor is created non-inheritable ([**PEP 446**](https://peps.python.org/pep-0446/)).

The caller must have an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

Added in version 3.14.

 int Py_fclose(FILE *file)

Close a file that `Py_fopen()` previously opened.

When it succeeds, `0` comes back. When it fails, `EOF` comes back and `errno` is set to signal the error. Either way, any later use (counting a second call to `Py_fclose()`) of the stream produces undefined behavior.

Added in version 3.14.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyos-fspath-to-pyos-getsig.md) · [Previous source contract](pyos-setsig-to-py-encodelocale.md) · [Following source contract](pysys-getobject-to-pysys-getxoptions.md)
