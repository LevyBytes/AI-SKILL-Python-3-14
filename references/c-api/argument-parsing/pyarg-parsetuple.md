# int PyArg_ParseTuple(PyObject *args, const char *format, ...)

### API Functions

 int PyArg_ParseTuple([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *args, const char *format, ...)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*
Reads the arguments of a function that accepts positional parameters alone, depositing them into local variables. A success yields true; a failure instead yields false and raises whatever exception fits.

[Subject index](INDEX.md) · [Previous source contract](other-objects.md) · [Previous source contract](pyarg-vaparse.md)
