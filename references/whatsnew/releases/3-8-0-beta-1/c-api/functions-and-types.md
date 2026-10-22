# Python 3.8.0 beta 1 / c api / functions and types

[bpo-36379](https://bugs.python.org/issue?@action=redirect&bpo=36379): Resolves crashes that arose when trying to use the *modulo* parameter while `__ipow__` is realized in C.

[bpo-36922](https://bugs.python.org/issue?@action=redirect&bpo=36922): Introduces a new type flag `Py_TPFLAGS_METHOD_DESCRIPTOR` for objects that act like unbound methods. Such objects back the optimization delivered by the `LOAD_METHOD`/`CALL_METHOD` opcodes. Refer to PEP 590.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
