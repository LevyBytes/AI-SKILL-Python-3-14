# Python 3.14.1 final / library / urllib robotparser

[gh-88375](https://github.com/python/cpython/issues/88375): Corrects how the [`urllib.robotparser`](https://docs.python.org/3.14/library/urllib.robotparser.html#module-urllib.robotparser) module normalizes the `robots.txt` rules and URLs. A trailing `?` is no longer dropped. The raw special characters `?`, `=` and `&` are now told apart from their percent-encoded counterparts.

[gh-111788](https://github.com/python/cpython/issues/111788): Corrects parsing failures within the [`urllib.robotparser`](https://docs.python.org/3.14/library/urllib.robotparser.html#module-urllib.robotparser) module. Odd paths no longer cause a parse failure. A non-UTF-8 `robots.txt` file no longer causes a decode failure.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
