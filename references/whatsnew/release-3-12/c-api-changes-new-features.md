# Python 3.12 changes: Unstable API, opaque type layouts and vectorcall construction

### C API Changes

### New Features

- [**PEP 697**](https://peps.python.org/pep-0697/): Bring in the [Unstable C API tier](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api), aimed at low-level tooling like debuggers and JIT compilers. Each minor release of CPython may alter this API without issuing deprecation warnings. The names of its members carry the `PyUnstable_` prefix.

Code object constructors:

  - `PyUnstable_Code_New()` (renamed from `PyCode_New`)

  - `PyUnstable_Code_NewWithPosOnlyArgs()` (renamed from `PyCode_NewWithPosOnlyArgs`)

Extra storage for code objects ([**PEP 523**](https://peps.python.org/pep-0523/)):

  - `PyUnstable_Eval_RequestCodeExtraIndex()` (renamed from `_PyEval_RequestCodeExtraIndex`)

  - `PyUnstable_Code_GetExtra()` (renamed from `_PyCode_GetExtra`)

  - `PyUnstable_Code_SetExtra()` (renamed from `_PyCode_SetExtra`)

The earlier names stay reachable right up until each respective API changes.

(Contributed by Petr Viktorin in [gh-101101](https://github.com/python/cpython/issues/101101).)

- [**PEP 697**](https://peps.python.org/pep-0697/): Provide an API for extending types whose instance memory layout stays opaque:

  - [`PyType_Spec.basicsize`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Spec.basicsize) may be zero or negative, which signals inheriting or extending the size of the base class.

  - [`PyObject_GetTypeData()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetTypeData) plus [`PyType_GetTypeDataSize()`](https://docs.python.org/3.14/c-api/object.html#c.PyType_GetTypeDataSize) were added so that subclass-specific instance data can be reached.

  - [`Py_TPFLAGS_ITEMS_AT_END`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_ITEMS_AT_END) plus [`PyObject_GetItemData()`](https://docs.python.org/3.14/c-api/object.html#c.PyObject_GetItemData) were added to permit safely extending some variable-sized types, [`PyType_Type`](https://docs.python.org/3.14/c-api/type.html#c.PyType_Type) among them.

  - [`Py_RELATIVE_OFFSET`](https://docs.python.org/3.14/c-api/structures.html#c.Py_RELATIVE_OFFSET) was added so that [`members`](https://docs.python.org/3.14/c-api/structures.html#c.PyMemberDef) can be defined relative to a subclass-specific struct.

(Contributed by Petr Viktorin in [gh-103509](https://github.com/python/cpython/issues/103509).)

- Introduce the fresh [limited C API](https://docs.python.org/3.14/c-api/stable.html#limited-c-api) function [`PyType_FromMetaclass()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromMetaclass), a generalization of the current [`PyType_FromModuleAndSpec()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_FromModuleAndSpec) that takes an extra metaclass argument. (Contributed by Wenzel Jakob in [gh-93012](https://github.com/python/cpython/issues/93012).)

- An API for building objects callable through [the vectorcall protocol](https://docs.python.org/3.14/c-api/call.html#vectorcall) was contributed to the [Limited API](https://docs.python.org/3.14/c-api/stable.html#stable):

  - [`Py_TPFLAGS_HAVE_VECTORCALL`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_VECTORCALL)

  - [`PyVectorcall_NARGS()`](https://docs.python.org/3.14/c-api/call.html#c.PyVectorcall_NARGS)

  - [`PyVectorcall_Call()`](https://docs.python.org/3.14/c-api/call.html#c.PyVectorcall_Call)

  - [`vectorcallfunc`](https://docs.python.org/3.14/c-api/call.html#c.vectorcallfunc)

Whenever a class reassigns its [`__call__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__call__) method, the [`Py_TPFLAGS_HAVE_VECTORCALL`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_HAVE_VECTORCALL) flag is now stripped from that class. That keeps vectorcall safe alongside mutable types (that is, heap types lacking the immutable flag, [`Py_TPFLAGS_IMMUTABLETYPE`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_IMMUTABLETYPE)). Any mutable type that leaves [`tp_call`](https://docs.python.org/3.14/c-api/typeobj.html#c.PyTypeObject.tp_call) unoverridden now inherits the `Py_TPFLAGS_HAVE_VECTORCALL` flag. (Contributed by Petr Viktorin in [gh-93274](https://github.com/python/cpython/issues/93274).)



[Subject index](INDEX.md) · [Previous source section](build-changes.md) · [Next source section](managed-dictionary-and-weakref-flags.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](managed-dictionary-and-weakref-flags.md) · [Following release/subject continuation](opaque-reference-counting-calls.md)
