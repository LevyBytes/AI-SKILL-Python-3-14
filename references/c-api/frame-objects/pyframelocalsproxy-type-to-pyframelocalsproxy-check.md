# Frame locals proxies

### Frame locals proxies

Added in version 3.13.

On a [frame object](https://docs.python.org/3.14/reference/datamodel.html#frame-objects), the [`f_locals`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_locals) attribute is an instance of a “frame-locals proxy”. What the proxy object presents is a write-through view onto the frame's underlying locals dictionary. That guarantees the variables `f_locals` surfaces stay in step with the live local variables inside the frame itself.

Turn to [**PEP 667**](https://peps.python.org/pep-0667/) for further detail.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyFrameLocalsProxy_Type

The type that frame [`locals()`](https://docs.python.org/3.14/library/functions.html#locals) proxy objects carry.

 int PyFrameLocalsProxy_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *obj)

Hand back non-zero whenever *obj* is a frame [`locals()`](https://docs.python.org/3.14/library/functions.html#locals) proxy.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyframeobject-to-pyframe-getgenerator.md) · [Previous source contract](pyframe-getglobals-to-pyframe-getlinenumber.md) · [Following source contract](pyframe-localstofast-to-pyframe-fasttolocalswitherror.md)
