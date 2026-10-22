# Python 3.11.0 alpha 5 / core and builtins / weakref

[bpo-46417](https://bugs.python.org/issue?@action=redirect&bpo=46417): Resolve a race condition while assigning a type's `__bases__` attribute: the internal helper `add_subclass()` now reads the `PyTypeObject.tp_subclasses` member only after [`PyWeakref_NewRef()`](https://docs.python.org/3.14/c-api/weakref.html#c.PyWeakref_NewRef) runs, because that call may launch a garbage collection that can in turn alter `PyTypeObject.tp_subclasses`. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
