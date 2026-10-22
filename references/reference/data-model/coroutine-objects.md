# 3.4.2. Coroutine Objects

### 3.4.2. Coroutine Objects

Every [Coroutine objects](https://docs.python.org/3.14/glossary.html#term-coroutine) entry is an [awaitable](https://docs.python.org/3.14/glossary.html#term-awaitable) object. You steer how a coroutine runs by invoking `__await__()` and stepping through what it yields. Once the coroutine wraps up and returns, [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) is raised by the iterator, with the return value stored in that exception’s [`value`](https://docs.python.org/3.14/library/exceptions.html#StopIteration.value) attribute. Any exception the coroutine throws gets carried outward by the iterator. A coroutine ought never to let an unhandled `StopIteration` escape on its own.

Beyond that, coroutines expose the methods shown below, paralleling the generator ones (see [Generator-iterator methods](https://docs.python.org/3.14/reference/expressions.html#generator-methods)). That said, coroutines differ from generators in offering no direct iteration support.

A coroutine is [generic](https://docs.python.org/3.14/library/typing.html#generics) across, in order, the types it yields, the types it is sent, and the type it returns.

Changed in version 3.5.2: Awaiting the same coroutine on more than one occasion triggers a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](awaitable-objects.md) · [Previous source section](object-await.md) · [Following source section](coroutine-send.md)
