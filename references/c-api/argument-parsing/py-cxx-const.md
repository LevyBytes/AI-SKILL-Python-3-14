# PY_CXX_CONST

PY_CXX_CONST

Whatever value, if any, gets placed ahead of char *const* within the *keywords* parameter declaration belonging to `PyArg_ParseTupleAndKeywords()` and `PyArg_VaParseTupleAndKeywords()`. It defaults to empty under C and to `const` under C++ (const char *const*). To change it, give it your chosen value before you include `Python.h`.

Added in version 3.13.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyarg-parsetuple.md) · [Previous source contract](pyarg-parsetupleandkeywords-to-pyarg-unpacktuple.md) · [Following source contract](py-buildvalue.md)
