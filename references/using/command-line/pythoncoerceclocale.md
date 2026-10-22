# PYTHONCOERCECLOCALE

PYTHONCOERCECLOCALE

When set to the value `0`, it makes the main Python command line application skip coercing the legacy ASCII-based C and POSIX locales into a more capable UTF-8 based alternative.

Suppose this variable is *not* set (or holds a value besides `0`), the `LC_ALL` locale override environment variable is likewise unset, and, for the `LC_CTYPE` category, the locale presently in effect amounts to either the default `C` locale or the explicitly ASCII-based `POSIX` locale; then the Python CLI will try to set up these locales for the `LC_CTYPE` category in the sequence shown before loading the interpreter runtime:

- `C.UTF-8`

- `C.utf8`

- `UTF-8`

Should setting one of these locale categories work, then the `LC_CTYPE` environment variable is likewise set to match in the current process environment ahead of the Python runtime being initialized. This guarantees that, on top of being visible to both the interpreter itself and other locale-aware components within the same process (the GNU `readline` library, for example), the revised setting is also visible in subprocesses (whether or not those processes run a Python interpreter), along with in operations that consult the environment instead of the current C locale (Python's own [`locale.getdefaultlocale()`](https://docs.python.org/3.14/library/locale.html#locale.getdefaultlocale), for example).

Setting up one of these locales (whether explicitly or through the implicit locale coercion described above) automatically switches on the `surrogateescape` [error handler](https://docs.python.org/3.14/library/codecs.html#error-handlers) for [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin) and [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout) ([`sys.stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr) keeps using `backslashreplace` just as it does in any other locale). You can override this stream handling behavior with `PYTHONIOENCODING` in the usual way.

For debugging purposes, setting `PYTHONCOERCECLOCALE=warn` makes Python emit warning messages on `stderr` if either the locale coercion kicks in, or else if a locale that *would* have set off coercion remains active when the Python runtime gets initialized.

Note as well that even with locale coercion turned off, or when it can't locate a suitable target locale, `PYTHONUTF8` still switches on by default in legacy ASCII-based locales. You have to turn off both features to compel the interpreter to use `ASCII` rather than `UTF-8` for system interfaces.

[Availability](https://docs.python.org/3.14/library/intro.html#availability): Unix.

Added in version 3.7: See [**PEP 538**](https://peps.python.org/pep-0538/) for more details.

[Subject index](INDEX.md) · [Previous source section](pythonlegacywindowsstdio.md) · [Following source section](pythondevmode.md)
