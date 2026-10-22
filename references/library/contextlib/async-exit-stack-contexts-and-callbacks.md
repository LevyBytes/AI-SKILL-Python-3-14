# contextlib / Utilities: `contextlib.AsyncExitStack`, `enter_async_context()`, `push_async_exit()`, `push_async_callback()`

*class *contextlib.AsyncExitStack

An [asynchronous context manager](https://docs.python.org/3.14/reference/datamodel.html#async-context-managers), akin to `ExitStack`, capable of pooling both synchronous and asynchronous context managers and of holding coroutines for cleanup logic.

There is no `close()` method here; reach for `aclose()` in its place.

 *async *enter_async_context(*cm*)

Akin to `ExitStack.enter_context()`, but it anticipates an asynchronous context manager.

Changed in version 3.11: when *cm* is not an asynchronous context manager, [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is now raised rather than [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError).

 push_async_exit(*exit*)

Akin to `ExitStack.push()`, but it anticipates either an asynchronous context manager or a coroutine function.

 push_async_callback(*callback*, */*, **args*, ***kwds*)

[Subject index](INDEX.md) · [Previous](contextlib-exitstack-class-to-contextlib-exitstack-close.md) · [Owning module, declaration or section: contextlib](contextlib-utilities-for-with-statement-contexts.md) · [Owning module, declaration or section: Utilities](contextlib-abstractcontextmanager-class.md) · [Required continuation of the source contract](contextlib-asyncexitstack-aclose.md)
