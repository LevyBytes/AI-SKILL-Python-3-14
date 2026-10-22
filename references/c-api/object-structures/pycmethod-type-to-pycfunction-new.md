# object structures C API: `PyCMethod_Type`, `PyCMethod_Check()`, `PyCMethod_CheckExact()`, `PyCMethod_New()`, `function.__module__`, `PyCFunction_Type`, `PyCFunction_Check()`, `PyCFunction_CheckExact()`, `PyCFunction_NewEx()`, `PyCFunction_New()`

METH_O

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

When a method takes exactly one object argument, you can list it with the `METH_O` flag rather than calling [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) using an `"O"` argument. These are of type `PyCFunction`, carrying the *self* parameter plus a PyObject* parameter that stands for the single argument.

The following two constants don't mark the calling convention but rather the binding when paired with methods of classes. They can't be applied to functions declared for modules. No more than one of these flags is allowed on any single method.

 METH_CLASS

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Rather than an instance of the type, the method receives the type object as its first parameter. This serves to build *class methods*, much like what the [`classmethod()`](https://docs.python.org/3.14/library/functions.html#classmethod) built-in function produces.

 METH_STATIC

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Rather than an instance of the type, the method receives `NULL` as its first parameter. This serves to build *static methods*, much like what the [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod) built-in function produces.

There is a further constant that governs whether a method gets loaded over another definition sharing its method name.

 METH_COEXIST

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This method gets loaded over any existing definitions. With *METH_COEXIST* absent, the standard behavior is to pass over duplicate definitions. Because slot wrappers load ahead of the method table, the presence of a *sq_contains* slot, say, would yield a wrapped method called [`__contains__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__contains__) and block the loading of a matching PyCFunction of the same name. Once the flag is set, the PyCFunction loads over the wrapper object and lives alongside the slot. That comes in handy because PyCFunction calls get optimized to a greater degree than wrapper object calls.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyCMethod_Type

The type object that backs Python C method objects. In the Python layer this surfaces as [`types.BuiltinMethodType`](https://docs.python.org/3.14/library/types.html#types.BuiltinMethodType).

 int PyCMethod_Check(PyObject *op)

Yields true when *op* is an instance of the `PyCMethod_Type` type or one of its subtypes. The function never fails.

 int PyCMethod_CheckExact(PyObject *op)

Behaves like `PyCMethod_Check()`, except that it ignores subtypes.

 PyObject *PyCMethod_New(PyMethodDef *ml, PyObject *self, PyObject *module, [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) *cls)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.9.*

Convert *ml* into a Python [callable](https://docs.python.org/3.14/glossary.html#term-callable) object. It falls to the caller to keep *ml* alive longer than the callable. Usually you declare *ml* as a static variable.

When the C function in `ml->ml_meth` runs, the *self* parameter is handed to it as the *self* argument. *self* is allowed to be `NULL`.

You can set the [callable](https://docs.python.org/3.14/glossary.html#term-callable) object's `__module__` attribute from the *module* argument you provide. *module* ought to be a Python string, serving as the name of the module in which the function lives. When that's not available, set it to [`None`](https://docs.python.org/3.14/library/constants.html#None) or `NULL`.

See also

[`function.__module__`](https://docs.python.org/3.14/reference/datamodel.html#function.__module__)

The C function receives the *cls* parameter as its *defining_class* argument. You must supply it whenever `METH_METHOD` is set on `ml->ml_flags`.

Added in version 3.9.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyCFunction_Type

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

The type object that backs Python C function objects. In the Python layer this surfaces as [`types.BuiltinFunctionType`](https://docs.python.org/3.14/library/types.html#types.BuiltinFunctionType).

 int PyCFunction_Check(PyObject *op)

Yields true when *op* is an instance of the `PyCFunction_Type` type or one of its subtypes. The function never fails.

 int PyCFunction_CheckExact(PyObject *op)

Behaves like `PyCFunction_Check()`, except that it ignores subtypes.

 PyObject *PyCFunction_NewEx(PyMethodDef *ml, PyObject *self, PyObject *module)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Equivalent to `PyCMethod_New(ml, self, module, NULL)`.

 PyObject *PyCFunction_New(PyMethodDef *ml, PyObject *self)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.4.*

Equivalent to `PyCMethod_New(ml, self, NULL, NULL)`.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pycfunction.md) · [Owning structure and shared ABI conditions](pymethoddef-to-ml-doc.md) · [Following source contract](pycfunction-getflags-to-pycfunction-get-self.md)
