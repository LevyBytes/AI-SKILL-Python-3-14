# What's new in Python 3.14 / Changes in the Python API — concurrent.futures, functools, gc, locale, mimetypes, multiprocessing, sys, types, typing

### Changes in the Python API

- Across Unix platforms apart from macOS, *forkserver* now serves as the default [start method](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-start-methods) for [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) and [`ProcessPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ProcessPoolExecutor), replacing *fork*.

See (1) and (2) for details.

Should [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError)s or pickling failures surface from [`multiprocessing`](https://docs.python.org/3.14/library/multiprocessing.html#module-multiprocessing) or [`concurrent.futures`](https://docs.python.org/3.14/library/concurrent.futures.html#module-concurrent.futures), consult the [forkserver restrictions](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-programming-forkserver).

Windows and macOS are unaffected by this change, since ["spawn"](https://docs.python.org/3.14/library/multiprocessing.html#multiprocessing-start-method-spawn) stays the default start method there.

- [`functools.partial`](https://docs.python.org/3.14/library/functools.html#functools.partial) has become a method descriptor. To keep the prior semantics, wrap the object in [`staticmethod()`](https://docs.python.org/3.14/library/functions.html#staticmethod). (Contributed by Serhiy Storchaka and Dominykas Grigonis in [gh-121027](https://github.com/python/cpython/issues/121027).)

- Because the garbage collector is now incremental, [`gc.collect()`](https://docs.python.org/3.14/library/gc.html#gc.collect) behaves a little differently:

  - `gc.collect(1)`: Performs an increment of garbage collection, rather than collecting generation 1.

  - Other calls to `gc.collect()` are unchanged.

- Under certain conditions, [`locale.nl_langinfo()`](https://docs.python.org/3.14/library/locale.html#locale.nl_langinfo) will momentarily switch the `LC_CTYPE` locale. Because that switch is global, other threads feel its effect for the duration. (Contributed by Serhiy Storchaka in [gh-69998](https://github.com/python/cpython/issues/69998).)

- [`types.UnionType`](https://docs.python.org/3.14/library/types.html#types.UnionType) now aliases [`typing.Union`](https://docs.python.org/3.14/library/typing.html#typing.Union), which shifts a few behaviors. Details appear above. (Contributed by Jelle Zijlstra in [gh-105499](https://github.com/python/cpython/issues/105499).)

- Annotations behave differently at runtime in several respects; the specifics are above. Although most annotation-handling code should keep functioning, certain undocumented details may now differ.

- Promoting the [`mimetypes`](https://docs.python.org/3.14/library/mimetypes.html#module-mimetypes) CLI to a public interface brought new exit codes: a failure yields `1` rather than `0`, while bad command-line arguments yield `2` rather than `1`. Diagnostics are now emitted to stderr.

- When supplied on its own as a whole regular-expression pattern, `\B` now succeeds against the empty string, a shift that can alter behaviour.

- On FreeBSD, [`sys.platform`](https://docs.python.org/3.14/library/sys.html#sys.platform) no longer contains the major version number.

[Subject index](INDEX.md) · [Previous source section](porting-to-python-3-14.md) · [Next source section](changes-in-annotations.md) · [Release/subject declaration](summary-release-highlights.md)
