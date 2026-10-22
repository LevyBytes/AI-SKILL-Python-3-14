# threading: `threading.active_count()`, `threading.current_thread()`, `threading.excepthook()`, `threading.__excepthook__`, `threading.get_ident()`, `threading.get_native_id()`, `threading.enumerate()`

### Reference

The functions listed here are defined by this module:

 threading.active_count()

Return how many `Thread` objects are alive at the moment. That total matches the length of the list that `enumerate()` hands back.

The name `activeCount` is a deprecated alias pointing at this function.

 threading.current_thread()

Return the `Thread` object for the present thread, the one belonging to the caller’s thread of control. When the caller’s thread of control did not originate from the `threading` module, you instead get back a dummy thread object whose capabilities are restricted.

The name `currentThread` is a deprecated alias pointing at this function.

 threading.excepthook(*args*, */*)

Handle uncaught exception raised by `Thread.run()`.

The *args* argument carries these attributes:

- *exc_type*: Exception type.

- *exc_value*: Exception value, can be `None`.

- *exc_traceback*: Exception traceback, can be `None`.

- *thread*: Thread which raised the exception, can be `None`.

When *exc_type* is [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit), the exception is quietly dropped. In every other case it is written out to [`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr).

Should this function itself raise an exception, [`sys.excepthook()`](https://docs.python.org/3.14/library/sys.html#sys.excepthook) is invoked to deal with it.

You may replace `threading.excepthook()` to dictate the way uncaught exceptions from `Thread.run()` get processed.

Keeping *exc_value* around through a custom hook may form a reference cycle. To break that cycle, clear it deliberately once you no longer require the exception.

Holding onto *thread* via a custom hook risks reviving it when it points to an object in the middle of being finalized. So that finalized objects are not brought back, refrain from retaining *thread* once the custom hook has returned.

See also

[`sys.excepthook()`](https://docs.python.org/3.14/library/sys.html#sys.excepthook) handles uncaught exceptions.

Added in version 3.8.

 threading.__excepthook__

Keeps the original `threading.excepthook()` value. Preserving it means the original can be put back should it ever be swapped out for broken or substitute objects.

Added in version 3.10.

 threading.get_ident()

Return the ‘thread identifier’ belonging to the current thread. The result is a nonzero integer. Its value carries no inherent meaning; treat it as a magic cookie, handy for instance as a key into a dictionary holding per-thread data. After one thread finishes and a fresh thread spins up, identifiers may be reused.

Added in version 3.3.

 threading.get_native_id()

Return the native integer Thread ID that the kernel has handed the current thread. The result is a non-negative integer. You can rely on it to single out this exact thread across the whole system (right up until the thread ends, after which the OS may reuse that value).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows, FreeBSD, Linux, macOS, OpenBSD, NetBSD, AIX, DragonFlyBSD, GNU/kFreeBSD.

Added in version 3.8.

Changed in version 3.13: Added support for GNU/kFreeBSD.

 threading.enumerate()

Return a list holding every `Thread` object that is currently active. Daemonic threads and the dummy thread objects produced by `current_thread()` are all included. Threads that have ended, plus those not yet launched, are left out. The main thread, however, always shows up in the list, even once it has ended.

[Subject index](INDEX.md) · [Previous](gil-and-performance-considerations.md) · [Continue](threading-main-thread-to-threading-timeout-max.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md)
