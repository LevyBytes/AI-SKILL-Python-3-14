# Objects for Type Hinting

# Typehints

### Objects for Type Hinting

A number of built-in types exist to support type hinting. At present the lineup comprises just two — [GenericAlias](https://docs.python.org/3.14/library/stdtypes.html#types-genericalias) together with [Union](https://docs.python.org/3.14/library/stdtypes.html#types-union). Of these, the C layer surfaces only `GenericAlias`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *Py_GenericAlias([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *origin, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *args)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.9.*

Build a [GenericAlias](https://docs.python.org/3.14/library/stdtypes.html#types-genericalias) object — the C counterpart of invoking the Python class [`types.GenericAlias`](https://docs.python.org/3.14/library/types.html#types.GenericAlias). Here the *origin* and *args* parameters populate, in order, the `GenericAlias`‘s `__origin__` and `__args__` attributes. Pass a [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject)* for *origin*, while *args* accepts either a [PyTupleObject](https://docs.python.org/3.14/c-api/tuple.html#c.PyTupleObject)* or any `PyObject*`. Whenever the supplied *args* is not a tuple, the call wraps it into a 1-tuple on your behalf and assigns `__args__` the value `(args,)`. Argument validation here is sparse, which means the routine still completes even should *origin* fail to be a type. Note that the `GenericAlias`‘s `__parameters__` attribute is filled in lazily out of `__args__`. Should something go wrong, an exception gets set and the result is `NULL`.

The snippet below illustrates one way to render an extension type generic:

```c
...
static PyMethodDef my_obj_methods[] = {
    // Other methods.
    ...
    {"__class_getitem__", Py_GenericAlias, METH_O|METH_CLASS, "my_obj is generic over its contained type"}
    ...
}

```

See also

The data model method [`__class_getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__class_getitem__).

Added in version 3.9.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) Py_GenericAliasType

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.9.*

This is the C type carried by whatever `Py_GenericAlias()` hands back — the analog, on the Python side, of [`types.GenericAlias`](https://docs.python.org/3.14/library/types.html#types.GenericAlias).

Added in version 3.9.

[Subject index](INDEX.md)
