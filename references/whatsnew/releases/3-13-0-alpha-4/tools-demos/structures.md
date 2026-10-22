# Python 3.13.0 alpha 4 / tools demos / structures

[gh-115015](https://github.com/python/cpython/issues/115015): Repair a bug in Argument Clinic that emitted wrong code for parameterless methods using the [METH_METHOD | METH_FASTCALL | METH_KEYWORDS](https://docs.python.org/3.14/c-api/structures.html#meth-method-meth-fastcall-meth-keywords) calling convention. Only the count of positional parameters was verified; any keyword argument supplied would be quietly accepted.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
