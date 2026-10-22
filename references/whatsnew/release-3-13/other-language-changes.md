# What's New In Python 3.13 / Other Language Changes — __future__, _thread, os

```pycon
>>> def spam():
...     """
...         This is a docstring with
...           leading whitespace.
...
...         It even has multiple paragraphs!
...     """
...
>>> spam.__doc__
'\nThis is a docstring with\n  leading whitespace.\n\nIt even has multiple paragraphs!\n'

```

(Contributed by Inada Naoki in [gh-81283](https://github.com/python/cpython/issues/81283).)

- [Annotation scopes](https://docs.python.org/3.14/reference/executionmodel.html#annotation-scopes) sitting inside class scopes may now hold lambdas plus comprehensions. A comprehension placed within a class scope is no longer folded into the enclosing parent scope.

```python
class C[T]:
    type Alias = lambda: T

```

(Contributed by Jelle Zijlstra in [gh-109118](https://github.com/python/cpython/issues/109118) and [gh-118160](https://github.com/python/cpython/issues/118160).)

- [Future statements](https://docs.python.org/3.14/reference/simple_stmts.html#future) will no longer fire when you do a relative import of the [`__future__`](https://docs.python.org/3.14/library/__future__.html#module-__future__) module. As a result, any line written as `from .__future__ import ...` becomes an ordinary relative import that turns on none of the special behaviors. (Contributed by Jeremiah Gabriel Pascual in [gh-118216](https://github.com/python/cpython/issues/118216).)

- [`global`](https://docs.python.org/3.14/reference/simple_stmts.html#global) declarations are henceforth allowed inside [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) blocks whenever that same global gets referenced from the [`else`](https://docs.python.org/3.14/reference/compound_stmts.html#else) block. Earlier this incorrectly produced a [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError). (Contributed by Irit Katriel in [gh-111123](https://github.com/python/cpython/issues/111123).)

- Add [`PYTHON_FROZEN_MODULES`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_FROZEN_MODULES), a fresh environment variable controlling whether the import machinery skips frozen modules; it mirrors the [`-X frozen_modules`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) option supplied on the command line. (Contributed by Yilei Yang in [gh-111374](https://github.com/python/cpython/issues/111374).)

- Add [support for the perf profiler](https://docs.python.org/3.14/howto/perf_profiling.html#perf-profiling) operating in the absence of [frame pointers](https://en.wikipedia.org/wiki/Call_stack), enabled by the freshly added environment variable [`PYTHON_PERF_JIT_SUPPORT`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_PERF_JIT_SUPPORT) together with the option [`-X perf_jit`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X). (Contributed by Pablo Galindo in [gh-118518](https://github.com/python/cpython/issues/118518).)

- Where a `.python_history` file lives may now be redirected by setting the freshly added [`PYTHON_HISTORY`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_HISTORY) variable in the environment. (Contributed by Levi Sabah, Zackery Spytz and Hugo van Kemenade in [gh-73965](https://github.com/python/cpython/issues/73965).)

- Classes gain a fresh [`__static_attributes__`](https://docs.python.org/3.14/reference/datamodel.html#type.__static_attributes__) attribute. The compiler fills it with a tuple holding the names of attributes the class assigns via `self.<name>` from anywhere inside its body. (Contributed by Irit Katriel in [gh-115775](https://github.com/python/cpython/issues/115775).)

- A `__firstlineno__` attribute is now produced by the compiler on each class, carrying the line number where the class definition opens. (Contributed by Serhiy Storchaka in [gh-118465](https://github.com/python/cpython/issues/118465).)

- The [`exec()`](https://docs.python.org/3.14/library/functions.html#exec) and [`eval()`](https://docs.python.org/3.14/library/functions.html#eval) builtins henceforth take *globals* and *locals* as keyword arguments. (Contributed by Raphael Gaschignard in [gh-105879](https://github.com/python/cpython/issues/105879))

- A fresh flag, `ast.PyCF_OPTIMIZED_AST`, is now accepted by the [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) builtin; it behaves like `ast.PyCF_ONLY_AST` save that the produced AST gets optimized following whatever the *optimize* argument requests. (Contributed by Irit Katriel in [gh-108113](https://github.com/python/cpython/issues/108113)).

- Add a [`__name__`](https://docs.python.org/3.14/library/functions.html#property.__name__) attribute onto [`property`](https://docs.python.org/3.14/library/functions.html#property) objects. (Contributed by Eugene Toder in [gh-101860](https://github.com/python/cpython/issues/101860).)

- Add [`PythonFinalizationError`](https://docs.python.org/3.14/library/exceptions.html#PythonFinalizationError), a fresh exception subclassing [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError); it flags cases where an operation is disallowed throughout [finalization](https://docs.python.org/3.14/glossary.html#term-interpreter-shutdown). These callables listed below now raise `PythonFinalizationError` rather than `RuntimeError`:

  - [`_thread.start_new_thread()`](https://docs.python.org/3.14/library/_thread.html#thread.start_new_thread)

  - [`os.fork()`](https://docs.python.org/3.14/library/os.html#os.fork)

- [`os.forkpty()`](https://docs.python.org/3.14/library/os.html#os.forkpty)

  - [`subprocess.Popen`](https://docs.python.org/3.14/library/subprocess.html#subprocess.Popen)

(Contributed by Victor Stinner in [gh-114570](https://github.com/python/cpython/issues/114570).)

- Permit the *count* argument of [`str.replace()`](https://docs.python.org/3.14/library/stdtypes.html#str.replace) to be supplied as a keyword. (Contributed by Hugo van Kemenade in [gh-106487](https://github.com/python/cpython/issues/106487).)

- A range of functions now warn whenever a boolean gets handed in where a file descriptor argument is expected, which surfaces certain mistakes sooner. (Contributed by Serhiy Storchaka in [gh-82626](https://github.com/python/cpython/issues/82626).)

- Added `name` and `mode` attributes on the compressed and archived file-like objects exposed by the [`bz2`](https://docs.python.org/3.14/library/bz2.html#module-bz2), [`lzma`](https://docs.python.org/3.14/library/lzma.html#module-lzma), [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile), and [`zipfile`](https://docs.python.org/3.14/library/zipfile.html#module-zipfile) modules. (Contributed by Serhiy Storchaka in [gh-115961](https://github.com/python/cpython/issues/115961).)

### Other Language Changes

- The compiler now removes the common leading whitespace from each line within a docstring. That shrinks the [bytecode cache](https://docs.python.org/3.14/glossary.html#term-bytecode) (for instance `.pyc` files), trimming file size by roughly 5%, as seen for example in `sqlalchemy.orm.session` from SQLAlchemy 2.0. Tools that consume docstrings, such as [`doctest`](https://docs.python.org/3.14/library/doctest.html#module-doctest), are affected by this change.

[Subject index](INDEX.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](new-modules.md) · [Previous source section](support-for-mobile-platforms.md)
