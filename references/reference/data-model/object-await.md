# object.__await__(*self*)

object.__await__(*self*)

Has to give back an [iterator](https://docs.python.org/3.14/glossary.html#term-iterator). It is the recommended way to build [awaitable](https://docs.python.org/3.14/glossary.html#term-awaitable) objects. As an example, [`asyncio.Future`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future) defines this method so that it works alongside the [`await`](https://docs.python.org/3.14/reference/expressions.html#await) expression. On its own the [`object`](https://docs.python.org/3.14/library/functions.html#object) class is neither awaitable nor an implementer of this method.

Note

No constraint is imposed by the language on either the type or the value of whatever the `__await__` iterator yields, since that depends entirely on the particular asynchronous execution framework (such as [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio)) charged with overseeing the [awaitable](https://docs.python.org/3.14/glossary.html#term-awaitable) object.

Added in version 3.5.

See also

[**PEP 492**](https://peps.python.org/pep-0492/) covers awaitable objects in greater depth.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](awaitable-objects.md) · [Previous source section](awaitable-objects.md) · [Following source section](coroutine-objects.md)
