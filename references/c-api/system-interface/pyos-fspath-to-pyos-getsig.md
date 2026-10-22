# system interface C API: `PyOS_FSPath()`, `Py_FdIsInteractive()`, `PyOS_BeforeFork()`, `PyOS_AfterFork_Parent()`, `PyOS_AfterFork_Child()`, `PyOS_AfterFork()`, `PyOS_CheckStack()`, `PyOS_getsig()`

# Sys

### Operating System Utilities

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyOS_FSPath([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *path)

*Return value: New reference.** Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) since version 3.6.*

Produce the file system representation that corresponds to *path*. When the supplied object is either a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) or a [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes), a fresh [strong reference](https://docs.python.org/3.14/glossary.html#term-strong-reference) comes back. Should the object instead satisfy the [`os.PathLike`](https://docs.python.org/3.14/library/os.html#os.PathLike) protocol, the value of [`__fspath__()`](https://docs.python.org/3.14/library/os.html#os.PathLike.__fspath__) is handed back provided it yields a `str` or `bytes`. In every other case a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) gets raised and `NULL` comes back.

Added in version 3.6.

 int Py_FdIsInteractive(FILE *fp, const char *filename)

Yield true (nonzero) when the standard I/O file *fp* carrying the name *filename* is judged to be interactive. That holds for any file where `isatty(fileno(fp))` evaluates true. When [`PyConfig.interactive`](https://docs.python.org/3.14/c-api/init_config.html#c.PyConfig.interactive) is non-zero, the routine likewise yields true if the *filename* pointer happens to be `NULL`, or if the name matches either of the strings `'<stdin>'` or `'???'`.

You must not invoke this routine before Python has been initialized.

 void PyOS_BeforeFork()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) on platforms with fork() since version 3.7.*

A routine that readies certain internal state ahead of a process fork. Invoke it prior to running `fork()` or any comparable routine that duplicates the running process. It exists only on systems where `fork()` is defined.

Warning

Issue the C `fork()` call solely from the [“main” thread](https://docs.python.org/3.14/c-api/threads.html#fork-and-threads) (within the [“main” interpreter](https://docs.python.org/3.14/c-api/subinterpreters.html#sub-interpreter-support)). That restriction applies equally to `PyOS_BeforeFork()`.

Added in version 3.7.

 void PyOS_AfterFork_Parent()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) on platforms with fork() since version 3.7.*

A routine that refreshes certain internal state once a process fork has happened. Invoke it within the parent process after running `fork()` or any comparable routine that duplicates the running process, no matter whether the cloning operation succeeded. It exists only on systems where `fork()` is defined.

Warning

Issue the C `fork()` call solely from the [“main” thread](https://docs.python.org/3.14/c-api/threads.html#fork-and-threads) (within the [“main” interpreter](https://docs.python.org/3.14/c-api/subinterpreters.html#sub-interpreter-support)). That restriction applies equally to `PyOS_AfterFork_Parent()`.

Added in version 3.7.

 void PyOS_AfterFork_Child()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) on platforms with fork() since version 3.7.*

A routine that refreshes internal interpreter state once a process fork has happened. Invoke it within the child process after running `fork()`, or any comparable routine that duplicates the running process, whenever there is any prospect the process will re-enter the Python interpreter. It exists only on systems where `fork()` is defined.

Warning

Issue the C `fork()` call solely from the [“main” thread](https://docs.python.org/3.14/c-api/threads.html#fork-and-threads) (within the [“main” interpreter](https://docs.python.org/3.14/c-api/subinterpreters.html#sub-interpreter-support)). That restriction applies equally to `PyOS_AfterFork_Child()`.

Added in version 3.7.

See also

[`os.register_at_fork()`](https://docs.python.org/3.14/library/os.html#os.register_at_fork) makes it possible to register your own Python functions for invocation by `PyOS_BeforeFork()`, `PyOS_AfterFork_Parent()` and `PyOS_AfterFork_Child()`.

 void PyOS_AfterFork()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) on platforms with fork().*

A routine that refreshes certain internal state once a process fork has happened; invoke it in the freshly created process whenever the Python interpreter is to keep being used. Should a new executable be loaded into that new process, calling this routine is unnecessary.

Deprecated since version 3.7: This function is superseded by `PyOS_AfterFork_Child()`.

 int PyOS_CheckStack()

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable) on platforms with USE_STACKCHECK since version 3.7.*

Yield true once the interpreter has exhausted its stack space. The check is dependable, yet it is offered solely when `USE_STACKCHECK` is defined (at present on some Windows builds compiled with the Microsoft Visual C++ compiler). `USE_STACKCHECK` is defined for you automatically; never alter the definition within your own code.

 typedef void (*PyOS_sighandler_t)(int)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

 PyOS_sighandler_t PyOS_getsig(int i)

* Part of the [Stable ABI](https://docs.python.org/3.14/c-api/stable.html#stable).*

Yield the signal handler presently bound to signal *i*. It is a slim wrapper over either `sigaction()` or `signal()`. Never call those functions directly!

[Subject index](INDEX.md) · [Following source contract](pyos-setsig-to-py-encodelocale.md)
