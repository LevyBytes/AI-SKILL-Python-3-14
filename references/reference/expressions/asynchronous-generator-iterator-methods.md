# 6.2.10.4. Asynchronous generator-iterator methods

#### 6.2.10.4. Asynchronous generator-iterator methods

This subsection covers the methods of an asynchronous generator iterator, which serve to govern how a generator function runs.

 *async *agen.__anext__()

Hands back an awaitable that, once run, begins executing the asynchronous generator or picks it up again at the yield expression that ran most recently. Whenever an asynchronous generator function resumes through an `__anext__()` method, the active yield expression evaluates to [`None`](https://docs.python.org/3.14/library/constants.html#None) within the returned awaitable, which upon running advances to the following yield expression. The `yield_list` value of the yield expression becomes the value of the [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) exception that the finishing coroutine raises. Should the asynchronous generator finish without producing a further value, the awaitable instead raises a [`StopAsyncIteration`](https://docs.python.org/3.14/library/exceptions.html#StopAsyncIteration) exception, indicating that the asynchronous iteration has wrapped up.

Ordinarily this method gets invoked behind the scenes by an [`async for`](https://docs.python.org/3.14/reference/compound_stmts.html#async-for) loop.

 *async *agen.asend(*value*)

Hands back an awaitable that, once run, picks the asynchronous generator back up. Like the `send()` method does for an ordinary generator, this "sends" a value into the asynchronous generator function, and that *value* argument turns into the outcome of the active yield expression. The awaitable that `asend()` produces will return the generator's next yielded value as the value of the raised [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration), or it raises [`StopAsyncIteration`](https://docs.python.org/3.14/library/exceptions.html#StopAsyncIteration) should the asynchronous generator finish without producing another value. When you call `asend()` to start the asynchronous generator, it has to be called with [`None`](https://docs.python.org/3.14/library/constants.html#None) as the argument, since no yield expression yet exists that could accept the value.

 *async *agen.athrow(*value*)

 *async *agen.athrow(*type*[, *value*[, *traceback*]])

Hands back an awaitable that throws an exception of type `type` at the spot where the asynchronous generator had paused, and returns the generator function's next yielded value as the value of the raised [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) exception. Should the asynchronous generator finish without producing a further value, the awaitable raises a [`StopAsyncIteration`](https://docs.python.org/3.14/library/exceptions.html#StopAsyncIteration) exception. When the generator function neither catches the supplied exception nor raises some different one, then running the awaitable propagates that exception to the awaitable's caller.

Changed in version 3.12: The alternate signature (type[, value[, traceback]]) now carries a deprecation and could disappear in some later Python release.

 *async *agen.aclose()

Hands back an awaitable that, once run, throws a [`GeneratorExit`](https://docs.python.org/3.14/library/exceptions.html#GeneratorExit) into the asynchronous generator function at the spot where it had paused. When the asynchronous generator function then finishes cleanly, is already closed, or raises `GeneratorExit` (by leaving the exception uncaught), then the returned awaitable raises a [`StopIteration`](https://docs.python.org/3.14/library/exceptions.html#StopIteration) exception. Every later awaitable produced by subsequent calls to the asynchronous generator will raise a [`StopAsyncIteration`](https://docs.python.org/3.14/library/exceptions.html#StopAsyncIteration) exception. Should the asynchronous generator produce a value, the awaitable raises a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError). Any other exception the asynchronous generator throws is forwarded to the awaitable's caller. When the asynchronous generator has already terminated, whether through an exception or a normal exit, then later calls to `aclose()` hand back an awaitable that has no effect.

[Subject index](INDEX.md) · [Owning language section](expressions.md) · [Owning language section](atoms.md) · [Owning language section](yield-expressions.md) · [Previous source section](asynchronous-generator-functions.md) · [Following source section](primaries.md)
