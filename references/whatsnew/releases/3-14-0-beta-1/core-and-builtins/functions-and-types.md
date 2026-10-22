# Python 3.14.0 beta 1 / core and builtins / functions and types

[gh-131798](https://github.com/python/cpython/issues/131798): The return type of `_BINARY_OP_SUBSCR_TUPLE_INT` is now propagated in the JIT. Tomas Roun wrote this patch.

[gh-131798](https://github.com/python/cpython/issues/131798): By setting the return type to int, the JIT can now drop int guards following `_CALL_LEN`. Diego Russo wrote this patch

[gh-132284](https://github.com/python/cpython/issues/132284): When a base `PyCFunction` slot is not overridden, it is no longer wrapped during class creation.

[gh-132286](https://github.com/python/cpython/issues/132286): A bug is fixed where [`type.__annotate__`](https://docs.python.org/3.14/reference/datamodel.html#type.__annotate__) was left undeleted after [`type.__annotations__`](https://docs.python.org/3.14/reference/datamodel.html#type.__annotations__) had been deleted.

[gh-131798](https://github.com/python/cpython/issues/131798): By setting the return type to bool, the JIT can drop an extra `_TO_BOOL_BOOL` instruction that follows `_CONTAINS_OP_DICT`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
