# weak references C API: `PyWeakref_Check()`, `PyWeakref_CheckRef()`, `PyWeakref_CheckRefExact()`, `PyWeakref_CheckProxy()`, `PyWeakref_NewRef()`, `PyWeakref_NewProxy()`, `PyWeakref_GetRef()`, `PyWeakref_GetObject()`, `PyWeakref_GET_OBJECT()`

# Weakref

### Weak Reference Objects

In Python, *weak references* exist as first-class objects. Two particular object types put weak references into practice directly: one is a plain reference object, while the other stands in as a proxy for the original object to whatever extent it's able.

 int PyWeakref_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob)

Yields a non-zero result when *ob* happens to be a reference object or a proxy object. The call can never fail.

 int PyWeakref_CheckRef([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob)

Yields a non-zero result when *ob* is a reference object, or a subclass of the reference type. The call can never fail.

 int PyWeakref_CheckRefExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob)

Yields a non-zero result when *ob* is a reference object that is not a subclass of the reference type. The call can never fail.

 int PyWeakref_CheckProxy([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob)

Yields a non-zero result when *ob* is a proxy object. The call can never fail.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyWeakref_NewRef([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *callback)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back a weak reference object for the object *ob*. A new reference always comes back, though a brand-new object isn't promised — an already-existing reference object might be what you get. That second argument, *callback*, may be a callable that gets notified once *ob* is garbage collected; it ought to take exactly one argument, namely the weak reference object itself. You can also pass `None` or `NULL` as *callback*. Should *ob* not be a weakly referenceable object, the call raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) and hands back `NULL`.

See also

[`PyType_SUPPORTS_WEAKREFS()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_SUPPORTS_WEAKREFS) to test whether *ob* can be weakly referenced.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyWeakref_NewProxy([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *callback)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Hand back a weak reference proxy object for the object *ob*. As before, a new reference is always returned, yet creating a fresh object isn't guaranteed — a proxy object that already exists may instead be handed back. The second argument, *callback*, may be a callable that's notified at the point *ob* is garbage collected; it should expect just one argument, that being the weak reference object itself. Passing `None` or `NULL` for *callback* is permitted too. When *ob* weakly referenceable object, the call raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) and hands back `NULL`.

See also

[`PyType_SUPPORTS_WEAKREFS()`](https://docs.python.org/3.14/c-api/type.html#c.PyType_SUPPORTS_WEAKREFS) to determine whether *ob* admits weak references.

 int PyWeakref_GetRef([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ref, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **pobj)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.13.*

Obtain a [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to the referenced object out of a weak reference, *ref*, placing it into **pobj*.

- When it works, point **pobj* at a new [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) to the referenced object and give back 1.

- Should the reference be dead, point **pobj* at `NULL` and give back 0.

- When something goes wrong, raise an exception and give back -1.

Added in version 3.13.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyWeakref_GetObject([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ref)

*Return value: Borrowed reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Give back a [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) to the referenced object drawn from a weak reference, *ref*. Where the referent has stopped being live, `Py_None` is what comes back.

Note

What this function gives back is a [borrowed reference](https://docs.python.org/3.14/glossary.html#term-borrowed-reference) to the referenced object. Consequently you ought to invoke [`Py_INCREF()`](https://docs.python.org/3.14/c-api/refcounting.html#c.Py_INCREF) on the object in every case but one: when there's no way it could be destroyed ahead of the final use of the borrowed reference.

Deprecated since version 3.13, will be removed in version 3.15: Reach for `PyWeakref_GetRef()` in its place.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyWeakref_GET_OBJECT([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ref)

*Return value: Borrowed reference.*

Much like `PyWeakref_GetObject()`, except that it skips any error checking.

Deprecated since version 3.13, will be removed in version 3.15: Switch to `PyWeakref_GetRef()` instead.

[Subject index](INDEX.md) · [Following source contract](weak-reference-liveness-and-callback-free-cleanup.md)
