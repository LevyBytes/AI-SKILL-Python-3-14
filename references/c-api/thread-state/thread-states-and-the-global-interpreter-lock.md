# Thread states and the global interpreter lock

### Thread states and the global interpreter lock

Apart from a [free-threaded build](https://docs.python.org/3.14/glossary.html#term-free-threaded-build) of [CPython](https://docs.python.org/3.14/glossary.html#term-CPython), the Python interpreter is, in general, not safe to use across threads. To make multi-threaded Python programs possible, a single global lock — termed the [global interpreter lock](https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock), or [GIL](https://docs.python.org/3.14/glossary.html#term-GIL) — has to be acquired by a thread before it touches any Python objects. Lacking that lock, even trivial operations might misbehave in a multi-threaded setting: consider two threads each bumping the reference count of one shared object at the same moment, where the count might rise by just one rather than two.

For this reason, a thread is only permitted to act on Python objects or call into Python's C API while it holds the GIL.

To approximate parallelism, the interpreter routinely attempts to swap between threads at the boundaries of bytecode instructions (see [`sys.setswitchinterval()`](https://docs.python.org/3.14/library/sys.html#sys.setswitchinterval)). That behavior is precisely why pure-Python code still relies on locks for thread-safety.

Beyond that, the global interpreter lock gets released whenever a blocking I/O operation runs — say, reading from or writing to a file. Within the C API, you achieve this by detaching the thread state.

A bundle of thread-local data, held in a structure named `PyThreadState`, is what the Python interpreter uses to track per-thread details; this is called a [thread state](https://docs.python.org/3.14/glossary.html#term-thread-state). Every thread carries a thread-local pointer aimed at a `PyThreadState`; whenever a thread state is referenced through that pointer, it counts as [attached](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

At any given moment a thread may hold no more than one [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state). Except under free-threaded builds, having an attached thread state generally corresponds to holding the GIL. Where the GIL is enabled, attaching a thread state will stall until the GIL becomes available. Yet even where the GIL is turned off, an attached thread state is still mandatory, since the interpreter must record which threads are allowed to reach Python objects.

Note

Attaching a thread state can stall even under the free-threaded build, because the GIL might get switched back on or threads could be briefly paused (for instance, while garbage collection runs).

For the most part, an attached thread state will already exist whenever you reach for Python's C API — during embedding as well as when you write methods — so configuring a thread state by hand is rarely required. The thread will lack an attached thread state only in particular situations, like within a `Py_BEGIN_ALLOW_THREADS` block or inside a brand-new thread. When in doubt, test whether `PyThreadState_GetUnchecked()` hands back `NULL`.

Should you actually need to build a thread state, invoke `PyThreadState_New()` and then `PyThreadState_Swap()`, or reach for the perilous `PyGILState_Ensure()` function.

[Subject index](INDEX.md) · [Following source contract](detaching-the-thread-state-from-extension-code.md)
