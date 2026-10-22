# inspect — Code Objects Bit Flags

### Code Objects Bit Flags

Every Python code object carries a [`co_flags`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_flags) attribute, a bitmap built from the flags listed below:

 inspect.CO_OPTIMIZED

The code object has been optimized to rely on fast locals.

 inspect.CO_NEWLOCALS

When this is set, running the code object brings a fresh dict into existence for the frame’s [`f_locals`](https://docs.python.org/3.14/reference/datamodel.html#frame.f_locals).

 inspect.CO_VARARGS

The code object takes a variadic positional parameter (in the style of `*args`).

 inspect.CO_VARKEYWORDS

The code object takes a variadic keyword parameter (in the style of `**kwargs`).

 inspect.CO_NESTED

This flag turns on whenever the code object belongs to a nested function.

 inspect.CO_GENERATOR

This flag turns on whenever the code object belongs to a generator function — that is, executing the code object hands back a generator object.

 inspect.CO_COROUTINE

This flag turns on whenever the code object belongs to a coroutine function. Executing that code object yields a coroutine object. Consult [**PEP 492**](https://peps.python.org/pep-0492/) for the full account.

Added in version 3.5.

 inspect.CO_ITERABLE_COROUTINE

This flag serves to convert generators into generator-based coroutines. A generator object carrying it may appear in an `await` expression and may `yield from` coroutine objects. Consult [**PEP 492**](https://peps.python.org/pep-0492/) for the full account.

Added in version 3.5.

 inspect.CO_ASYNC_GENERATOR

This flag turns on whenever the code object belongs to an asynchronous generator function. Executing that code object yields an asynchronous generator object. Consult [**PEP 525**](https://peps.python.org/pep-0525/) for the full account.

Added in version 3.6.

 inspect.CO_HAS_DOCSTRING

This flag turns on whenever the source carries a docstring for the code object. When it is set, that docstring occupies the first slot of [`co_consts`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_consts).

Added in version 3.14.

 inspect.CO_METHOD

This flag turns on whenever the code object is a function declared within class scope.

Added in version 3.14.

Note

These flags are particular to CPython and might be absent from other Python implementations. They are, moreover, an implementation detail, so future Python releases may drop or deprecate them. For whatever introspection you require, leaning on the public APIs of the `inspect` module is the advised course.

[Subject index](INDEX.md) · [Previous](inspect-getgeneratorlocals-to-inspect-getasyncgenlocals.md) · [Continue](inspect-bufferflags-class.md) · [Owning module, declaration or section: inspect](inspect-inspect-live-objects.md)
