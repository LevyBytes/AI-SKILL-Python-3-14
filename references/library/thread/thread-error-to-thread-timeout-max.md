# _thread: `_thread.error`, `_thread.start_new_thread()`, `_thread.interrupt_main()`, `_thread.exit()`, `_thread.allocate_lock()`, `_thread.get_ident()`, `_thread.get_native_id()`, `_thread.stack_size()`, `_thread.TIMEOUT_MAX`

### `_thread` - Low-level threading API

---

This module exposes low-level building blocks for driving several threads at once (sometimes termed *light-weight processes* or *tasks*) — that is, multiple flows of control that share one global data space. To coordinate them, plain locks (also known as *mutexes* or *binary semaphores*) are supplied. Layered on top of this module, the [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module offers a friendlier, higher-level threading API.

Changed in version 3.7: Once an optional module, it is now present at all times.

The constants and functions this module defines are as follows:

 *exception *_thread.error

Thrown when thread-specific errors occur.

Changed in version 3.3: It is now simply another name for the built-in [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError).

 _thread.start_new_thread(*function*, *args*[, *kwargs*])

Launch a fresh thread and hand back its identifier. That thread runs *function* against the argument list *args* (which has to be a tuple). The optional *kwargs* argument provides a dictionary of keyword arguments.

Once the function comes back, the thread quietly shuts down.

Should the function end with an exception nobody handled, [`sys.unraisablehook()`](https://docs.python.org/3.14/library/sys.html#sys.unraisablehook) gets invoked to deal with it. On the hook argument, the *object* attribute is *function*. The default behavior prints a stack trace and then the thread shuts down (while the remaining threads keep running).

Should the function throw a [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit) exception, that exception is quietly swallowed.

Raises an [auditing event](https://docs.python.org/3.14/library/sys.html#auditing) `_thread.start_new_thread` with arguments `function`, `args`, `kwargs`.

Changed in version 3.8: Unhandled exceptions are now dealt with through [`sys.unraisablehook()`](https://docs.python.org/3.14/library/sys.html#sys.unraisablehook).

 _thread.interrupt_main(*signum=signal.SIGINT*, */*)

Mimic what would happen if a signal reached the main thread. One thread can call this to interrupt the main thread, although nothing promises the interruption will land right away.

When supplied, *signum* names the signal number to mimic. With *signum* left out, [`signal.SIGINT`](https://docs.python.org/3.14/library/signal.html#signal.SIGINT) is the one mimicked.

Where Python is not handling the given signal (it was assigned [`signal.SIG_DFL`](https://docs.python.org/3.14/library/signal.html#signal.SIG_DFL) or [`signal.SIG_IGN`](https://docs.python.org/3.14/library/signal.html#signal.SIG_IGN)), this function has no effect.

Changed in version 3.10: The *signum* argument was introduced so the signal number can be tailored.

Note

Rather than actually firing the matching signal, this queues a call to that signal's handler (where one is defined). To genuinely fire the signal, turn to [`signal.raise_signal()`](https://docs.python.org/3.14/library/signal.html#signal.raise_signal).

 _thread.exit()

Throw the [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit) exception. Left uncaught, it makes the thread shut down quietly.

 _thread.allocate_lock()

Hand back a fresh lock object. The methods locks expose are documented further down. A newly created lock starts out unlocked.

 _thread.get_ident()

Hand back the ‘thread identifier’ belonging to the calling thread. This comes as a nonzero integer whose value carries no inherent significance; treat it as a magic cookie, handy for instance as a key into a dictionary of thread-specific data. After a thread shuts down and a new one is spawned, these identifiers may be reused.

 _thread.get_native_id()

Hand back the native integral Thread ID the kernel gave the calling thread. This is a non-negative integer that can pin down this exact thread across the whole system (right up until the thread ends, at which point the OS may reuse the value).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows, FreeBSD, Linux, macOS, OpenBSD, NetBSD, AIX, DragonFlyBSD, GNU/kFreeBSD.

Added in version 3.8.

Changed in version 3.13: Gained support for GNU/kFreeBSD.

 _thread.stack_size([*size*])

Hand back the thread stack size applied when spawning new threads. The optional *size* argument sets the stack size for threads created from that point on; it has to be either 0 (meaning the platform or configured default) or a positive integer no smaller than 32,768 (32 KiB). Leave *size* out and 0 is assumed. Where adjusting the thread stack size is not supported, a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) gets raised. Where the size you give is invalid, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised and the stack size stays as it was. At present 32 KiB is the smallest supported stack size, chosen to leave the interpreter itself enough room. Keep in mind that certain platforms impose their own constraints on stack-size values, perhaps demanding a floor above 32 KiB or insisting the allocation be a multiple of the system memory page size — consult the platform documentation for specifics (pages of 4 KiB are typical; absent firmer guidance, sticking to multiples of 4096 for the stack size is the recommended route).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows, pthreads.

Unix platforms that carry POSIX threads support.

 _thread.TIMEOUT_MAX

The ceiling permitted for the *timeout* parameter of [`Lock.acquire`](https://docs.python.org/3.14/library/threading.html#threading.Lock.acquire). Handing it a timeout above this ceiling triggers an [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError).

Added in version 3.2.

[Subject index](INDEX.md) · [Previous](low-level-threading-api.md) · [Continue](thread-locktype-class-to-thread-locktype-locked.md)
