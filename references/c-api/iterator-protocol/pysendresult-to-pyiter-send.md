# iterator protocol C API: `PySendResult`, `PyIter_Send()`

type PySendResult

The enum value that captures the various outcomes of `PyIter_Send()`.

Added in version 3.10.

 PySendResult PyIter_Send([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *iter, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *arg, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) **presult)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Pushes the *arg* value through to the iterator *iter*. The return values are:

- `PYGEN_RETURN` if iterator returns. Return value is returned via *presult*.

- `PYGEN_NEXT` if iterator yields. Yielded value is returned via *presult*.

- `PYGEN_ERROR` if iterator has raised and exception. *presult* is set to `NULL`.

Added in version 3.10.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pyiter-check-to-pyiter-next.md) · [Following source contract](../iterator-objects/pyseqiter-type-to-pycalliter-new.md)
