# calling objects C API: Object method calls and vectorcall entrypoints

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_CallMethod([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, const char *name, const char *format, ...)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Invoke the method called *name* on object *obj*, passing a varying count of C arguments. Those C arguments get spelled out by a [`Py_BuildValue()`](https://docs.python.org/3.14/c-api/arg.html#c.Py_BuildValue) format string whose output should be a tuple.

A *NULL* format signals that no arguments are being passed.

On success the call's result comes back; should it fail, an exception is raised and *NULL* is returned.

This is the equivalent of the Python expression: `obj.name(arg1, arg2, ...)`.

Bear in mind that when your arguments are solely [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)* values, `PyObject_CallMethodObjArgs()` runs faster.

Changed in version 3.4: Previously `char *`, the types covering *name* together with *format* were updated.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_CallFunctionObjArgs([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *callable, ...)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Invoke the callable Python object *callable* with a varying count of [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)* arguments. You hand these over as a series of parameters whose end is marked by *NULL*.

On success the call's result comes back; should it fail, an exception is raised and *NULL* is returned.

This is the equivalent of the Python expression: `callable(arg1, arg2, ...)`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_CallMethodObjArgs([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *name, ...)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Invoke a method on the Python object *obj*, with the method's name supplied as a Python string object via *name*. The invocation carries a varying count of [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject)* arguments, handed over as a series of parameters terminated by *NULL*.

On success the call's result comes back; should it fail, an exception is raised and *NULL* is returned.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_CallMethodNoArgs([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *name)

Invoke a method on the Python object *obj* passing nothing, with the method's name handed over as a Python string object in *name*.

On success the call's result comes back; should it fail, an exception is raised and *NULL* is returned.

Added in version 3.9.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_CallMethodOneArg([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *arg)

Invoke a method on the Python object *obj* handing it one positional argument *arg*, with the method's name handed over as a Python string object in *name*.

On success the call's result comes back; should it fail, an exception is raised and *NULL* is returned.

Added in version 3.9.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_Vectorcall([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *callable, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *const *args, size_t nargsf, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *kwnames)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.12.*

Invoke the callable Python object *callable*. Its arguments mirror those of `vectorcallfunc`. Provided *callable* offers vectorcall, this goes straight to the vectorcall function held in *callable*.

On success the call's result comes back; should it fail, an exception is raised and *NULL* is returned.

Added in version 3.8: as `_PyObject_Vectorcall`

Changed in version 3.9: Given its present name, with the leading underscore dropped. That earlier provisional name is now [soft deprecated](https://docs.python.org/3.14/glossary.html#term-soft-deprecated).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_VectorcallDict([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *callable, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *const *args, size_t nargsf, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *kwdict)

Invoke *callable* with its positional arguments delivered just as the vectorcall protocol prescribes, yet with keyword arguments delivered through a dictionary *kwdict*. Only the positional arguments sit inside the *args* array.

No matter which protocol runs underneath, the arguments still have to be converted. Hence you should turn to this function purely when the caller has on hand a dictionary for the keyword arguments but lacks a tuple for the positional ones.

Added in version 3.9.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyObject_VectorcallMethod([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *name, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *const *args, size_t nargsf, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *kwnames)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.12.*

Invoke a method through the vectorcall calling convention. You supply the method's name as a Python string *name*. The object on which the method runs is *args[0]*, while the portion of the *args* array beginning at *args[1]* holds the call's arguments. No fewer than one positional argument is required. *nargsf* tallies the positional arguments counting *args[0]*, with `PY_VECTORCALL_ARGUMENTS_OFFSET` added in when `args[0]` might be altered for a moment. You may supply keyword arguments exactly as you do in `PyObject_Vectorcall()`.

When the object carries the [`Py_TPFLAGS_METHOD_DESCRIPTOR`](https://docs.python.org/3.14/c-api/typeobj.html#c.Py_TPFLAGS_METHOD_DESCRIPTOR) trait, this invokes the unbound method object using the entire *args* vector as its arguments.

On success the call's result comes back; should it fail, an exception is raised and *NULL* is returned.

Added in version 3.9.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyobject-call-to-pyobject-callfunction.md) · [Following source contract](pycallable-check.md)
