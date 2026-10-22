# exceptions: `OSError`, `PythonFinalizationError`

name

The name belonging to the variable whose access was attempted.

Changed in version 3.10: Added the `name` attribute.

 *exception *NotImplementedError

This exception descends from `RuntimeError`. Within user defined base classes, abstract methods ought to raise it whenever they need derived classes to override the method, or while a class remains under development as a way of signaling that the actual implementation has yet to be supplied.

Note

It is not meant to convey that an operator or method is not supposed to be supported in any form — for that case, either leave the operator / method undefined, or, when dealing with a subclass, assign it [`None`](https://docs.python.org/3.14/library/constants.html#None).

Caution

`NotImplementedError` and `NotImplemented` cannot stand in for one another. Confine this exception to the usage spelled out above; consult [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented) for the proper way to use the built-in constant.

 *exception *OSError([*arg*])

 *exception *OSError(*errno*, *strerror*[, *filename*[, *winerror*[, *filename2*]]])

This exception arises whenever a system function reports a system-related error, encompassing I/O failures such as "file not found" or "disk full" (but not illegal argument types or other unrelated errors).

The constructor's second form populates the matching attributes detailed below. Where they are not given, the attributes fall back to [`None`](https://docs.python.org/3.14/library/constants.html#None). To preserve backwards compatibility, passing three arguments leaves the `args` attribute holding only a 2-tuple made of the first two constructor arguments.

The constructor frequently gives back a subclass of `OSError`, as laid out under OS exceptions below. Which subclass it is hinges on the final `errno` value. Such behaviour shows up solely when `OSError` is constructed directly or by way of an alias, and subclasses do not inherit it.

 errno

A numeric error code drawn from the C variable `errno`.

 winerror

On Windows, this hands you the native Windows error code. The `errno` attribute then becomes a rough rendering, expressed in POSIX terms, of that native error code.

On Windows, when the *winerror* constructor argument is an integer, the `errno` attribute is worked out from the Windows error code, and the *errno* argument is disregarded. On platforms other than Windows, the *winerror* argument is disregarded, and the `winerror` attribute is absent.

 strerror

The matching error message, as supplied by the operating system. Its formatting comes from the C functions `perror()` on POSIX and `FormatMessage()` on Windows.

 filename

 filename2

When exceptions concern a file system path (for example [`open()`](https://docs.python.org/3.14/library/functions.html#open) or [`os.unlink()`](https://docs.python.org/3.14/library/os.html#os.unlink)), `filename` holds the file name that was handed to the function. When functions concern a pair of file system paths (for example [`os.rename()`](https://docs.python.org/3.14/library/os.html#os.rename)), `filename2` matches the second file name handed to the function.

Changed in version 3.3: `EnvironmentError`, `IOError`, `WindowsError`, [`socket.error`](https://docs.python.org/3.14/library/socket.html#socket.error), [`select.error`](https://docs.python.org/3.14/library/select.html#select.error) along with `mmap.error` were folded together into `OSError`, with the constructor permitted to hand back a subclass.

Changed in version 3.4: The `filename` attribute now holds the file name in its original form as handed to the function, rather than a version encoded to (or decoded from) the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler). The *filename2* constructor argument and attribute were introduced as well.

 *exception *OverflowError

Raised whenever an arithmetic operation produces a result too large to represent. Integers cannot trigger this (they would sooner raise `MemoryError` than admit defeat). That said, for historical reasons OverflowError does occasionally get raised for integers that lie beyond some required range. Owing to the absence of any standard for floating-point exception handling in C, the bulk of floating-point operations go unchecked.

 *exception *PythonFinalizationError

This exception descends from `RuntimeError`. It arises whenever an operation is blocked while the interpreter is shutting down, otherwise referred to as [Python finalization](https://docs.python.org/3.14/glossary.html#term-interpreter-shutdown).

Some examples of operations that can be blocked by a `PythonFinalizationError` over the course of the Python finalization:

- Creating a new Python thread.

- [`Joining`](https://docs.python.org/3.14/library/threading.html#threading.Thread.join) a running daemon thread.

- [`os.fork()`](https://docs.python.org/3.14/library/os.html#os.fork).

See also the [`sys.is_finalizing()`](https://docs.python.org/3.14/library/sys.html#sys.is_finalizing) function.

Added in version 3.13: Previously, a plain `RuntimeError` was raised.

Changed in version 3.14: [`threading.Thread.join()`](https://docs.python.org/3.14/library/threading.html#threading.Thread.join) can now raise this exception.

[Subject index](INDEX.md) · [Previous](assertionerror-to-nameerror.md) · [Continue](recursionerror-to-taberror.md) · [Owning module, declaration or section: Concrete exceptions](assertionerror-to-nameerror.md)
