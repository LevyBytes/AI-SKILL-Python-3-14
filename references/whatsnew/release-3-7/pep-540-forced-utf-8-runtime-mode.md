# What's New In Python 3.7 / PEP 540: Forced UTF-8 Runtime Mode — os, sys

### PEP 540: Forced UTF-8 Runtime Mode

The new [`-X`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-X) `utf8` command line option together with the [`PYTHONUTF8`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONUTF8) environment variable switch on the [Python UTF-8 Mode](https://docs.python.org/3.14/library/os.html#utf8-mode).

While running in UTF-8 mode, CPython disregards the locale configuration and defaults to the UTF-8 encoding. For the [`sys.stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin) and [`sys.stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout) streams the error handlers become `surrogateescape`.

You can rely on forced UTF-8 mode to alter how text is handled inside an embedded Python interpreter while leaving the embedding application's locale configuration untouched.

Although [**PEP 540**](https://peps.python.org/pep-0540/)'s UTF-8 mode has the upside of functioning no matter which locales the host offers, the catch is that it does nothing for extension modules (for instance GNU `readline`), child processes that run non-Python programs, and child processes on older Python versions. So as to lower the chance of mangling text data while talking to those pieces, Python 3.7 additionally provides PEP 540: Forced UTF-8 Runtime Mode).

UTF-8 mode turns on automatically when the locale is `C` or `POSIX` and the [**PEP 538**](https://peps.python.org/pep-0538/) locale coercion mechanism cannot switch it over to a UTF-8 capable substitute (be that because `PYTHONCOERCECLOCALE=0` is set, because `LC_ALL` is set, or because no fitting target locale exists).

See also

[**PEP 540**](https://peps.python.org/pep-0540/) — Add a new UTF-8 mode

PEP written and implemented by Victor Stinner

[Subject index](INDEX.md) · [Previous source section](pep-538-legacy-c-locale-coercion.md) · [Next source section](pep-553-built-in-breakpoint.md) · [Release/subject declaration](summary-release-highlights.md)
