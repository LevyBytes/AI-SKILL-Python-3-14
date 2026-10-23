# What's New In Python 3.7 / PEP 538: Legacy C Locale Coercion - readline, sys

### PEP 538: Legacy C Locale Coercion

A recurring difficulty across the Python 3 line has been settling on a reasonable default approach to the "7-bit ASCII" text encoding presumption that the standard C or POSIX locale currently brings on non-Windows systems.

[**PEP 538**](https://peps.python.org/pep-0538/) revises the default interpreter command line behavior so it automatically promotes that locale to a UTF-8 capable locale when one exists, per the writeup of the new [`PYTHONCOERCECLOCALE`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONCOERCECLOCALE) environment variable. Setting `LC_CTYPE` automatically in this manner makes the core interpreter together with locale-aware C extensions (for instance [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline)) treat UTF-8, instead of ASCII, as the implicit text encoding.

The platform support specification in [**PEP 11**](https://peps.python.org/pep-0011/) was likewise revised to restrict complete text handling support to properly configured locales that are not ASCII based.

Along with this change, the default error handler for [`stdin`](https://docs.python.org/3.14/library/sys.html#sys.stdin) and [`stdout`](https://docs.python.org/3.14/library/sys.html#sys.stdout) becomes `surrogateescape` (in place of `strict`) whenever any recognized coercion target locale is in play (presently `C.UTF-8`, `C.utf8`, and `UTF-8`). For [`stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr) the default error handler stays `backslashreplace`, no matter the locale.

By default the coercion happens quietly, yet to help diagnose integration trouble that might stem from the locale, you can ask for explicit warnings (printed straight to [`stderr`](https://docs.python.org/3.14/library/sys.html#sys.stderr)) by setting `PYTHONCOERCECLOCALE=warn`. That value additionally makes the Python runtime warn when the legacy C locale is still in effect as the core interpreter starts up.

Although [**PEP 538**](https://peps.python.org/pep-0538/)'s coercion carries the upside of reaching extension modules (for instance GNU `readline`) plus child processes (among them ones running non-Python programs and earlier Python versions), its drawback is that the host must already provide a fitting target locale. For the situation where no fitting target locale exists (as happens on RHEL/CentOS 7, say), Python 3.7 additionally provides PEP 540: Forced UTF-8 Runtime Mode.

See also

[**PEP 538**](https://peps.python.org/pep-0538/): Coercing the legacy C locale to a UTF-8 based locale

PEP written and implemented by Nick Coghlan.

[Subject index](INDEX.md) · [Previous source section](pep-563-postponed-evaluation-of-annotations.md) · [Next source section](pep-540-forced-utf-8-runtime-mode.md) · [Release/subject declaration](summary-release-highlights.md)
