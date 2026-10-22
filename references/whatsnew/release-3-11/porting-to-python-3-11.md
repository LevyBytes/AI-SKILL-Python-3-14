# What's New In Python 3.11 / Porting to Python 3.11 — ast, asyncio-eventloop, calendar, codecs, concurrent.futures, fileinput, io, locale, pdb, random, re

### Porting to Python 3.11

Below you will find both the previously covered changes plus extra bugfixes affecting the Python API that might oblige you to adjust your own Python code.

The C API porting guidance appears in its own section.

- [`open()`](https://docs.python.org/3.14/library/functions.html#open), [`io.open()`](https://docs.python.org/3.14/library/io.html#io.open), [`codecs.open()`](https://docs.python.org/3.14/library/codecs.html#codecs.open) and [`fileinput.FileInput`](https://docs.python.org/3.14/library/fileinput.html#fileinput.FileInput) will no longer take `'U'` (“universal newline”) within the file mode. Under Python 3, “universal newline” behavior applies automatically every time a file gets opened in text mode, and the `'U'` flag has carried a deprecation since Python 3.3. The [newline parameter](https://docs.python.org/3.14/library/functions.html#open-newline-parameter) passed to these calls governs how universal newlines behave. (Contributed by Victor Stinner in [bpo-37330](https://bugs.python.org/issue?@action=redirect&bpo=37330).)

- [`ast.AST`](https://docs.python.org/3.14/library/ast.html#ast.AST) node positions now get validated once they are handed to [`compile()`](https://docs.python.org/3.14/library/functions.html#compile) along with other functions of that kind. Should invalid positions turn up, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised. (Contributed by Pablo Galindo in [gh-93351](https://github.com/python/cpython/issues/93351))

- Forbade handing non-[`concurrent.futures.ThreadPoolExecutor`](https://docs.python.org/3.14/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor) executors to [`asyncio.loop.set_default_executor()`](https://docs.python.org/3.14/library/asyncio-eventloop.html#asyncio.loop.set_default_executor), after this had been deprecated back in Python 3.8. (Contributed by Illia Volochii in [bpo-43234](https://bugs.python.org/issue?@action=redirect&bpo=43234).)

- [`calendar`](https://docs.python.org/3.14/library/calendar.html#module-calendar): When no locale gets passed, the [`calendar.LocaleTextCalendar`](https://docs.python.org/3.14/library/calendar.html#calendar.LocaleTextCalendar) along with [`calendar.LocaleHTMLCalendar`](https://docs.python.org/3.14/library/calendar.html#calendar.LocaleHTMLCalendar) classes now rely on [`locale.getlocale()`](https://docs.python.org/3.14/library/locale.html#locale.getlocale) rather than on [`locale.getdefaultlocale()`](https://docs.python.org/3.14/library/locale.html#locale.getdefaultlocale). (Contributed by Victor Stinner in [bpo-46659](https://bugs.python.org/issue?@action=redirect&bpo=46659).)

- When the [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) module reads its `.pdbrc` configuration file, it now decodes that file as `'UTF-8'`.

> (Contributed by Srinivas Reddy Thatiparthy (శ్రీనివాస్ రెడ్డి తాటిపర్తి) in [bpo-41137](https://bugs.python.org/issue?@action=redirect&bpo=41137).)

- The *population* argument of [`random.sample()`](https://docs.python.org/3.14/library/random.html#random.sample) has to be a sequence, and the automatic turning of [`set`](https://docs.python.org/3.14/library/stdtypes.html#set)s into [`list`](https://docs.python.org/3.14/library/stdtypes.html#list)s is no longer offered. On top of that, when the requested sample exceeds the population in size, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) results. (Contributed by Raymond Hettinger in [bpo-40465](https://bugs.python.org/issue?@action=redirect&bpo=40465).)

- The *random* optional argument of [`random.shuffle()`](https://docs.python.org/3.14/library/random.html#random.shuffle) is gone. Formerly it let you supply any random function for shuffling; from now on [`random.random()`](https://docs.python.org/3.14/library/random.html#random.random) (which was its earlier default) gets used every time.

- Within [`re`](https://docs.python.org/3.14/library/re.html#module-re) [Regular Expression Syntax](https://docs.python.org/3.14/library/re.html#re-syntax), global inline flags (e.g. `(?i)`) are now permitted solely at the beginning of a regular expression. Placing them anywhere else has carried a deprecation since Python 3.6. (Contributed by Serhiy Storchaka in [bpo-47066](https://bugs.python.org/issue?@action=redirect&bpo=47066).)

- Inside the [`re`](https://docs.python.org/3.14/library/re.html#module-re) module, a number of long-standing defects got resolved that, on uncommon occasions, might leave capture groups holding an incorrect value. As a result, the captured text in such situations can differ. (Contributed by Ma Lin in [bpo-35859](https://bugs.python.org/issue?@action=redirect&bpo=35859).)

[Subject index](INDEX.md) · [Previous source section](removed.md) · [Next source section](build-changes.md) · [Release/subject declaration](summary-release-highlights.md)
