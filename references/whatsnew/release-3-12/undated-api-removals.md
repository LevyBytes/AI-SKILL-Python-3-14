# What’s New In Python 3.12 / Pending removal in future versions — argparse, builtins, calendar, codecs, datetime, gettext, importlib

### Pending removal in future versions

These APIs are slated for eventual deletion, though no removal date has been fixed yet.

- [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse):

  - Nesting one argument group inside another, as well as nesting mutually exclusive groups, is deprecated.

  - Handing the undocumented keyword argument *prefix_chars* to [`add_argument_group()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.add_argument_group) now counts as deprecated.

  - The [`argparse.FileType`](https://docs.python.org/3.14/library/argparse.html#argparse.FileType) type converter is deprecated.

- [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins):

  - Generators: the `throw(type, exc, tb)` and `athrow(type, exc, tb)` signature is deprecated; prefer the one-argument form, `throw(exc)` and `athrow(exc)`.

  - Right now Python permits a numeric literal that runs straight into a keyword, such as `0in x`, `1or x`, `0if 1else 2`. This permits puzzling, ambiguous code like `[0x1for x in y]` (readable either as `[0x1 for x in y]` or as `[0x1f or x in y]`). A syntax warning fires whenever a numeric literal butts directly against one of the keywords [`and`](https://docs.python.org/3.14/reference/expressions.html#and), [`else`](https://docs.python.org/3.14/reference/compound_stmts.html#else), [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for), [`if`](https://docs.python.org/3.14/reference/compound_stmts.html#if), [`in`](https://docs.python.org/3.14/reference/expressions.html#in), [`is`](https://docs.python.org/3.14/reference/expressions.html#is) and [`or`](https://docs.python.org/3.14/reference/expressions.html#or). A later release will promote this to a syntax error. ([gh-87999](https://github.com/python/cpython/issues/87999))

  - Allowing `__index__()` and `__int__()` to hand back a non-int type: going forward these methods must yield an instance belonging to a strict subclass of [`int`](https://docs.python.org/3.14/library/functions.html#int).

  - Allowing `__float__()` to hand back a strict subclass of [`float`](https://docs.python.org/3.14/library/functions.html#float): such methods will be obliged to yield an instance of `float`.

  - Allowing `__complex__()` to hand back a strict subclass of [`complex`](https://docs.python.org/3.14/library/functions.html#complex): such methods will be obliged to yield an instance of `complex`.

  - Supplying a complex number for the *real* or *imag* argument of the [`complex()`](https://docs.python.org/3.14/library/functions.html#complex) constructor is now deprecated; supply it only as a lone positional argument. (Contributed by Serhiy Storchaka in [gh-109218](https://github.com/python/cpython/issues/109218).)

- [`calendar`](https://docs.python.org/3.14/library/calendar.html#module-calendar): the `calendar.January` and `calendar.February` constants are deprecated, superseded by [`calendar.JANUARY`](https://docs.python.org/3.14/library/calendar.html#calendar.JANUARY) and [`calendar.FEBRUARY`](https://docs.python.org/3.14/library/calendar.html#calendar.FEBRUARY). (Contributed by Prince Roshan in [gh-103636](https://github.com/python/cpython/issues/103636).)

- [`codecs`](https://docs.python.org/3.14/library/codecs.html#module-codecs): reach for [`open()`](https://docs.python.org/3.14/library/functions.html#open) rather than [`codecs.open()`](https://docs.python.org/3.14/library/codecs.html#codecs.open). ([gh-133038](https://github.com/python/cpython/issues/133038))

- [`codeobject.co_lnotab`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_lnotab): rely on the [`codeobject.co_lines()`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_lines) method in its place.

- [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime):

  - [`utcnow()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.utcnow): switch to `datetime.datetime.now(tz=datetime.UTC)`.

  - [`utcfromtimestamp()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.utcfromtimestamp): switch to `datetime.datetime.fromtimestamp(timestamp, tz=datetime.UTC)`.

- [`gettext`](https://docs.python.org/3.14/library/gettext.html#module-gettext): a Plural value is required to be an integer.

- [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib):

  - The [`cache_from_source()`](https://docs.python.org/3.14/library/importlib.html#importlib.util.cache_from_source) *debug_override* parameter is deprecated: rely on the *optimization* parameter instead.

[Subject index](INDEX.md) · [Previous source section](pending-removal-in-python-3-17.md) · [Next source section](pending-removal-in-future-versions-importlib-metadata.md) · [Release/subject declaration](summary-release-highlights.md)
