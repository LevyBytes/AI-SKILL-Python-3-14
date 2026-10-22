# Soft-deprecated API

### Soft-deprecated API

[Soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) since version 3.15.

These APIs found their way into Python's C API in error. They appear here purely for the sake of completeness; lean on the other `PyFile*` APIs in their stead.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFile_NewStdPrinter(int fd)

Use `PyFile_FromFd()` with defaults (`fd, NULL, "w", -1, NULL, NULL, NULL, 0`) instead.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyStdPrinter_Type

The type of the file-like objects the interpreter relies on internally during Python startup, before [`io`](https://docs.python.org/3.14/library/io.html#module-io) has become available. To make file objects, turn instead to Python's [`open()`](https://docs.python.org/3.14/library/functions.html#open) or to `PyFile_FromFd()`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyfile-fromfd-to-pyfile-writestring.md)
