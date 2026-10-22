# 3.4.1. Awaitable Objects

### 3.4. Coroutines

### 3.4.1. Awaitable Objects

Typically an [awaitable](https://docs.python.org/3.14/glossary.html#term-awaitable) object supplies an `__await__()` method. The [Coroutine objects](https://docs.python.org/3.14/glossary.html#term-coroutine) that [`async def`](https://docs.python.org/3.14/reference/compound_stmts.html#async-def) functions hand back qualify as awaitable.

Note

When a generator wears the [`types.coroutine()`](https://docs.python.org/3.14/library/types.html#types.coroutine) decorator, the [generator iterator](https://docs.python.org/3.14/glossary.html#term-generator-iterator) it yields counts as awaitable too, yet it offers no `__await__()` method.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Previous source section](special-method-lookup.md) · [Following source section](object-await.md)
