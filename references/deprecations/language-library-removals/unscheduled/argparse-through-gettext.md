# Language and standard library pending removal in future versions: argparse; builtins; calendar; codecs; codeobject.co_lnotab; datetime; gettext

# Pending Removal In Future

### Pending removal in future versions

The APIs listed below are slated to go away eventually, even though no removal date has yet been fixed for any of them.

- [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse):

  - Putting argument groups inside one another, and likewise nesting mutually exclusive groups, is now deprecated.

  - Handing the undocumented keyword argument *prefix_chars* to [`add_argument_group()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.add_argument_group) has become deprecated.

  - The [`argparse.FileType`](https://docs.python.org/3.14/library/argparse.html#argparse.FileType) type converter is deprecated.

- [`builtins`](https://docs.python.org/3.14/library/builtins.html#module-builtins):

  - Generators: the `throw(type, exc, tb)` and `athrow(type, exc, tb)` signature is deprecated; reach instead for the single-argument forms `throw(exc)` and `athrow(exc)`.

  - At present Python tolerates a numeric literal sitting right up against a keyword, as in `0in x`, `1or x`, `0if 1else 2`. This opens the door to muddled, ambiguous expressions such as `[0x1for x in y]` (readable either as `[0x1 for x in y]` or as `[0x1f or x in y]`). Whenever a numeric literal butts directly against one of the keywords [`and`](https://docs.python.org/3.14/reference/expressions.html#and), [`else`](https://docs.python.org/3.14/reference/compound_stmts.html#else), [`for`](https://docs.python.org/3.14/reference/compound_stmts.html#for), [`if`](https://docs.python.org/3.14/reference/compound_stmts.html#if), [`in`](https://docs.python.org/3.14/reference/expressions.html#in), [`is`](https://docs.python.org/3.14/reference/expressions.html#is) or [`or`](https://docs.python.org/3.14/reference/expressions.html#or), a syntax warning now fires. A later release will turn this into a syntax error outright. ([gh-87999](https://github.com/python/cpython/issues/87999))

  - Permitting the `__index__()` and `__int__()` method to hand back a non-int type: going forward, these methods will have to return an instance of a strict subclass of [`int`](https://docs.python.org/3.14/library/functions.html#int).

  - Permitting the `__float__()` method to hand back a strict subclass of [`float`](https://docs.python.org/3.14/library/functions.html#float): going forward, these methods will have to return an instance of `float`.

  - Permitting the `__complex__()` method to hand back a strict subclass of [`complex`](https://docs.python.org/3.14/library/functions.html#complex): going forward, these methods will have to return an instance of `complex`.

  - Supplying a complex number as either the *real* or the *imag* argument to the [`complex()`](https://docs.python.org/3.14/library/functions.html#complex) constructor is now deprecated; it may only be given as a lone positional argument. (Contributed by Serhiy Storchaka in [gh-109218](https://github.com/python/cpython/issues/109218).)

- [`calendar`](https://docs.python.org/3.14/library/calendar.html#module-calendar): the `calendar.January` and `calendar.February` constants are deprecated, their successors being [`calendar.JANUARY`](https://docs.python.org/3.14/library/calendar.html#calendar.JANUARY) and [`calendar.FEBRUARY`](https://docs.python.org/3.14/library/calendar.html#calendar.FEBRUARY). (Contributed by Prince Roshan in [gh-103636](https://github.com/python/cpython/issues/103636).)

- [`codecs`](https://docs.python.org/3.14/library/codecs.html#module-codecs): reach for [`open()`](https://docs.python.org/3.14/library/functions.html#open) rather than [`codecs.open()`](https://docs.python.org/3.14/library/codecs.html#codecs.open). ([gh-133038](https://github.com/python/cpython/issues/133038))

- [`codeobject.co_lnotab`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_lnotab): lean on the [`codeobject.co_lines()`](https://docs.python.org/3.14/reference/datamodel.html#codeobject.co_lines) method in its place.

- [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime):

  - [`utcnow()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.utcnow): use `datetime.datetime.now(tz=datetime.UTC)`.

  - [`utcfromtimestamp()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.utcfromtimestamp): use `datetime.datetime.fromtimestamp(timestamp, tz=datetime.UTC)`.

- [`gettext`](https://docs.python.org/3.14/library/gettext.html#module-gettext): the plural value is required to be an integer.

[Subject index](INDEX.md) · [Next source section](importlib-through-shutil.md)
