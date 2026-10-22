# What's New In Python 3.4 / Porting to Python 3.4 / Changes in the C API

### Changes in the C API

- A debugging assertion has been added to [`PyEval_EvalFrameEx()`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyEval_EvalFrameEx), [`PyObject_Repr()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_Repr), and [`PyObject_Str()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_Str), as well as a handful of other internal C APIs, guarding against their use anywhere they might quietly throw away an exception that is currently live. When tossing the active exception is in fact intended and wanted — say it was already stashed away locally via [`PyErr_Fetch()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Fetch) or is on purpose being supplanted by another exception — you will have to call [`PyErr_Clear()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_Clear) explicitly so the assertion does not fire as you reach these operations, whether directly or indirectly, atop a build of Python compiled with assertions turned on.

- When its **msg** argument goes unset, [`PyErr_SetImportError()`](https://docs.python.org/3.14/c-api/exceptions.html#c.PyErr_SetImportError) now raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). Before this, it merely handed back `NULL` and left no exception in place.

- Whatever the [`PyOS_ReadlineFunctionPointer`](https://docs.python.org/3.14/c-api/veryhigh.html#c.PyOS_ReadlineFunctionPointer) callback yields is now required to be a string allocated through [`PyMem_RawMalloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_RawMalloc) or [`PyMem_RawRealloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_RawRealloc) — or `NULL` should something go wrong — rather than one allocated through [`PyMem_Malloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Malloc) or [`PyMem_Realloc()`](https://docs.python.org/3.14/c-api/memory.html#c.PyMem_Realloc) ([bpo-16742](https://bugs.python.org/issue?@action=redirect&bpo=16742))

- From now on [`PyThread_set_key_value()`](https://docs.python.org/3.14/c-api/tls.html#c.PyThread_set_key_value) sets the value in every case. Back in Python 3.3 the function stayed idle whenever the key was already present (that is, when the existing value was a non-`NULL` pointer).

- To put a bug right, the `f_tstate` (thread state) field on the [`PyFrameObject`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrameObject) structure has been dropped; the reasoning is laid out in [bpo-14432](https://bugs.python.org/issue?@action=redirect&bpo=14432).

[Subject index](INDEX.md) · [Previous source section](changes-in-the-python-api.md) · [Next source section](http-certificate-verification-defaults.md) · [Release/subject declaration](release-highlights.md) · [Release/subject declaration](porting-to-python-3-4.md)
