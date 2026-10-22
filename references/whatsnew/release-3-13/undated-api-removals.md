# What's New In Python 3.13 / Pending removal in future versions — argparse, builtins, calendar, codecs, datetime, gettext, importlib

### Pending removal in future versions

These APIs are headed for removal eventually, though no specific date for it has been set yet.

- [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse):

  - Nested argument groups, along with nested mutually exclusive groups, carry a deprecation.

  - Handing the undocumented keyword argument *prefix_chars* to [`add_argument_group()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.add_argument_group) now carries a deprecation.

  - The [`argparse.FileType`](https://docs.python.org/3.14/library/argparse.html#argparse.FileType) type converter carries a deprecation.

- [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins):

  - Generators: the three-argument `throw(type, exc, tb)` and `athrow(type, exc, tb)` form carries a deprecation; prefer the single-argument variants `throw(exc)` and `athrow(exc)`.

  - At present Python will accept a numeric literal sitting directly before a keyword, such as `0in x`, `1or x`, `0if 1else 2`. This permits puzzling, ambiguous expressions like `[0x1for x in y]` (readable as either `[0x1 for x in y]` or `[0x1f or x in y]`). When a numeric literal directly precedes one of the keywords [`and`](https://docs.python.org/3.14/reference/expressions.html#and), [`else`](https://docs.python.org/3.14/reference/compound_stmts.html#else), [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for), [`if`](https://docs.python.org/3.14/reference/compound_stmts.html#if), [`in`](https://docs.python.org/3.14/reference/expressions.html#in), [`is`](https://docs.python.org/3.14/reference/expressions.html#is) and [`or`](https://docs.python.org/3.14/reference/expressions.html#or), a syntax warning fires. A later release will promote this to a syntax error. ([gh-87999](https://github.com/python/cpython/issues/87999))

  - `__index__()` and `__int__()` returning a non-int type remains supported for now: going forward, these methods will have to yield an instance of a strict subclass of [`int`](https://docs.python.org/3.14/library/functions.html#int).

  - `__float__()` returning a strict subclass of [`float`](https://docs.python.org/3.14/library/functions.html#float) remains supported for now: going forward, these methods will have to yield an instance of `float`.

  - `__complex__()` returning a strict subclass of [`complex`](https://docs.python.org/3.14/library/functions.html#complex) remains supported for now: going forward, these methods will have to yield an instance of `complex`.

  - Handing a complex number as the *real* or *imag* argument to the [`complex()`](https://docs.python.org/3.14/library/functions.html#complex) constructor now carries a deprecation; supply it solely as a lone positional argument. (Contributed by Serhiy Storchaka in [gh-109218](https://github.com/python/cpython/issues/109218).)

- [`calendar`](https://docs.python.org/3.14/library/calendar.html#module-calendar): the `calendar.January` and `calendar.February` constants carry a deprecation and give way to [`calendar.JANUARY`](https://docs.python.org/3.14/library/calendar.html#calendar.JANUARY) and [`calendar.FEBRUARY`](https://docs.python.org/3.14/library/calendar.html#calendar.FEBRUARY). (Contributed by Prince Roshan in [gh-103636](https://github.com/python/cpython/issues/103636).)

- [`codecs`](https://docs.python.org/3.14/library/codecs.html#module-codecs): prefer [`open()`](https://docs.python.org/3.14/library/functions.html#open) over [`codecs.open()`](https://docs.python.org/3.14/library/codecs.html#codecs.open). ([gh-133038](https://github.com/python/cpython/issues/133038))

- [`codeobject.co_lnotab`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_lnotab): rely on the [`codeobject.co_lines()`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_lines) method in its place.

- [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime):

  - [`utcnow()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.utcnow): switch to `datetime.datetime.now(tz=datetime.UTC)`.

  - [`utcfromtimestamp()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.utcfromtimestamp): switch to `datetime.datetime.fromtimestamp(timestamp, tz=datetime.UTC)`.

- [`gettext`](https://docs.python.org/3.14/library/gettext.html#module-gettext): the plural value is required to be an integer.

- [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib):

  - [`cache_from_source()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.cache_from_source) carries a deprecation on its *debug_override* parameter: rely on the *optimization* parameter instead.

[Subject index](INDEX.md) · [Previous source section](pending-removal-in-python-3-19.md) · [Next source section](pending-removal-in-future-versions-importlib-metadata.md) · [Release/subject declaration](summary-release-highlights.md)
