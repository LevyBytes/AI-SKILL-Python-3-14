# 3.2.8.5. Asynchronous generator functions

#### 3.2.8.5. Asynchronous generator functions

Any function or method declared with [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) that also contains the [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) statement is termed a *asynchronous generator function*. Whenever such a function is called, it hands back an [asynchronous iterator](https://docs.python.org/3.14/glossary.html#term-asynchronous-iterator) object that an [`async for`](https://docs.python.org/3.14/reference/compound_stmts.html#async-for) statement can drive to run the function's body.

Invoking that asynchronous iterator's `aiterator.__anext__` method yields an [awaitable](https://docs.python.org/3.14/glossary.html#term-awaitable) that, once awaited, runs until it produces a value through the [`yield`](https://docs.python.org/3.14/reference/simple_stmts.html#yield) expression. Once the function runs an empty [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return) statement or simply reaches its end, a [`StopAsyncIteration`](https://docs.python.org/3.14/library/exceptions.html#StopAsyncIteration) exception fires and the asynchronous iterator has exhausted the collection of values it was meant to yield.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](callable-types.md) · [Previous source section](coroutine-functions.md) · [Following source section](built-in-functions.md)
