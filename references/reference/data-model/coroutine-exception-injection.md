# coroutine.throw(*value*) / coroutine.throw(*type*[, *value*[, *traceback*]])

coroutine.throw(*value*)

 coroutine.throw(*type*[, *value*[, *traceback*]])

Throws the given exception inside the coroutine. Provided the iterator that suspended the coroutine owns a [`throw()`](https://docs.python.org/3.14/reference/expressions.html#generator.throw) method, this call hands off to it. Failing that, the exception fires at the point of suspension. Whatever results (a return value, a [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration), or another exception) lines up with iterating across the `__await__()` return value covered earlier. Should the coroutine fail to catch the exception, it travels back up to the caller.

Changed in version 3.12: Marked deprecated, the alternate `type[, value[, traceback]]` signature could disappear in some later Python release.

[Subject index](INDEX.md) · [Owning language section](objects-values-and-types.md) · [Owning language section](awaitable-objects.md) · [Owning language section](coroutine-objects.md) · [Previous source section](coroutine-send.md) · [Following source section](coroutine-close.md)
