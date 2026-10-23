# What's new in Python 3.14 / Command line and environment - textwrap

### Command line and environment

- Modules that have already been loaded (‘cached’) can now be tracked by the import time flag, thanks to the new [`-X importtime=2`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X). On importing such a module, the string `cached` takes the place of the `self` and `cumulative` times.

Anything beyond `2` for `-X importtime` is now held back for later use.

(Contributed by Noah Kim and Adam Turner in [gh-118655](https://github.com/python/cpython/issues/118655).)

- Before running, the command-line option [`-c`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-c) now dedents its code argument automatically. This auto-dedentation behaves the same way as [`textwrap.dedent()`](https://docs.python.org/3.14/library/textwrap.html#textwrap.dedent). (Contributed by Jon Crall and Steven Sun in [gh-103998](https://github.com/python/cpython/issues/103998).)

- As a reserved flag for [Jython](https://www.jython.org/), `-J` is gone, and it now carries no special meaning. (Contributed by Adam Turner in [gh-133336](https://github.com/python/cpython/issues/133336).)

[Subject index](INDEX.md) · [Previous source section](built-ins.md) · [Next source section](pep-758-allow-except-and-except-expressions-without-brackets.md) · [Release/subject declaration](summary-release-highlights.md)
