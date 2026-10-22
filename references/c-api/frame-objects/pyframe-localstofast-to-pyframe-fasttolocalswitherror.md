# Legacy local variable APIs

### Legacy local variable APIs

The APIs here are [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated). From Python 3.13 onward they accomplish nothing. Their only reason for existing is backward compatibility.

 void PyFrame_LocalsToFast(PyFrameObject *f, int clear)

Up until Python 3.13, this function copied the [`f_locals`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_locals) attribute of *f* over into the internal “fast” array of local variables, so that alterations made to frame objects became visible to the interpreter. Where *clear* held true, this function dealt with variables left unset in the locals dictionary.

[Soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) since version 3.13: This function now accomplishes nothing.

 void PyFrame_FastToLocals(PyFrameObject *f)

Up until Python 3.13, this function copied the internal “fast” array of local variables (the one the interpreter uses) over into the [`f_locals`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_locals) attribute of *f*, so that alterations made to local variables became visible to frame objects.

[Soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) since version 3.13: This function now accomplishes nothing.

 int PyFrame_FastToLocalsWithError(PyFrameObject *f)

Up until Python 3.13, this function resembled `PyFrame_FastToLocals()`, except it handed back `0` on success and `-1` with an exception set on failure.

[Soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated) since version 3.13: This function now accomplishes nothing.

See also

[**PEP 667**](https://peps.python.org/pep-0667/)

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyframeobject-to-pyframe-getgenerator.md) · [Previous source contract](pyframelocalsproxy-type-to-pyframelocalsproxy-check.md) · [Following source contract](internal-frames.md)
