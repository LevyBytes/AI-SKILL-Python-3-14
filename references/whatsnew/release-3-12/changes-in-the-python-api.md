# What’s New In Python 3.12 / Changes in the Python API - argparse, asyncio, functools, locale, os, shlex, shutil, sys, syslog, tarfile, tokenize

### Changes in the Python API

- Numerical group references along with group names inside regular expressions now obey tighter rules. A numerical reference is only honoured when it is a run of ASCII digits. Within bytes patterns and replacement strings, a group name is now restricted to ASCII letters, digits, and the underscore. (Contributed by Serhiy Storchaka in [gh-91760](https://github.com/python/cpython/issues/91760).)

- Drop the `randrange()` behaviour that had been deprecated as of Python 3.10. Previously, `randrange(10.0)` was converted to `randrange(10)` without loss. It now raises a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) instead. On top of that, calls with non-integer values like `randrange(10.5)` or `randrange('10')` now raise `TypeError` where they once raised [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). The change additionally avoids bugs in which `randrange(1e25)` would quietly draw from a wider span than `randrange(10**25)`. (Originally suggested by Serhiy Storchaka [gh-86388](https://github.com/python/cpython/issues/86388).)

- [`argparse.ArgumentParser`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser) switched the encoding plus error handler used when it reads arguments out of a file (for instance via the `fromfile_prefix_chars` option), moving off the default text encoding (such as [`locale.getpreferredencoding(False)`](https://docs.python.org/3.14/library/locale.html#locale.getpreferredencoding)) and onto the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler). On Windows, encode argument files as UTF-8 rather than the ANSI Codepage.

- Drop the `asyncore`-backed `smtpd` module, which had been deprecated across Python 3.4.7 and 3.5.4. As a substitute, consider the [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio)-backed [aiosmtpd](https://pypi.org/project/aiosmtpd/) PyPI module.

- [`shlex.split()`](https://docs.python.org/3.14/library/shlex.html#shlex.split): Handing `None` as the *s* argument now triggers an exception instead of pulling from [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin). That behaviour had been deprecated in Python 3.9. (Contributed by Victor Stinner in [gh-94352](https://github.com/python/cpython/issues/94352).)

- The [`os`](https://docs.python.org/3.14/library/os.html#module-os) module will no longer take bytes-like paths such as the [`bytearray`](https://docs.python.org/3.14/library/stdtypes.html#bytearray) and [`memoryview`](https://docs.python.org/3.14/library/stdtypes.html#memoryview) types; for bytes strings, only the precise [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) type is taken. (Contributed by Victor Stinner in [gh-98393](https://github.com/python/cpython/issues/98393).)

- [`syslog.openlog()`](https://docs.python.org/3.14/library/syslog.html#syslog.openlog) plus [`syslog.closelog()`](https://docs.python.org/3.14/library/syslog.html#syslog.closelog) now error out when invoked inside subinterpreters. You can still call [`syslog.syslog()`](https://docs.python.org/3.14/library/syslog.html#syslog.syslog) from subinterpreters, though only once `syslog.openlog()` has been run within the main interpreter. None of these fresh restrictions touch the main interpreter, so the pool of affected users should be tiny. The change aids interpreter isolation. Beyond that, [`syslog`](https://docs.python.org/3.14/library/syslog.html#module-syslog) wraps process-global resources, and such resources are best handled from the main interpreter. (Contributed by Donghee Na in [gh-99127](https://github.com/python/cpython/issues/99127).)

- The undocumented locking behaviour of [`cached_property()`](https://docs.python.org/3.14/library/functools.html#functools.cached_property) is gone, since it took a lock spanning every instance of the class, which produced heavy lock contention. As a result, for any single instance a cached property getter could now execute more than once should two threads race. With most straightforward cached properties (for example ones that are idempotent and merely derive a value from the instance's other attributes) this will be fine. Where synchronization is required, add locking inside the cached property getter function or around the points of multi-threaded access.

- [`sys._current_exceptions()`](https://docs.python.org/3.14/library/sys.html#sys._current_exceptions) now hands back a mapping that goes from thread-id to an exception instance, in place of a `(typ, exc, tb)` tuple. (Contributed by Irit Katriel in [gh-103176](https://github.com/python/cpython/issues/103176).)

- While unpacking tar files through [`tarfile`](https://docs.python.org/3.14/library/tarfile.html#module-tarfile) or [`shutil.unpack_archive()`](https://docs.python.org/3.14/library/shutil.html#shutil.unpack_archive), supply the *filter* argument to restrict features that could prove surprising or dangerous. Consult [Extraction filters](https://docs.python.org/3.14/library/tarfile.html#tarfile-extraction-filter) for the specifics.

- What the [`tokenize.tokenize()`](https://docs.python.org/3.14/library/tokenize.html#tokenize.tokenize) plus [`tokenize.generate_tokens()`](https://docs.python.org/3.14/library/tokenize.html#tokenize.generate_tokens) functions output has now shifted owing to the work brought in by [**PEP 701**](https://peps.python.org/pep-0701/). Concretely, `STRING` tokens are no longer produced for f-strings; in their stead the tokens spelled out in [**PEP 701**](https://peps.python.org/pep-0701/) appear: `FSTRING_START`, `FSTRING_MIDDLE` and `FSTRING_END` now turn up for the f-string "string" portions on top of the tokens that fit the tokenization within the expression components. As an illustration, given the f-string `f"start {1+1} end"` the previous tokenizer produced:

```python
1,0-1,18:           STRING         'f"start {1+1} end"'

```

while the new version emits:

```python
1,0-1,2:            FSTRING_START  'f"'
1,2-1,8:            FSTRING_MIDDLE 'start '
1,8-1,9:            OP             '{'
1,9-1,10:           NUMBER         '1'
1,10-1,11:          OP             '+'
1,11-1,12:          NUMBER         '1'
1,12-1,13:          OP             '}'
1,13-1,17:          FSTRING_MIDDLE ' end'
1,17-1,18:          FSTRING_END    '"'

```

On top of that, a few small behavioural shifts may follow from the changes that supporting [**PEP 701**](https://peps.python.org/pep-0701/) demanded. A sampling of those shifts:

  - For certain invalid Python characters such as `!`, the `type` attribute on the emitted tokens has moved from `ERRORTOKEN` over to `OP`.

  - Single-line strings that are incomplete now likewise raise [`tokenize.TokenError`](https://docs.python.org/3.14/library/tokenize.html#tokenize.TokenError), matching how incomplete multiline strings behave.

  - Some incomplete or otherwise invalid Python code now raises [`tokenize.TokenError`](https://docs.python.org/3.14/library/tokenize.html#tokenize.TokenError) during tokenization rather than handing back arbitrary `ERRORTOKEN` tokens.

  - Combining tabs together with spaces for indentation inside one file is no longer allowed and will raise a [`TabError`](https://docs.python.org/3.14/library/exceptions.html#TabError).

- The [`threading`](https://docs.python.org/3.14/library/threading.html#module-threading) module now counts on the `_thread` module carrying an `_is_main_interpreter` attribute. That attribute is a zero-argument function returning `True` whenever the interpreter currently running is the main one.

Whatever library or application ships its own custom `_thread` module ought to also supply `_is_main_interpreter()`. (See [gh-112826](https://github.com/python/cpython/issues/112826).)

[Subject index](INDEX.md) · [Previous source section](porting-to-python-3-12.md) · [Release/subject declaration](summary-release-highlights.md) · [Next source section](build-changes.md)
