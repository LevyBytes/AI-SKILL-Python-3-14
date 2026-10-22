# Scheduling callbacks

### Scheduling callbacks

 loop.call_soon(*callback*, **args*, *context=None*)

Schedule the *callback* [callback](https://docs.python.org/3.14/glossary.html#term-callback) so that it runs with *args* arguments on the loop’s next iteration.

Hand back an `asyncio.Handle` instance; you can use it afterward to cancel the callback.

The order in which callbacks register is the order in which they run. Every callback runs precisely once.

Through the optional keyword-only *context* argument you may name a custom [`contextvars.Context`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context) in which the *callback* executes. When no *context* is supplied, callbacks adopt the current context.

In contrast to `call_soon_threadsafe()`, this method offers no thread safety.

 loop.call_soon_threadsafe(*callback*, **args*, *context=None*)

A thread-safe variant of `call_soon()`. To queue callbacks from a different thread you *must* reach for this function, because `call_soon()` is not thread-safe.

Calling this function from a reentrant context or a signal handler is safe; using the returned handle within those contexts, however, is neither safe nor productive.

Raises [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) if called on a loop that’s been closed. On a secondary thread this may occur as the main application winds down.

See the [concurrency and multithreading](https://docs.python.org/3.14/library/asyncio-dev.html#asyncio-multithreading) section of the documentation.

Changed in version 3.7: Introduced the keyword-only *context* parameter. Consult [**PEP 567**](https://peps.python.org/pep-0567/) for further details.

Note

The majority of [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) scheduling functions won’t accept keyword arguments. When you need them, turn to [`functools.partial()`](https://docs.python.org/3.14/library/functools.html#functools.partial):

```python
# will schedule "print("Hello", flush=True)"
loop.call_soon(
    functools.partial(print, "Hello", flush=True))

```

Reaching for partial objects tends to beat lambdas for convenience, since asyncio depicts partial objects more clearly in debug and error messages.

[Subject index](INDEX.md) · [Previous](loop-run-until-complete-to-loop-shutdown-default-executor.md) · [Continue](loop-call-later-to-loop-time.md)
