# What's New In Python 3.7 / PEP 565: Show DeprecationWarning in `__main__` — __main__

### PEP 565: Show DeprecationWarning in `__main__`

How [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) is treated by default has shifted so these warnings appear once more out of the box, though only where the originating code runs straight inside the [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__) module. Because of that, people writing single-file scripts and those at the interactive prompt will again notice deprecation warnings for the APIs they call, while deprecation warnings raised from imported application, library, and framework code stay suppressed by default.

Following this change, three distinct deprecation warning behaviours are now available to developers from the standard library:

- [`FutureWarning`](https://docs.python.org/3.14/library/exceptions.html#FutureWarning): shown by default in every case, advised for warnings meant for the end users of an application (for instance over deprecated application configuration settings).

- [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning): shown by default solely within [`__main__`](https://docs.python.org/3.14/library/__main__.html#module-__main__) and while tests run, advised for warnings aimed at fellow Python developers where upgrading a version could alter behaviour or raise an error.

- [`PendingDeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#PendingDeprecationWarning): shown by default solely while tests run, meant for situations where some later version upgrade will switch the warning category over to [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) or [`FutureWarning`](https://docs.python.org/3.14/library/exceptions.html#FutureWarning).

Up to now [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) along with [`PendingDeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#PendingDeprecationWarning) surfaced only while tests ran, so developers mostly writing single-file scripts or working at the interactive prompt might be caught off guard by breaking changes in the APIs they relied on.

See also

[**PEP 565**](https://peps.python.org/pep-0565/) — Show DeprecationWarning in `__main__`

PEP written and implemented by Nick Coghlan

[Subject index](INDEX.md) · [Previous source section](pep-564-new-time-functions-with-nanosecond-resolution.md) · [Next source section](pep-560-core-support-for-typing-module-and-generic-types.md) · [Release/subject declaration](summary-release-highlights.md)
