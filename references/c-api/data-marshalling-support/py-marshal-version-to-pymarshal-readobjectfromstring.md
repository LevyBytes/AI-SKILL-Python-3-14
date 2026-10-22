# Data marshalling support

## Data marshalling support

### Data marshalling support

From C code, these functions let you handle serialized objects in the very format produced by the [`marshal`](https://docs.python.org/3.14/library/marshal.html#module-marshal) module. Some of them emit data in that serialization layout, while others recover the data afterward. Whenever marshalled content is kept in a file, that file has to be opened in binary mode.

Numbers get written out least-significant-byte-first.

More than one version of the data format is recognized by the module; the [`Python module documentation`](https://docs.python.org/3.14/library/marshal.html#module-marshal) spells out the specifics.

 Py_MARSHAL_VERSION

Holds the format version in use right now. Refer to [`marshal.version`](https://docs.python.org/3.14/library/marshal.html#marshal.version).

 void PyMarshal_WriteLongToFile(long value, FILE *file, int version)

Writes the long integer *value* out to *file* in marshalled form. No matter how wide the platform's native long happens to be, only the bottom 32 bits of *value* are recorded. The chosen file format is given by *version*.

Failure is possible here; when it happens the error indicator gets set, and you can detect it by calling [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred).

 void PyMarshal_WriteObjectToFile([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *value, FILE *file, int version)

Serializes the Python object *value* into *file*. The format of that file is selected by *version*.

This call may not succeed; on a failure it raises the error indicator, which a follow-up [`PyErr_Occurred()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Occurred) will reveal.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyMarshal_WriteObjectToString([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *value, int version)

*Return value: New reference.*

Produces a bytes object that holds the marshalled form of *value*. The format is dictated by *version*.

Reading previously marshalled values back is the job of the functions listed below.

 long PyMarshal_ReadLongFromFile(FILE *file)

Pulls a C long out of the data stream sitting in a FILE* that was opened for reading. Whatever the platform's native long width is, this routine only ever reads a 32-bit quantity.

If an error occurs, it raises the right exception ([`EOFError`](https://docs.python.org/3.14/library/exceptions.html#EOFError)) and gives back `-1`.

 int PyMarshal_ReadShortFromFile(FILE *file)

Reads a C short from the data stream held in a FILE* opened for reading. No matter the native size of short on the host, only a 16-bit value is taken.

Encountering an error makes it set the proper exception ([`EOFError`](https://docs.python.org/3.14/library/exceptions.html#EOFError)) and hand back `-1`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyMarshal_ReadObjectFromFile(FILE *file)

*Return value: New reference.*

Recovers a Python object from the data stream within a FILE* opened for reading.

When something goes wrong, the matching exception ([`EOFError`](https://docs.python.org/3.14/library/exceptions.html#EOFError), [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) or [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError)) is raised and `NULL` comes back.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyMarshal_ReadLastObjectFromFile(FILE *file)

*Return value: New reference.*

Recovers a Python object from the data stream within a FILE* opened for reading. In contrast to `PyMarshal_ReadObjectFromFile()`, it presumes nothing more will be read from that file, so it can eagerly pull the file's bytes into memory and then de-serialize entirely from there instead of fetching one byte at a time off disk. Reach for this variant only when you are sure the file holds nothing else you intend to read.

When something goes wrong, the matching exception ([`EOFError`](https://docs.python.org/3.14/library/exceptions.html#EOFError), [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) or [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError)) is raised and `NULL` is returned.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyMarshal_ReadObjectFromString(const char *data, [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) len)

*Return value: New reference.*

Builds a Python object out of the data stream found in a byte buffer of *len* bytes that *data* points at.

Upon an error it sets the fitting exception ([`EOFError`](https://docs.python.org/3.14/library/exceptions.html#EOFError), [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) or [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError)) and returns `NULL`.

[Subject index](INDEX.md) · [Previous source contract](../mapping-protocol/pymapping-haskey-to-pymapping-items.md)
