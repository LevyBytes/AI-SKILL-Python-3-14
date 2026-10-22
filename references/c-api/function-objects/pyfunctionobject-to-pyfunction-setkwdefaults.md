# function objects C API: Function creation, globals, defaults and vectorcall configuration

type PyFunctionObject

The C structure that backs functions.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyFunction_Type

An instance of [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject), this stands for the Python function type. To Python programmers it surfaces under the name `types.FunctionType`.

 int PyFunction_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Yields true when *o* is a function object — that is, it carries the type `PyFunction_Type`. The parameter is not permitted to be `NULL`. This call never fails.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFunction_New([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *code, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *globals)

*Return value: New reference.*

Hand back a fresh function object tied to the code object *code*. The *globals* argument has to be a dictionary holding the global variables the function can reach.

Both the function's docstring and its name come from the code object. The value of [`__module__`](https://docs.python.org/3.14/reference/datamodel.html#function.__module__) is drawn from *globals*. Argument defaults, annotations, and the closure all start out as `NULL`. As for [`__qualname__`](https://docs.python.org/3.14/reference/datamodel.html#function.__qualname__), it takes on whatever the code object's [`co_qualname`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_qualname) field holds.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFunction_NewWithQualName([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *code, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *globals, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *qualname)

*Return value: New reference.*

Behaves like `PyFunction_New()`, but on top of that lets you assign the function object's [`__qualname__`](https://docs.python.org/3.14/reference/datamodel.html#function.__qualname__) attribute. Pass *qualname* as either a unicode object or `NULL`; when it is `NULL`, the `__qualname__` attribute ends up matching the code object's [`co_qualname`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_qualname) field.

Added in version 3.3.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFunction_GetCode([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

*Return value: Borrowed reference.*

Give back the code object that the function object *op* is bound to.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFunction_GetGlobals([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

*Return value: Borrowed reference.*

Give back the globals dictionary tied to the function object *op*.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFunction_GetModule([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

*Return value: Borrowed reference.*

Hand back a [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) pointing at the [`__module__`](https://docs.python.org/3.14/reference/datamodel.html#function.__module__) attribute of the [function object](https://docs.python.org/3.14/reference/datamodel.html#user-defined-funcs) *op*. A value of *NULL* is possible here.

Typically this holds a [`string`](https://docs.python.org/3.14/library/stdtypes.html#str) with the module name, although Python code is free to assign some other object to it.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFunction_GetDefaults([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

*Return value: Borrowed reference.*

Give back the argument default values held by the function object *op*. What comes back is either a tuple of arguments or `NULL`.

 int PyFunction_SetDefaults([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *defaults)

Assign the argument default values on the function object *op*. The *defaults* argument has to be `Py_None` or a tuple.

Should it fail, it throws [`SystemError`](https://docs.python.org/3.14/library/exceptions.html#SystemError) and gives back `-1`.

 void PyFunction_SetVectorcall(PyFunctionObject *func, [vectorcallfunc](https://docs.python.org/3.14/c-api/call.html#c.vectorcallfunc) vectorcall)

Assign the vectorcall field on the supplied function object *func*.

Warning: any extension that leans on this API is obliged to keep the conduct of the untouched (default) vectorcall function intact!

Added in version 3.12.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyFunction_GetKwDefaults([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op)

*Return value: Borrowed reference.*

Give back the keyword-only argument default values carried by the function object *op*. This turns out to be either a dictionary of arguments or `NULL`.

 int PyFunction_SetKwDefaults([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *op, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *defaults)

Assign the keyword-only argument default values on the function object *op*. Here *defaults* has to be either a dictionary of keyword-only arguments or `Py_None`.

On success this call yields `0`, and on failure it yields `-1` with an exception set.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](function-objects.md) · [Following source contract](pyfunction-getclosure-to-pyfunction-clearwatcher.md)
