# Numbers

### Numbers

With these formats you can express Python numbers or single characters as C numbers. Formats expecting [`int`](https://docs.python.org/3.14/library/functions.html#int), [`float`](https://docs.python.org/3.14/library/functions.html#float) or [`complex`](https://docs.python.org/3.14/library/functions.html#complex) are also able to invoke the matching special methods [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__), [`__float__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__float__) or [`__complex__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__complex__) to coerce the Python object into the type required.

With signed integer formats, an [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) is raised whenever the value falls outside the C type’s range. With unsigned integer formats, no range checking happens — should the receiving field be too small to hold the value, the most significant bits are quietly dropped.

`b` ([`int`](https://docs.python.org/3.14/library/functions.html#int)) [unsigned char]

Turn a nonnegative Python integer into an unsigned tiny integer, kept in a C unsigned char.

`B` ([`int`](https://docs.python.org/3.14/library/functions.html#int)) [unsigned char]

Turn a Python integer into a tiny integer with no overflow checking, kept in a C unsigned char.

`h` ([`int`](https://docs.python.org/3.14/library/functions.html#int)) [short int]

Turn a Python integer into a C short int.

`H` ([`int`](https://docs.python.org/3.14/library/functions.html#int)) [unsigned short int]

Turn a Python integer into a C unsigned short int, with no overflow checking.

`i` ([`int`](https://docs.python.org/3.14/library/functions.html#int)) [int]

Turn a Python integer into a plain C int.

`I` ([`int`](https://docs.python.org/3.14/library/functions.html#int)) [unsigned int]

Turn a Python integer into a C unsigned int, with no overflow checking.

`l` ([`int`](https://docs.python.org/3.14/library/functions.html#int)) [long int]

Turn a Python integer into a C long int.

`k` ([`int`](https://docs.python.org/3.14/library/functions.html#int)) [unsigned long]

Turn a Python integer into a C unsigned long with no overflow checking.

Changed in version 3.14: Use [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) if available.

`L` ([`int`](https://docs.python.org/3.14/library/functions.html#int)) [long long]

Turn a Python integer into a C long long.

`K` ([`int`](https://docs.python.org/3.14/library/functions.html#int)) [unsigned long long]

Turn a Python integer into a C unsigned long long with no overflow checking.

Changed in version 3.14: Use [`__index__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__index__) if available.

`n` ([`int`](https://docs.python.org/3.14/library/functions.html#int)) [[`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t)]

Turn a Python integer into a C [`Py_ssize_t`](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t).

`c` ([`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) of length 1) [char]

Turn a Python byte — given as a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) or [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) object of length 1 — into a C char.

Changed in version 3.3: Allow [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) objects.

`C` ([`str`](https://docs.python.org/3.14/library/stdtypes.html#str) of length 1) [int]

Turn a Python character — given as a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) object of length 1 — into a C int.

`f` ([`float`](https://docs.python.org/3.14/library/functions.html#float)) [float]

Turn a Python floating-point number into a C float.

`d` ([`float`](https://docs.python.org/3.14/library/functions.html#float)) [double]

Turn a Python floating-point number into a C double.

`D` ([`complex`](https://docs.python.org/3.14/library/functions.html#complex)) [Py_complex]

Turn a Python complex number into a C [`Py_complex`](https://docs.python.org/3.14/c-api/complex.html#c.Py_complex) structure.

[Subject index](INDEX.md) · [Previous source contract](strings-and-buffers-w-read-write-bytes-like-object-py-buffer.md) · [Following source contract](other-objects.md)
