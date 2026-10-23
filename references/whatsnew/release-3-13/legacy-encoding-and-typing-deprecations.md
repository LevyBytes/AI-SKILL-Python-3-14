# What's New In Python 3.13 / New Deprecations - sys, tarfile, traceback, typing, wave

[`sys`](https://docs.python.org/3.14/library/sys.html#module-sys):

  - The [`_enablelegacywindowsfsencoding()`](https://docs.python.org/3.14/library/sys.html#sys._enablelegacywindowsfsencoding) function is now deprecated and will be dropped in Python 3.16. Set the [`PYTHONLEGACYWINDOWSFSENCODING`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONLEGACYWINDOWSFSENCODING) environment variable in its place. (Contributed by Inada Naoki in [gh-73427](https://github.com/python/cpython/issues/73427).)

- [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile):

  - The undocumented, never-used `TarFile.tarfile` attribute is now deprecated and is set to disappear in Python 3.16. (Contributed in [gh-115256](https://github.com/python/cpython/issues/115256).)

- [`traceback`](https://docs.python.org/3.14/library/traceback.html#module-traceback):

  - The [`TracebackException.exc_type`](https://docs.python.org/3.14/library/traceback.html#traceback.TracebackException.exc_type) attribute is now deprecated. Reach for [`TracebackException.exc_type_str`](https://docs.python.org/3.14/library/traceback.html#traceback.TracebackException.exc_type_str) instead. (Contributed by Irit Katriel in [gh-112332](https://github.com/python/cpython/issues/112332).)

- [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing):

  - The undocumented keyword-argument form for building [`NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple) classes (such as `Point = NamedTuple("Point", x=int, y=int)`) is now deprecated and goes away in Python 3.15. Pick either the class-based form or the functional form. (Contributed by Alex Waygood in [gh-105566](https://github.com/python/cpython/issues/105566).)

  - Leaving out the *fields* parameter while building a [`NamedTuple`](https://docs.python.org/3.14/library/typing.html#typing.NamedTuple) or [`typing.TypedDict`](https://docs.python.org/3.14/library/typing.html#typing.TypedDict) class is now deprecated, as is handing `None` to that *fields* parameter on either type. A real sequence will be mandatory for *fields* starting with Python 3.15. For a NamedTuple class holding no fields, write `class NT(NamedTuple): pass` or `NT = NamedTuple("NT", ())`. For a TypedDict class holding no fields, write `class TD(TypedDict): pass` or `TD = TypedDict("TD", {})`. (Contributed by Alex Waygood in [gh-105566](https://github.com/python/cpython/issues/105566) and [gh-105570](https://github.com/python/cpython/issues/105570).)

  - The [`typing.no_type_check_decorator()`](https://docs.python.org/3.14/library/typing.html#typing.no_type_check_decorator) decorator function is now deprecated and exits in Python 3.15. Despite eight years living in the [`typing`](https://docs.python.org/3.14/library/typing.html#module-typing) module, no significant type checker has ever adopted it. (Contributed by Alex Waygood in [gh-106309](https://github.com/python/cpython/issues/106309).)

  - [`typing.AnyStr`](https://docs.python.org/3.14/library/typing.html#typing.AnyStr) is now deprecated. Come Python 3.16 it leaves `typing.__all__`, and importing or touching it then raises a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) while running. Full removal lands in Python 3.18. Adopt the new [type parameter syntax](https://docs.python.org/3.14/reference/compound_stmts.html#type-params) going forward. (Contributed by Michael The in [gh-107116](https://github.com/python/cpython/issues/107116).)

- [`wave`](https://docs.python.org/3.14/library/wave.html#module-wave):

  - The [`getmark()`](https://docs.python.org/3.14/library/wave.html#wave.Wave_read.getmark), `setmark()`, and [`getmarkers()`](https://docs.python.org/3.14/library/wave.html#wave.Wave_read.getmarkers) methods belonging to the [`Wave_read`](https://docs.python.org/3.14/library/wave.html#wave.Wave_read) and [`Wave_write`](https://docs.python.org/3.14/library/wave.html#wave.Wave_write) classes are now deprecated, with removal targeted for Python 3.15. (Contributed by Victor Stinner in [gh-105096](https://github.com/python/cpython/issues/105096).)

[Subject index](INDEX.md) · [Previous source section](plural-selection-and-library-deprecations.md) · [Next source section](pending-removal-in-python-3-14.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](new-deprecations.md) · [Preceding release/subject continuation](new-deprecations.md)
