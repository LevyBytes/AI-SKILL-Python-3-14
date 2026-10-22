# Python 3.13.0 alpha 3 / library / readline

[gh-112292](https://github.com/python/cpython/issues/112292): Fix a [`readline`](https://docs.python.org/3.14/library/readline.html#module-readline) crash that occurs when it is imported from inside a sub interpreter. Anthony Shaw wrote the patch

[gh-112105](https://github.com/python/cpython/issues/112105): Get [`readline.set_completer_delims()`](https://docs.python.org/3.14/library/readline.html#readline.set_completer_delims) working under libedit

[gh-112510](https://github.com/python/cpython/issues/112510): Provide [`readline.backend`](https://docs.python.org/3.14/library/readline.html#readline.backend) to report which backend readline relies on (`editline` or `readline`)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
