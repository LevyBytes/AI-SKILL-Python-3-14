# 3.4.4. Asynchronous Context Managers

### 3.4.4. Asynchronous Context Managers

A *context manager* qualifies as an *asynchronous context manager* when it can pause execution within both its `__aenter__` and `__aexit__` methods.

An [`async with`](https://docs.python.org/3.14/reference/compound_stmts.html#async-with) statement is where asynchronous context managers come into play.

The plain [`object`](https://docs.python.org/3.14/library/functions.html#object) class supplies none of these methods on its own.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](awaitable-objects.md) · [Previous source section](object-anext.md) · [Following source section](object-aenter.md)
