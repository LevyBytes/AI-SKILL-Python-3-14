# asyncio.task: `done()`, `result()`, `exception()`, `add_done_callback()`, `remove_done_callback()`, `get_stack()`, `print_stack()`, `get_coro()`, `get_context()`

done()

Return `True` if the Task is *done*.

A Task counts as *done* once the wrapped coroutine has returned a value, raised an exception, or the Task itself was cancelled.

 result()

Return the result of the Task.

When the Task is *done*, you get back the wrapped coroutine’s result (and if that coroutine raised an exception, the exception is re-raised).

When the Task has been *cancelled*, calling this method raises a [`CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) exception.

When the Task’s result has not arrived yet, this method raises an [`InvalidStateError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.InvalidStateError) exception.

 exception()

Return the exception of the Task.

Should the wrapped coroutine have raised an exception, that exception comes back. Should the wrapped coroutine have returned normally, this method gives `None`.

When the Task has been *cancelled*, calling this method raises a [`CancelledError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.CancelledError) exception.

When the Task is not yet *done*, this method raises an [`InvalidStateError`](https://docs.python.org/3.14/library/asyncio-exceptions.html#asyncio.InvalidStateError) exception.

 add_done_callback(*callback*, ***, *context=None*)

Add a callback to be run when the Task is *done*.

Reserve this method for low-level callback-based code only.

See the documentation of [`Future.add_done_callback()`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future.add_done_callback) for more details.

 remove_done_callback(*callback*)

Remove *callback* from the callbacks list.

Reserve this method for low-level callback-based code only.

See the documentation of [`Future.remove_done_callback()`](https://docs.python.org/3.14/library/asyncio-future.html#asyncio.Future.remove_done_callback) for more details.

 get_stack(***, *limit=None*)

Return the list of stack frames for this Task.

When the wrapped coroutine has not finished, you get the stack at its suspension point. When the coroutine has completed successfully or was cancelled, you get an empty list. When an exception ended the coroutine, you get the list of traceback frames.

The order of the frames always runs from oldest to newest.

For a suspended coroutine, just a single stack frame comes back.

The optional *limit* argument caps how many frames are returned; with no value, every available frame is returned. How the returned list is ordered hinges on whether it holds a stack or a traceback: for a stack the newest frames come back, while for a traceback the oldest frames come back. (This lines up with how the traceback module behaves.)

 print_stack(***, *limit=None*, *file=None*)

Print the stack or traceback for this Task.

The output resembles what the traceback module produces for the frames that `get_stack()` collects.

The *limit* argument is passed to `get_stack()` directly.

The *file* argument names an I/O stream that receives the output; with no value given, the output goes to [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout).

 get_coro()

Return the coroutine object wrapped by the `Task`.

Note

For Tasks that already finished eagerly, this gives back `None`. See the Eager Task Factory.

Added in version 3.8.

Changed in version 3.12: With eager task execution now available, the result may turn out to be `None`.

 get_context()

Return the [`contextvars.Context`](https://docs.python.org/3.14/library/contextvars.html#contextvars.Context) object associated with the task.

Added in version 3.12.

[Subject index](INDEX.md) · [Previous](asyncio-task-class.md) · [Continue](asyncio-task-get-name-to-asyncio-task-cancelled.md) · [Owning module, declaration or section: asyncio.Task](asyncio-task-class.md) · [Owning module, declaration or section: Task object](asyncio-task-class.md)
