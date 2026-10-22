# concurrent.futures: `cancel()`, `cancelled()`, `running()`, `done()`, `result()`, `exception()`, `add_done_callback()`, `set_running_or_notify_cancel()`

cancel()

Try to call off the call. When the call is already executing or has finished and therefore can't be called off, the method gives back `False`; otherwise the call is called off and the method gives back `True`.

 cancelled()

Hand back `True` when the call was cancelled successfully.

 running()

Hand back `True` when the call is executing right now and can't be cancelled.

 done()

Hand back `True` when the call either was cancelled successfully or has finished running.

 result(*timeout=None*)

Hand back whatever value the call produced. Should the call still be unfinished, this method waits as long as *timeout* seconds. If the call isn't finished within *timeout* seconds, a [`TimeoutError`](https://docs.python.org/3.14/library/exceptions.html#TimeoutError) is raised. You may give *timeout* as an int or float. Leave *timeout* out or set it to `None`, and the wait is unbounded.

Should the future be cancelled ahead of finishing, a `CancelledError` is raised.

When the call threw an exception, this method re-raises that very exception.

 exception(*timeout=None*)

Hand back whatever exception the call threw. Should the call still be unfinished, this method waits as long as *timeout* seconds. If the call isn't finished within *timeout* seconds, a [`TimeoutError`](https://docs.python.org/3.14/library/exceptions.html#TimeoutError) is raised. You may give *timeout* as an int or float. Leave *timeout* out or set it to `None`, and the wait is unbounded.

Should the future be cancelled ahead of finishing, a `CancelledError` is raised.

When the call finished without throwing, `None` comes back.

 add_done_callback(*fn*)

Binds the callable *fn* to the future. Once the future is cancelled or wraps up, *fn* is invoked with the future as its sole argument.

The callables you add fire in the sequence they were added, and they always fire on a thread that belongs to the process which added them. Should the callable throw an [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception) subclass, it gets logged and dropped. Should the callable throw a [`BaseException`](https://docs.python.org/3.14/library/exceptions.html#BaseException) subclass, the behavior is left undefined.

Should the future already have wrapped up or been cancelled, *fn* fires straight away.

The `Future` methods listed below are intended for unit tests and for `Executor` implementations.

 set_running_or_notify_cancel()

[Subject index](INDEX.md) · [Previous](concurrent-futures-future-class.md) · [Owning module, declaration or section: concurrent.futures.Future](concurrent-futures-future-class.md) · [Owning module, declaration or section: Future Objects](concurrent-futures-future-class.md)
