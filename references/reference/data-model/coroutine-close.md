# coroutine.close()

coroutine.close()

Makes the coroutine tidy up after itself and shut down. For a suspended coroutine, the call begins by deferring to the [`close()`](https://docs.python.org/3.14/reference/expressions.html#generator.close) method on the iterator that suspended it, assuming such a method exists. Next, [`GeneratorExit`](https://docs.python.org/3.14/library/exceptions.html#GeneratorExit) is thrown at the suspension point, prompting the coroutine to tidy up right away. To finish, the coroutine is flagged as done running, even when it never actually began.

As a coroutine object nears destruction, that very procedure shuts it down for you automatically.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](awaitable-objects.md) · [Owning language section](coroutine-objects.md) · [Previous source section](coroutine-exception-injection.md) · [Following source section](asynchronous-iterators.md)
