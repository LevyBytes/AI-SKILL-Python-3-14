# thread state C API: `PyThread_set_stacksize()`, `PyThread_get_stacksize()`

int PyThread_set_stacksize(size_t size)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Configure the running thread's stack size to *size* bytes.

The return value is `0` when it works, `-1` when *size* is not valid, and `-2` when the platform offers no way to alter the stack size. No exceptions get set by this routine.

For the caller, holding an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state) is not necessary.

 size_t PyThread_get_stacksize(void)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Report, in bytes, the running thread's stack size, or `0` whenever the platform's default stack size is what's active.

There is no need for the caller to be holding an [attached thread state](https://docs.python.org/3.14/glossary.html#term-attached-thread-state).

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pythread-start-new-thread-to-pythread-init-thread.md)
