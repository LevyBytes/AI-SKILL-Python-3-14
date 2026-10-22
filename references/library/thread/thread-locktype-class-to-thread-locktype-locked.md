# _thread / Low-level threading API: `_thread.LockType`, `acquire()`, `release()`, `locked()`

*class *_thread.LockType

This denotes the type that lock objects have.

The methods carried by lock objects are these:

 acquire(*blocking=True*, *timeout=-1*)

Called with no optional argument, this method takes the lock no matter what, blocking if needed until some other thread lets it go (since only one thread may hold a lock at any moment — which is the whole point of a lock).

When the *blocking* argument is supplied, behavior hinges on its value: a false value means the lock is taken solely when it can be had at once without waiting, whereas a true value means the lock is taken unconditionally, as described above.

When the floating-point *timeout* argument is supplied and positive, it caps how many seconds the call will wait before giving up. A negative *timeout* means wait without limit. You may not supply a *timeout* while *blocking* is false.

What comes back is `True` when the lock was taken successfully and `False` otherwise.

Changed in version 3.2: The *timeout* parameter was added.

Changed in version 3.2: On POSIX, signals can now break into a lock acquisition.

Changed in version 3.14: On Windows, signals can now break into a lock acquisition.

 release()

Lets go of the lock. The lock has to have been taken beforehand, though not necessarily by this same thread.

 locked()

Hand back the lock's state: `True` when some thread is holding it and `False` otherwise.

Beyond these methods, lock objects work with the [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement as well, for instance:

```python
import _thread

a_lock = _thread.allocate_lock()

with a_lock:
    print("a_lock is locked while this executes")

```

**Caveats:**

- Interrupts are always routed to the main thread (it is that thread which gets the [`KeyboardInterrupt`](https://docs.python.org/3.14/library/exceptions.html#KeyboardInterrupt) exception.)

- Invoking [`sys.exit()`](https://docs.python.org/3.14/library/sys.html#sys.exit) or throwing the [`SystemExit`](https://docs.python.org/3.14/library/exceptions.html#SystemExit) exception amounts to the same thing as invoking `_thread.exit()`.

- After the main thread ends, whether the remaining threads carry on is left up to the system. On the majority of systems they are terminated without running their [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) … [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) clauses or invoking object destructors.

[Subject index](INDEX.md) · [Previous](thread-error-to-thread-timeout-max.md) · [Continue](../abc/abc-abc-class.md) · [Owning module, declaration or section: _thread](thread-error-to-thread-timeout-max.md)
