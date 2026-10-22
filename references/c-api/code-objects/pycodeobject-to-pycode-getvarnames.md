# code objects C API: Code object construction, bytecode and source locations

type PyCodeObject

The C structure backing the objects that describe code objects. You should expect this type's fields to change at any moment.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyCode_Type

An instance of [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) that stands for the Python [code object](https://docs.python.org/3.14/reference/datamodel.html#code-objects).

 int PyCode_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *co)

Yield true when *co* is a [code object](https://docs.python.org/3.14/reference/datamodel.html#code-objects). The function never fails.

 [Py_ssize_t](https://docs.python.org/3.14/c-api/intro.html#c.Py_ssize_t) PyCode_GetNumFree(PyCodeObject *co)

Give back how many [free (closure) variables](https://docs.python.org/3.14/glossary.html#term-closure-variable) a code object holds.

 int PyUnstable_Code_GetFirstFree(PyCodeObject *co)

 *Part of the [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api); minor releases may alter it with no warning.*

Give back the index of the earliest [free (closure) variable](https://docs.python.org/3.14/glossary.html#term-closure-variable) within a code object.

Changed in version 3.13: Renamed away from `PyCode_GetFirstFree` under the [Unstable C API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api). Although the former name is deprecated, it sticks around until the signature next changes.

 PyCodeObject *PyUnstable_Code_New(int argcount, int kwonlyargcount, int nlocals, int stacksize, int flags, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *code, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *consts, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *names, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *varnames, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *freevars, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *cellvars, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *filename, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *qualname, int firstlineno, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *linetable, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exceptiontable)

 *Belongs to the [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api); a minor release may change it without notice.*

Give back a new code object. Should you merely want a placeholder code object for building a frame, turn to `PyCode_NewEmpty()` instead.

Because the bytecode's definition shifts so frequently, a direct call to `PyUnstable_Code_New()` can tie you to one specific Python version.

This function's numerous arguments depend on one another in intricate ways, so that even slight tweaks to the values can readily produce wrong execution or VM crashes. Wield it only with the utmost caution.

Changed in version 3.11: Added `qualname` and `exceptiontable` parameters.

Changed in version 3.12: Renamed away from `PyCode_New` under the [Unstable C API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api). Although the former name is deprecated, it sticks around until the signature next changes.

 PyCodeObject *PyUnstable_Code_NewWithPosOnlyArgs(int argcount, int posonlyargcount, int kwonlyargcount, int nlocals, int stacksize, int flags, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *code, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *consts, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *names, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *varnames, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *freevars, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *cellvars, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *filename, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *qualname, int firstlineno, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *linetable, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *exceptiontable)

 *Counted among the [Unstable API](https://docs.python.org/3.14/c-api/stable.html#unstable-c-api); it can shift without notice across minor releases.*

Comparable to `PyUnstable_Code_New()`, except it takes one more “posonlyargcount” covering positional-only arguments. Whatever cautions surround `PyUnstable_Code_New` hold for this function just the same.

Added in version 3.8: as `PyCode_NewWithPosOnlyArgs`

Changed in version 3.11: Added `qualname` and `exceptiontable` parameters.

Changed in version 3.12: Renamed to `PyUnstable_Code_NewWithPosOnlyArgs`. The earlier name, now deprecated, stays usable up until the signature next changes.

 PyCodeObject *PyCode_NewEmpty(const char *filename, const char *funcname, int firstlineno)

*Return value: New reference.*

Give back a fresh empty code object carrying the filename, function name, and first line number you supply. Run it and the code object that results raises an `Exception`.

 int PyCode_Addr2Line(PyCodeObject *co, int byte_offset)

Give back the line number for the instruction that falls at or before `byte_offset` and finishes past it. When the line number of a frame is all you are after, reach for [`PyFrame_GetLineNumber()`](https://docs.python.org/3.14/c-api/frame.html#c.PyFrame_GetLineNumber) instead.

To step efficiently through a code object's line numbers, lean on [**the API described in PEP 626**](https://peps.python.org/pep-0626/#out-of-process-debuggers-and-profilers).

 int PyCode_Addr2Location([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *co, int byte_offset, int *start_line, int *start_column, int *end_line, int *end_column)

Fills the `int` pointers handed in with the source line and column numbers of the instruction at `byte_offset`. Where no information exists for a given element, it writes `0` into the value.

Hands back `1` when the function succeeds and 0 if it does not.

Added in version 3.11.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCode_GetCode(PyCodeObject *co)

The counterpart of the Python expression `getattr(co, 'co_code')`. It hands back a strong reference to a [`PyBytesObject`](https://docs.python.org/3.14/c-api/bytes.html#c.PyBytesObject) that captures a code object's bytecode. Where something goes wrong, `NULL` comes back and an exception is set.

The interpreter might build this `PyBytesObject` only when asked, and it need not mirror the bytecode CPython genuinely runs. Debuggers and profilers are what this function chiefly serves.

Added in version 3.11.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyCode_GetVarnames(PyCodeObject *co)

The counterpart of the Python expression `getattr(co, 'co_varnames')`. It hands back a new reference to a [`PyTupleObject`](https://docs.python.org/3.14/c-api/tuple.html#c.PyTupleObject) that holds the names of the local variables. Where something goes wrong, `NULL` comes back and an exception is set.

Added in version 3.11.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](code-objects.md) · [Following source contract](pycode-getcellvars-to-pycode-clearwatcher.md)
