# Async Object Structures

<a id="async-object-structures"></a>

Async Object Structures: Added in version 3.5.

type PyAsyncMethods

Pointers to the functions needed to realize [awaitable](https://docs.python.org/3.14/glossary.html#term-awaitable) and [asynchronous iterator](https://docs.python.org/3.14/glossary.html#term-asynchronous-iterator) objects are stored in this structure.

Here is the structure definition:

```c
typedef struct {
    unaryfunc am_await;
    unaryfunc am_aiter;
    unaryfunc am_anext;
    sendfunc am_send;
} PyAsyncMethods;

```

 unaryfunc PyAsyncMethods.am_await

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_am_await` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.5.*

Here is the signature of this function:

```c
PyObject *am_await(PyObject *self);

```

What it returns has to be an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator); that is, [`PyIter_Check()`](https://docs.python.org/3.14/c-api/iter.html#c.PyIter_Check) has to yield `1` for it.

Where an object is not an [awaitable](https://docs.python.org/3.14/glossary.html#term-awaitable), this slot may be set to `NULL`.

 unaryfunc PyAsyncMethods.am_aiter

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_am_aiter` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.5.*

Here is the signature of this function:

```c
PyObject *am_aiter(PyObject *self);

```

Has to return an [asynchronous iterator](https://docs.python.org/3.14/glossary.html#term-asynchronous-iterator) object. Refer to [`__anext__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__anext__) for the particulars.

Where an object does not implement the asynchronous iteration protocol, this slot may be set to `NULL`.

 unaryfunc PyAsyncMethods.am_anext

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_am_anext` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.5.*

Here is the signature of this function:

```c
PyObject *am_anext(PyObject *self);

```

Has to return an [awaitable](https://docs.python.org/3.14/glossary.html#term-awaitable) object. Refer to [`__anext__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__anext__) for the particulars. This slot may be set to `NULL`.

 sendfunc PyAsyncMethods.am_send

* The corresponding [slot ID](https://docs.python.org/3.14/c-api/type.html#c.PyType_Slot) `Py_am_send` is part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.10.*

Here is the signature of this function:

```c
PySendResult am_send(PyObject *self, PyObject *arg, PyObject **result);

```

Refer to [`PyIter_Send()`](https://docs.python.org/3.14/c-api/iter.html#c.PyIter_Send) for the particulars. This slot may be set to `NULL`.

Added in version 3.10.

[Subject index](INDEX.md) · [Following source contract](pyobject-to-py-hash-t.md)
