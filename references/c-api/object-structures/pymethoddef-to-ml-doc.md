# object structures C API: `PyMethodDef`

type PyMethodDef

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) (including all members).*

A structure for describing a method belonging to an extension type. Four fields make up this structure:

 const char *ml_name

Name of the method.

 PyCFunction ml_meth

Pointer to the C implementation.

 int ml_flags

Flags bits indicating how the call should be constructed.

 const char *ml_doc

Points to the contents of the docstring.

The `ml_meth` holds a C function pointer. Although these functions can vary in type, every one of them returns PyObject*. When a function isn't a `PyCFunction`, the compiler insists on a cast inside the method table. And while `PyCFunction` lists its first parameter as PyObject*, method implementations frequently work with the concrete C type of the *self* object.

The `ml_flags` field is a bitfield that may carry the flags below. Each individual flag names either a calling convention or a binding convention.

The available calling conventions are:

 METH_VARARGS

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

This is the everyday calling convention, in which the methods are of type `PyCFunction`. The function looks for two PyObject* values. The first is the *self* object for methods, or the module object when it comes to module functions. The second one (frequently named *args*) is a tuple object that bundles every argument. You normally handle this parameter with [`PyArg_ParseTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTuple) or [`PyArg_UnpackTuple()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_UnpackTuple).

 METH_KEYWORDS

Permitted only in particular combinations alongside other flags: METH_VARARGS | METH_KEYWORDS, METH_FASTCALL | METH_KEYWORDS and METH_METHOD | METH_FASTCALL | METH_KEYWORDS.

METH_VARARGS | METH_KEYWORDS

Methods carrying these flags have to be of type `PyCFunctionWithKeywords`. The function looks for three parameters: *self*, *args*, *kwargs*, where *kwargs* is a dictionary holding all the keyword arguments, or possibly `NULL` when none were supplied. You normally handle these parameters with [`PyArg_ParseTupleAndKeywords()`](https://docs.python.org/3.14/c-api/arg.html#c.PyArg_ParseTupleAndKeywords).

 METH_FASTCALL

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

A fast calling convention that handles positional arguments only. The methods are of type `PyCFunctionFast`. Its first parameter is *self*, the second is a C array of PyObject* values that carries the arguments, and the third is the argument count (how long that array is).

Added in version 3.7.

Changed in version 3.10: `METH_FASTCALL` is now part of the [stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable-abi).

METH_FASTCALL | METH_KEYWORDS

An extension to `METH_FASTCALL` that additionally handles keyword arguments, using methods of type `PyCFunctionFastWithKeywords`. The keyword arguments arrive exactly as they do under the [vectorcall protocol](https://docs.python.org/3.14/c-api/call.html#vectorcall): a further fourth PyObject* parameter shows up, a tuple naming the keyword arguments (always guaranteed to be strings), or possibly `NULL` when there are no keywords. The keyword argument values land in the *args* array, following the positional arguments.

Added in version 3.7.

 METH_METHOD

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.7.*

Permitted only in this combination with other flags: METH_METHOD | METH_FASTCALL | METH_KEYWORDS.

METH_METHOD | METH_FASTCALL | METH_KEYWORDS

An extension to METH_FASTCALL | METH_KEYWORDS that adds the *defining class*, meaning the class where the method in question lives. That defining class may well be a superclass of `Py_TYPE(self)`.

The method has to be of type `PyCMethod`, identical to `METH_FASTCALL | METH_KEYWORDS` except that a `defining_class` argument follows `self`.

Added in version 3.9.

 METH_NOARGS

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

When methods take no parameters, listing them with the `METH_NOARGS` flag spares them from verifying whether arguments were supplied. Such methods must be of type `PyCFunction`. Their first parameter usually goes by *self* and carries a reference to the module or object instance. The second parameter is `NULL` in every situation.

There must be 2 parameters on the function. Because the second parameter goes unused, you can apply [`Py_UNUSED`](https://docs.python.org/3.14/c-api/intro.html#c.Py_UNUSED) to head off a compiler warning.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pycfunction.md) · [Previous source contract](pycmethod.md) · [Following source contract](pycmethod-type-to-pycfunction-new.md)
