# Language and standard library pending removal in future versions: argparse; builtins; calendar; codecs; codeobject.co_lnotab; datetime; gettext; importlib

### Pending removal in future versions

The APIs below are headed for removal eventually, though no removal date has yet been fixed.

- [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse):

  - Nesting argument groups, as well as nesting mutually exclusive groups, is deprecated.

  - Supplying the undocumented keyword argument *prefix_chars* to [`add_argument_group()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.add_argument_group) is now deprecated.

  - The [`argparse.FileType`](https://docs.python.org/3.14/library/argparse.html#argparse.FileType) type converter is deprecated.

- [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins):

  - Generators: the `throw(type, exc, tb)` and `athrow(type, exc, tb)` signature is deprecated; use the single-argument form `throw(exc)` and `athrow(exc)` instead.

  - At present Python permits numeric literals directly followed by keywords, such as `0in x`, `1or x`, `0if 1else 2`. This admits confusing, ambiguous expressions like `[0x1for x in y]` (readable either as `[0x1 for x in y]` or `[0x1f or x in y]`). When a numeric literal sits immediately before one of the keywords [`and`](https://docs.python.org/3.14/reference/expressions.html#and), [`else`](https://docs.python.org/3.14/reference/compound_stmts.html#else), [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for), [`if`](https://docs.python.org/3.14/reference/compound_stmts.html#if), [`in`](https://docs.python.org/3.14/reference/expressions.html#in), [`is`](https://docs.python.org/3.14/reference/expressions.html#is), or [`or`](https://docs.python.org/3.14/reference/expressions.html#or), a syntax warning fires. A later release will turn this into a syntax error. ([gh-87999](https://github.com/python/cpython/issues/87999))

  - Support for `__index__()` and `__int__()` methods returning a non-int type: these methods will be obliged to return an instance of a strict subclass of [`int`](https://docs.python.org/3.14/library/functions.html#int).

  - Support for an `__float__()` method returning a strict subclass of [`float`](https://docs.python.org/3.14/library/functions.html#float): such methods will be obliged to return an instance of `float`.

  - Support for a `__complex__()` method returning a strict subclass of [`complex`](https://docs.python.org/3.14/library/functions.html#complex): such methods will be obliged to return an instance of `complex`.

  - Supplying a complex number as the *real* or *imag* argument to the [`complex()`](https://docs.python.org/3.14/library/functions.html#complex) constructor is now deprecated; pass it only as a lone positional argument. (Contributed by Serhiy Storchaka in [gh-109218](https://github.com/python/cpython/issues/109218).)

- [`calendar`](https://docs.python.org/3.14/library/calendar.html#module-calendar): the `calendar.January` and `calendar.February` constants are deprecated, superseded by [`calendar.JANUARY`](https://docs.python.org/3.14/library/calendar.html#calendar.JANUARY) and [`calendar.FEBRUARY`](https://docs.python.org/3.14/library/calendar.html#calendar.FEBRUARY). (Contributed by Prince Roshan in [gh-103636](https://github.com/python/cpython/issues/103636).)

- [`codecs`](https://docs.python.org/3.14/library/codecs.html#module-codecs): reach for [`open()`](https://docs.python.org/3.14/library/functions.html#open) rather than [`codecs.open()`](https://docs.python.org/3.14/library/codecs.html#codecs.open). ([gh-133038](https://github.com/python/cpython/issues/133038))

- [`codeobject.co_lnotab`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_lnotab): rely on the [`codeobject.co_lines()`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_lines) method instead.

- [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime):

  - [`utcnow()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.utcnow): switch to `datetime.datetime.now(tz=datetime.UTC)`.

  - [`utcfromtimestamp()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.utcfromtimestamp): switch to `datetime.datetime.fromtimestamp(timestamp, tz=datetime.UTC)`.

- [`gettext`](https://docs.python.org/3.14/library/gettext.html#module-gettext): the plural value has to be an integer.

- [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib):

  - [`cache_from_source()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.cache_from_source)'s *debug_override* parameter is deprecated; rely on the *optimization* parameter instead.

[Subject index](INDEX.md) · [Previous source section](../python-3-19/ctypes.md) · [Next source section](importlib-metadata-through-shutil.md)
