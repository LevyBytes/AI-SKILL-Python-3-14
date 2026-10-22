# Python 3.11 changes: Immutable heap types and vectorcall migration

Heap types bearing the [`Py_TPFLAGS_IMMUTABLETYPE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE) flag are now able to inherit the [**PEP 590**](https://peps.python.org/pep-0590/) vectorcall protocol. Up to now, only [static types](https://docs.python.org/3.14/c-api/typeobj.html#static-types) could do so. (Contributed by Erlend E. Aasland in [bpo-43908](https://bugs.python.org/issue?@action=redirect&bpo=43908))

- Given that [`Py_TYPE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_TYPE) has been converted into an inline static function, `Py_TYPE(obj) = new_type` has to be swapped for `Py_SET_TYPE(obj, new_type)`: refer to the [`Py_SET_TYPE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_SET_TYPE) function (offered since Python 3.9). To stay backward compatible, this macro is usable:

```python
#if PY_VERSION_HEX < 0x030900A4 && !defined(Py_SET_TYPE)
static inline void _Py_SET_TYPE(PyObject *ob, PyTypeObject *type)
{ ob->ob_type = type; }
#define Py_SET_TYPE(ob, type) _Py_SET_TYPE((PyObject*)(ob), type)
#endif

```

(Contributed by Victor Stinner in [bpo-39573](https://bugs.python.org/issue?@action=redirect&bpo=39573).)

- Given that [`Py_SIZE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_SIZE) has been converted into an inline static function, `Py_SIZE(obj) = new_size` has to be swapped for `Py_SET_SIZE(obj, new_size)`: refer to the [`Py_SET_SIZE()`](https://docs.python.org/3.14/c-api/structures.html#c.Py_SET_SIZE) function (offered since Python 3.9). To stay backward compatible, this macro is usable:

```python
#if PY_VERSION_HEX < 0x030900A4 && !defined(Py_SET_SIZE)
static inline void _Py_SET_SIZE(PyVarObject *ob, Py_ssize_t size)
{ ob->ob_size = size; }
#define Py_SET_SIZE(ob, size) _Py_SET_SIZE((PyVarObject*)(ob), size)
#endif

```

(Contributed by Victor Stinner in [bpo-39573](https://bugs.python.org/issue?@action=redirect&bpo=39573).)

-

[Subject index](INDEX.md) · [Previous source section](c-api-trashcan-lifecycle-migration.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](c-api-changes-new-features.md) · [Release/subject declaration](c-api-trashcan-lifecycle-migration.md) · [Following release/subject continuation](limited-api-header-dependencies.md)
