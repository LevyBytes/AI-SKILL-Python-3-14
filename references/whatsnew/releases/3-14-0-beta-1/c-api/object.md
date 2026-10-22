# Python 3.14.0 beta 1 / c api / object

[gh-133164](https://github.com/python/cpython/issues/133164): The [`PyUnstable_Object_IsUniqueReferencedTemporary()`](https://docs.python.org/3.14/c-api/object.html#c.PyUnstable_Object_IsUniqueReferencedTemporary) function is added to test whether an object lives as a unique temporary variable on the interpreter's stack. It replaces certain situations where verifying that [`Py_REFCNT()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_REFCNT) equals one no longer suffices to confirm that a Python object can be modified in-place without any visible side effects.

[gh-133140](https://github.com/python/cpython/issues/133140): A new [`PyUnstable_Object_IsUniquelyReferenced()`](https://docs.python.org/3.14/c-api/object.html#c.PyUnstable_Object_IsUniquelyReferenced) helper is introduced to stand in for `Py_REFNCT(op) == 1` when running on [free threaded](https://docs.python.org/3.14/glossary.html#term-free-threading) Python builds.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
