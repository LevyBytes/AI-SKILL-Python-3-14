# threading.Thread: `start()`, `run()`, `join()`, `getName()`, `setName()`

start()

Start the thread’s activity.

You may call it no more than once for each thread object. It sets things up so the object’s `run()` method runs within a separate thread of control.

Calling this method a second time on the same thread object will raise a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

Where the platform allows, give the operating system thread the name `threading.Thread.name`. Depending on the operating system’s thread-name limits, that name may be cut short.

Changed in version 3.14: Set the operating system thread name.

 run()

Method representing the thread’s activity.

This method can be overridden in a subclass. The default `run()` method calls whatever callable object was passed as the *target* argument to the object’s constructor (if any), using positional and keyword arguments drawn from the *args* and *kwargs* arguments in turn.

Supplying a list or tuple as the *args* argument passed to the `Thread` reaches the same result.

Example:

```python
>>> from threading import Thread
>>> t = Thread(target=print, args=[1])
>>> t.run()
1
>>> t = Thread(target=print, args=(1,))
>>> t.run()
1

```

 join(*timeout=None*)

Wait until the thread terminates. This holds the calling thread back until the thread on which `join()` was called finishes — be that normally or by way of an exception that goes uncaught — or until the optional timeout elapses.

Whenever the *timeout* argument is supplied and is not `None`, it ought to be a floating-point number giving, in seconds (or fractions thereof), how long the operation may run. Since `join()` always hands back `None`, you have to call `is_alive()` once `join()` returns to tell whether a timeout struck — a thread still alive means the `join()` call timed out.

Whenever the *timeout* argument is missing or `None`, the operation blocks until the thread finishes.

You may join a thread any number of times.

`join()` raises a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) should you try to join the current thread, since that would produce a deadlock. Likewise, calling `join()` on a thread that has not been started yet is an error, and such attempts raise that same exception.

Should you try to join a daemonic thread still running during the late phases of [Python finalization](https://docs.python.org/3.14/glossary.html#term-interpreter-shutdown), `join()` raises a [`PythonFinalizationError`](https://docs.python.org/3.14/library/exceptions.html#PythonFinalizationError).

Changed in version 3.14: May raise [`PythonFinalizationError`](https://docs.python.org/3.14/library/exceptions.html#PythonFinalizationError).

 name

A string serving solely for identification. It carries no semantics. The same name may be assigned to multiple threads. The constructor sets the initial name.

On certain platforms, the thread’s name is registered at the operating system level once the thread starts, making it show up in task managers. To fit a system-specific cap, this name may be cut short (for instance, 15 bytes on Linux or 63 bytes on macOS).

Edits to *name* show up at the OS level only when the thread doing the renaming is the one currently running. (Assigning the *name* attribute of some other thread merely refreshes the Python Thread object.)

 getName()

 setName()

Deprecated getter/setter API for `name`; use it directly as a property instead.

Deprecated since version 3.10.

 ident

This thread’s ‘thread identifier’, or `None` while the thread has yet to be started. The value is a nonzero integer. Refer to the `get_ident()` function. After one thread ends and a fresh thread is made, thread identifiers may be reused. The identifier stays available even once the thread has ended.

 native_id

This thread’s Thread ID (`TID`), as handed out by the OS (kernel). It is a non-negative integer, or `None` while the thread has yet to be started. Refer to the `get_native_id()` function. You can use this value to single out this exact thread across the whole system (right up until the thread ends, after which the OS may reuse the value).

Note

Much like Process IDs, Thread IDs hold meaning (guaranteed unique system-wide) only over the span from when the thread is made until the thread has ended.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows, FreeBSD, Linux, macOS, OpenBSD, NetBSD, AIX, DragonFlyBSD.

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](threading-thread-class.md) · [Continue](threading-thread-is-alive.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md) · [Owning module, declaration or section: threading.Thread](threading-thread-class.md) · [Owning module, declaration or section: Thread objects](threading-thread-class.md)
