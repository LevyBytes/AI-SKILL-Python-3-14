# 3.4.3. Asynchronous Iterators

### 3.4.3. Asynchronous Iterators

Within its `__anext__` method, an *asynchronous iterator* is free to invoke asynchronous code.

You can drive asynchronous iterators from inside an [`async for`](https://docs.python.org/3.14/reference/compound_stmts.html#async-for) statement.

These methods are absent from the bare [`object`](https://docs.python.org/3.14/library/functions.html#object) class.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](awaitable-objects.md) · [Previous source section](coroutine-close.md) · [Following source section](object-aiter.md)
