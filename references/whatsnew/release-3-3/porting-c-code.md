# What's New In Python 3.3 / Porting C code

### Porting C code

- As part of revisions to the buffer API, the undocumented `smalltable` member of the [`Py_buffer`](https://docs.python.org/3.14/c-api/buffer.html#c.Py_buffer) structure was dropped, and the `PyMemoryViewObject` layout was altered.

Every extension that depends on the affected portions of `memoryobject.h` or `object.h` needs to be rebuilt.

- On account of PEP 393, the [`Py_UNICODE`](https://docs.python.org/3.14/c-api/unicode.html#c.Py_UNICODE) type, together with every function that uses it, is deprecated — though it will remain available for no fewer than five years. Anyone who relied on low-level Unicode APIs to build and read unicode objects and wants the smaller memory footprint that [**PEP 393**](https://peps.python.org/pep-0393/) brings must port their code over to the new [Unicode API](https://docs.python.org/3.14/c-api/unicode.html).

That said, if all you ever called were high-level functions like [`PyUnicode_Concat()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_Concat), [`PyUnicode_Join()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_Join) or [`PyUnicode_FromFormat()`](https://docs.python.org/3.14/c-api/unicode.html#c.PyUnicode_FromFormat), your code picks up the new unicode representations on its own.

- On failure, [`PyImport_GetMagicNumber()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_GetMagicNumber) now returns `-1`.

- Now that a negative *level* argument is invalid for [`__import__()`](https://docs.python.org/3.14/library/functions.html#import__), the same restriction extends to [`PyImport_ImportModuleLevel()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModuleLevel). One consequence is that the *level* value [`PyImport_ImportModuleEx()`](https://docs.python.org/3.14/c-api/import.html#c.PyImport_ImportModuleEx) applies is now `0` rather than `-1`.

[Subject index](INDEX.md) · [Previous source section](porting-python-code.md) · [Next source section](building-c-extensions.md) · [Release/subject declaration](summary-release-highlights.md)
