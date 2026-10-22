# Method Objects

### Method Objects

A method is a function object that carries a binding, and that binding is invariably to an instance of some user-defined class. The old notion of unbound methods — ones bound to a class object instead — has been dropped.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyMethod_Type

Standing in for the Python method type, this [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) instance is presented to Python programs under the name `types.MethodType`.

 int PyMethod_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *o)

Yield true when *o* is a method object — one whose type is `PyMethod_Type`. The argument may not be `NULL`. This call can never fail.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyMethod_New([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *func, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *self)

*Return value: New reference.*

Produce a fresh method object, where *func* is any callable object and *self* is the instance the method ought to be bound to. That *func* is what runs once the method is invoked, and *self* may not be `NULL`.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyMethod_Function([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *meth)

*Return value: Borrowed reference.*

Hand back the function object that the method *meth* is tied to.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyMethod_GET_FUNCTION([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *meth)

*Return value: Borrowed reference.*

A macro form of `PyMethod_Function()` that skips the error checking.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyMethod_Self([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *meth)

*Return value: Borrowed reference.*

Hand back the instance that the method *meth* is tied to.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyMethod_GET_SELF([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *meth)

*Return value: Borrowed reference.*

A macro form of `PyMethod_Self()` that skips the error checking.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyinstancemethod-type-to-pyinstancemethod-get-function.md)
