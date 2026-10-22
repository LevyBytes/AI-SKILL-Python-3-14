# Instance Method Objects

## Instance Method Objects

### Instance Method Objects

An instance method wraps a [`PyCFunction`](https://docs.python.org/3.14/c-api/structures.html#c.PyCFunction) and is the current means of binding a `PyCFunction` onto a class object. It stands in for what used to be the `PyMethod_New(func, NULL, class)` call.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyInstanceMethod_Type

Standing in for the Python instance method type, this [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) instance is never surfaced to Python programs.

 int PyInstanceMethod_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Yield true when *o* is an instance method object — that is, one of type `PyInstanceMethod_Type`. The argument is not allowed to be `NULL`. This call can never fail.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyInstanceMethod_New([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *func)

*Return value: New reference.*

Produce a fresh instance method object, where *func* may be any callable object. That *func* is what gets invoked once the instance method itself is invoked.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyInstanceMethod_Function([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *im)

*Return value: Borrowed reference.*

Hand back the function object that the instance method *im* is tied to.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyInstanceMethod_GET_FUNCTION([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *im)

*Return value: Borrowed reference.*

A macro form of `PyInstanceMethod_Function()` that skips the error checking.

[Subject index](INDEX.md) · [Previous source contract](../memoryview-objects/pymemoryview-type-to-pymemoryview-get-base.md) · [Following source contract](pymethod-type-to-pymethod-get-self.md)
