# 3.2.8.4. Coroutine functions

#### 3.2.8.4. Coroutine functions

Any function or method declared with [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) is termed a *coroutine function*. Whenever such a function is called, it hands back a [coroutine](https://docs.python.org/3.14/glossary.html#term-coroutine) object. Inside it may appear [`await`](https://docs.python.org/3.14/reference/expressions.html#await) expressions, together with [`async with`](https://docs.python.org/3.14/reference/compound_stmts.html#async-with) and [`async for`](https://docs.python.org/3.14/reference/compound_stmts.html#async-for) statements. Consult the Coroutine Objects section as well.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](the-standard-type-hierarchy.md) · [Owning language section](callable-types.md) · [Previous source section](generator-functions.md) · [Following source section](asynchronous-generator-functions.md)
