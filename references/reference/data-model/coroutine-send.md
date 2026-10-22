# coroutine.send(*value*)

coroutine.send(*value*)

Kicks off the coroutine or picks its execution back up. Passing `None` for *value* amounts to stepping the iterator that `__await__()` produced one notch forward. Passing a *value* other than `None` makes this method hand off to the [`send()`](https://docs.python.org/3.14/reference/expressions.html#generator.send) method on whichever iterator put the coroutine to sleep. Whatever comes out (a return value, a [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration), or some other exception) matches the outcome of iterating across the `__await__()` return value covered earlier.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](awaitable-objects.md) · [Owning language section](coroutine-objects.md) · [Previous source section](coroutine-objects.md) · [Following source section](coroutine-exception-injection.md)
