# threading: Thread tracing, profiling, stack size and timeout limits

threading.main_thread()

Return the main `Thread` object. Ordinarily this is the very thread that launched the Python interpreter.

Added in version 3.4.

 threading.settrace(*func*)

Install a trace function across all threads that the `threading` module launches. For each thread, *func* is handed to [`sys.settrace()`](https://docs.python.org/3.14/library/sys.html#sys.settrace) ahead of that thread’s `run()` method running.

 threading.settrace_all_threads(*func*)

Install a trace function across every thread launched by the `threading` module together with all Python threads running right now.

For each thread, *func* is handed to [`sys.settrace()`](https://docs.python.org/3.14/library/sys.html#sys.settrace) ahead of that thread’s `run()` method running.

Added in version 3.12.

 threading.gettrace()

Get the trace function as set by `settrace()`.

Added in version 3.10.

 threading.setprofile(*func*)

Install a profile function across all threads that the `threading` module launches. For each thread, *func* is handed to [`sys.setprofile()`](https://docs.python.org/3.14/library/sys.html#sys.setprofile) ahead of that thread’s `run()` method running.

 threading.setprofile_all_threads(*func*)

Install a profile function across every thread launched by the `threading` module together with all Python threads running right now.

For each thread, *func* is handed to [`sys.setprofile()`](https://docs.python.org/3.14/library/sys.html#sys.setprofile) ahead of that thread’s `run()` method running.

Added in version 3.12.

 threading.getprofile()

Get the profiler function as set by `setprofile()`.

Added in version 3.10.

 threading.stack_size([*size*])

Return the stack size applied when fresh threads are made. The optional *size* argument names the stack size for threads created from then on, and it has to be either 0 (meaning the platform or configured default) or a positive integer no smaller than 32,768 (32 KiB). When *size* is omitted, 0 applies. A [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) is raised if altering the thread stack size is not supported. An invalid stack size triggers a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) and leaves the stack size untouched. At present 32 KiB stands as the smallest supported stack size, ensuring the interpreter has enough stack room of its own. Be aware that certain platforms impose their own rules on stack size values, like demanding a minimum above 32 KiB or insisting the allocation fall on multiples of the system memory page size — check the platform documentation for the specifics (pages of 4 KiB are typical; when nothing more precise is known, picking multiples of 4096 for the stack size is recommended).

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Windows, pthreads.

Unix platforms with POSIX threads support.

There is also this constant defined by the module:

 threading.TIMEOUT_MAX

The largest figure permitted for the *timeout* parameter of blocking calls (`Lock.acquire()`, `RLock.acquire()`, `Condition.wait()`, and so on). Passing a timeout above this figure raises an [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError).

Added in version 3.2.

Several classes are defined by this module as well, each covered in the sections that follow.

This module’s design takes loose inspiration from Java’s threading model. Yet whereas Java bakes locks and condition variables into the fundamental behavior of every object, in Python they stand as separate objects. Python’s `Thread` class covers only part of what Java’s Thread class does; at this point there are no priorities, no thread groups, and you cannot destroy, stop, suspend, resume, or interrupt threads. Where they exist, the static methods of Java’s Thread class become module-level functions here.

Each of the methods covered below runs atomically.

[Subject index](INDEX.md) · [Previous](threading-active-count-to-threading-enumerate.md) · [Continue](thread-local-data-section-introduction-and-initial-examples.md) · [Owning module, declaration or section: threading](threading-thread-based-parallelism.md) · [Owning module, declaration or section: Reference](threading-active-count-to-threading-enumerate.md)
