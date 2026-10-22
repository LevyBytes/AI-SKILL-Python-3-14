# Python 3.12.0 alpha 4 / library / os

[gh-89727](https://github.com/python/cpython/issues/89727): Streamline and speed up [`os.walk()`](https://docs.python.org/3.14/library/os.html#os.walk) with [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) checks against the top of the stack.

[gh-100228](https://github.com/python/cpython/issues/100228): Calling [`os.fork()`](https://docs.python.org/3.14/library/os.html#os.fork) or [`os.forkpty()`](https://docs.python.org/3.14/library/os.html#os.forkpty) from a multi-threaded process may now trigger a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). Forking while threads exist is unsafe and may lead to deadlocks, crashes, and subtle bugs. The absence of a warning is no guarantee the fork was safe, because Python cannot always see every thread.

[gh-89727](https://github.com/python/cpython/issues/89727): Resolve an issue with [`os.walk()`](https://docs.python.org/3.14/library/os.html#os.walk) in which deeply nested directory trees triggered a [`RecursionError`](https://docs.python.org/3.14/library/exceptions.html#RecursionError); the fix reworks `os.walk()` from a recursive form into an iterative one.

[bpo-40447](https://bugs.python.org/issue?@action=redirect&bpo=40447): Allow [`os.PathLike`](https://docs.python.org/3.14/library/os.html#os.PathLike) values (for example [`pathlib.Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path)) in the `stripdir` arguments of [`compileall.compile_file()`](https://docs.python.org/3.14/library/compileall.html#compileall.compile_file) and [`compileall.compile_dir()`](https://docs.python.org/3.14/library/compileall.html#compileall.compile_dir).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
