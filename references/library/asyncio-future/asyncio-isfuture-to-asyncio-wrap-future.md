# Future Functions

### Future Functions

 asyncio.isfuture(*obj*)

Yields `True` whenever *obj* falls into any of these:

- an instance of `asyncio.Future`,

- an instance of [`asyncio.Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task),

- a Future-like object carrying a `_asyncio_future_blocking` attribute.

Added in version 3.5.

 asyncio.ensure_future(*obj*, ***, *loop=None*)

Return:

- *obj* untouched, when *obj* already is a `Future`, a [`Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task), or a Future-like object (the check here uses `isfuture()`.)

- a [`Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) object that wraps *obj*, when *obj* turns out to be a coroutine (verified via [`iscoroutine()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.iscoroutine)); the coroutine then gets scheduled through `ensure_future()`.

- a [`Task`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.Task) object set to await *obj*, when *obj* is an awaitable (verified via [`inspect.isawaitable()`](https://docs.python.org/3.14/library/inspect.html#inspect.isawaitable).)

When *obj* matches none of the above, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) gets raised.

Important

Hold on to a reference to whatever this function returns, so the task does not vanish partway through running.

Consult as well the [`create_task()`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.create_task) function, the recommended route for spawning fresh tasks, or lean on [`asyncio.TaskGroup`](https://docs.python.org/3.14/library/asyncio-task.html#asyncio.TaskGroup), which retains the task reference for you.

Changed in version 3.5.1: Now the function takes any [awaitable](https://docs.python.org/3.14/glossary.html#term-awaitable) object.

Deprecated since version 3.10: A deprecation warning fires when *obj* is not a Future-like object, *loop* goes unspecified, and no event loop is running.

 asyncio.wrap_future(*future*, ***, *loop=None*)

Enclose a [`concurrent.futures.Future`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.Future) object inside an `asyncio.Future` object.

Deprecated since version 3.10: A deprecation warning fires when *future* is not a Future-like object, *loop* goes unspecified, and no event loop is running.

[Subject index](INDEX.md) · [Previous](futures.md) · [Continue](asyncio-future-class.md)
