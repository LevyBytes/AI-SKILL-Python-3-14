# What’s New In Python 3.5 / Summary – Release highlights - collections, sys, typing, zipapp

### What’s New In Python 3.5

Editors:

Elvis Pranskevichus <[elvis@magic.io](mailto:elvis%40magic.io)>, Yury Selivanov <[yury@magic.io](mailto:yury%40magic.io)>

This document describes what landed in Python 3.5 relative to the 3.4 line. The 3.5 release shipped on September 13, 2015. Consult the [changelog](https://docs.python.org/3.5/whatsnew/changelog.html) for an exhaustive enumeration of every change.

See also

[**PEP 478**](https://peps.python.org/pep-0478/) - Python 3.5 Release Schedule

### Summary – Release highlights

New syntax features:

- PEP 492, coroutines with async and await syntax.

- PEP 465, a new matrix multiplication operator: `a @ b`.

- PEP 448, additional unpacking generalizations.

New library modules:

- [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing): PEP 484 – Type Hints.

- [`zipapp`](https://docs.python.org/3.14/library/zipapp.html#module-zipapp): PEP 441 Improving Python ZIP Application Support.

New built-in features:

- `bytes % args`, `bytearray % args`: PEP 461 – Adding `%` formatting to bytes and bytearray.

- Fresh [`bytes.hex()`](https://docs.python.org/3.14/library/stdtypes.html#bytes.hex), [`bytearray.hex()`](https://docs.python.org/3.14/library/stdtypes.html#bytearray.hex) and [`memoryview.hex()`](https://docs.python.org/3.14/library/stdtypes.html#memoryview.hex) methods land here. (Contributed by Arnon Yaari in [bpo-9951](https://bugs.python.org/issue?@action=redirect&bpo=9951).)

- [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) gains tuple indexing as well, multi-dimensional cases included. (Contributed by Antoine Pitrou in [bpo-23632](https://bugs.python.org/issue?@action=redirect&bpo=23632).)

- A fresh `gi_yieldfrom` attribute on generators surfaces whatever object a `yield from` expression is currently iterating over. (Contributed by Benno Leslie and Yury Selivanov in [bpo-24450](https://bugs.python.org/issue?@action=redirect&bpo=24450).)

- Hitting the ceiling on recursion depth now triggers a fresh [`RecursionError`](https://docs.python.org/3.14/library/exceptions.html#RecursionError) exception. (Contributed by Georg Brandl in [bpo-19235](https://bugs.python.org/issue?@action=redirect&bpo=19235).)

CPython implementation improvements:

- Should the `LC_TYPE` locale be the POSIX one (the `C` locale), [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin) plus [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout) now switch to the `surrogateescape` error handler rather than the `strict` error handler. (Contributed by Victor Stinner in [bpo-19977](https://bugs.python.org/issue?@action=redirect&bpo=19977).)

- The `.pyo` files have been dropped, giving way to a more adaptable scheme that bakes the optimization level right into the `.pyc` name. (See PEP 488 overview.)

- A multi-phase process, echoing the way Python modules get loaded, now drives the setup of Builtin and extension modules. (See PEP 489 overview.)

Significant improvements in the standard library:

- A C implementation now backs [`collections.OrderedDict`](https://docs.python.org/3.14/library/collections.html#collections.OrderedDict), delivering a 4 to 100 times speedup.

- Memory BIO support arrived in the [`ssl`](https://docs.python.org/3.14/library/ssl.html#module-ssl) module, separating handling of the SSL protocol from network IO.

- A superior and markedly quicker route for walking directories arrives via the new [`os.scandir()`](https://docs.python.org/3.14/library/os.html#os.scandir) function.

- A largely C-based rewrite of [`functools.lru_cache()`](https://docs.python.org/3.14/library/functools.html#functools.lru_cache) delivers far stronger performance.

- A tidy means of launching subprocesses arrives through the new [`subprocess.run()`](https://docs.python.org/3.14/library/subprocess.html#subprocess.run) function.

- Considerable upgrades to the [`traceback`](https://docs.python.org/3.14/library/traceback.html#module-traceback) module boost both its speed and how convenient it is for developers.

Security improvements:

- Across the standard library SSLv3 now sits disabled by default. Turning it back on remains possible by hand-constructing a [`ssl.SSLContext`](https://docs.python.org/3.14/library/ssl.html#ssl.SSLContext). (Consult [bpo-22638](https://bugs.python.org/issue?@action=redirect&bpo=22638) for the full story; the fix also landed in CPython 3.4 along with 2.7.)

- Parsing of HTTP cookies has tightened up so as to guard against possible injection attacks. (Contributed by Antoine Pitrou in [bpo-22796](https://bugs.python.org/issue?@action=redirect&bpo=22796).)

Windows improvements:

- On Windows a brand-new installer now stands in for the former MSI. See [Using Python on Windows](https://docs.python.org/3.14/using/windows.html#using-on-windows) for more information.

- Builds on Windows now rely on Microsoft Visual C++ 14.0, and extension modules ought to match that.

Keep reading for the thorough rundown of changes that affect users, covering numerous additional smaller refinements, CPython speedups, deprecations, and possible porting concerns.

[Subject index](INDEX.md) · [Next source section](pep492-async-await-coroutine-examples.md)
