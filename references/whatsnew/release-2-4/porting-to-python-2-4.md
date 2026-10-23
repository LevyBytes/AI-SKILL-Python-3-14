# What’s New in Python 2.4 / Porting to Python 2.4 - datetime, fcntl, tarfile

### Porting to Python 2.4

Gathered here are changes already covered above that could oblige you to adjust your code:

- Oversized left shifts and hexadecimal or octal constants no longer set off a [`FutureWarning`](https://docs.python.org/3.14/library/exceptions.html#FutureWarning) nor cap their result at 32 or 64 bits; what they hand back now is a long integer.

- An `OverflowWarning` is no longer raised by integer operations, and the `OverflowWarning` warning itself is slated to vanish in Python 2.5.

- Called with no arguments, the [`zip()`](https://docs.python.org/3.14/library/functions.html#zip) built-in and `itertools.izip()` hand back an empty list these days rather than throwing a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) exception.

- Comparing the `date` and [`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) instances that the [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime) module supplies is no longer allowed. A pair drawn from different classes always counts as unequal now, and ordering them with (`<`, `>`) throws a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

- Rather than yielding empty lists, `dircache.listdir()` now lets exceptions propagate to the caller.

- Formerly `LexicalHandler.startDTD()` got the public and system IDs handed to it in reversed order. That's been put right, so any application that depended on the old reversed order has to be amended.

- [`fcntl.ioctl()`](https://docs.python.org/3.14/library/fcntl.html#fcntl.ioctl) now issues a warning when the *mutate* argument is left out yet matters.

- As its default, the [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) module now writes tar files in GNU format.

- A failure during a module import no longer leaves behind a half-built module object inside `sys.modules`.

- [`None`](https://docs.python.org/3.14/library/constants.html#None) has become a constant, so any code that rebinds the name `None` to a fresh value now counts as a syntax error.

- For some invalid values the `signals.signal()` function now throws a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) exception, whereas before those errors slipped by quietly. As one case, attaching a handler to the `SIGKILL` signal is no longer permitted.

[Subject index](INDEX.md) · [Previous source section](port-specific-changes.md) · [Release/subject declaration](pep-218-built-in-set-objects.md)
