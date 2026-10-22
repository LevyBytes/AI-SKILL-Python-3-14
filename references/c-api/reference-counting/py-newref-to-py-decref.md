# reference counting C API: `Py_NewRef()`, `Py_XNewRef()`, `Py_DECREF()`, `Py_XDECREF()`, `Py_CLEAR()`, `Py_IncRef()`, `Py_DecRef()`

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *Py_NewRef([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Mint a fresh [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to an object: invoke `Py_INCREF()` against *o* and hand the object *o* back.

Once the [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) is no longer wanted, you should invoke `Py_DECREF()` on it to give up the reference.

The object *o* cannot be `NULL`; turn to `Py_XNewRef()` whenever *o* might be `NULL`.

For example:

```c
Py_INCREF(obj);
self->attr = obj;

```

can be written as:

```c
self->attr = Py_NewRef(obj);

```

See also `Py_INCREF()`.

Added in version 3.10.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *Py_XNewRef([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Comparable to `Py_NewRef()`, except that here the object *o* is permitted to be NULL.

Should the object *o* be `NULL`, the function simply hands back `NULL`.

Added in version 3.10.

 void Py_DECREF([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Give up a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to object *o*, signalling that the reference is finished with.

The function leaves [immortal](https://docs.python.org/3.14/glossary.html#term-immortal) objects untouched.

As soon as the final [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) goes away (that is, the object's reference count drops to 0), the deallocation function of the object's type is called (and that function cannot be `NULL`).

You generally apply this routine to drop a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) just before leaving its scope.

The object cannot be `NULL`; when you are uncertain whether it is `NULL`, fall back on `Py_XDECREF()`.

Do not count on this function to alter *o* in any fashion. For at least [**some objects**](https://peps.python.org/pep-0683/), it does nothing at all.

Warning

That deallocation function may end up running arbitrary Python code (for instance, when a class instance carrying a [`__del__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__del__) method is freed). Although exceptions raised in such code do not propagate, the code that runs has unrestricted access to every Python global variable. The implication is that any object reachable through a global variable ought to sit in a consistent state ahead of any `Py_DECREF()` call. As an example, code that removes an object from a list should stash a reference to the removed object in a temporary variable, revise the list data structure, and only then invoke `Py_DECREF()` for that temporary variable.

Changed in version 3.12: Immortal objects are not modified.

 void Py_XDECREF([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Comparable to `Py_DECREF()`, except that here the object *o* is allowed to be `NULL`, in which event nothing happens. The identical warning that accompanies `Py_DECREF()` is in force here too.

 void Py_CLEAR([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Give up a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) for object *o*. The object is allowed to be `NULL`, in which event the macro does nothing; otherwise it behaves just like `Py_DECREF()`, save that the argument is additionally reset to `NULL`. The warning attached to `Py_DECREF()` does not bite with regard to the object handed in, since the macro takes care to use a temporary variable and to reset the argument to `NULL` ahead of releasing the reference.

Reaching for this macro is wise any time you release a reference to an object that could be traversed in the course of garbage collection.

Changed in version 3.12: Evaluation of the macro's argument now happens a single time only; any side effects it carries are therefore not repeated.

 void Py_IncRef([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Signal that you are acquiring a fresh [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to object *o*. A function-form counterpart to `Py_XINCREF()`. It comes in handy for embedding Python dynamically at runtime.

 void Py_DecRef([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Give up a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to object *o*. A function-form counterpart to `Py_XDECREF()`. It comes in handy for embedding Python dynamically at runtime.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](py-refcnt-to-py-xincref.md) · [Following source contract](py-setref-to-py-xsetref.md)
