# Python 3.14.0 beta 2 / library / exceptions

[gh-134152](https://github.com/python/cpython/issues/134152): Resolved an [`UnboundLocalError`](https://docs.python.org/3.14/library/exceptions.html#UnboundLocalError) that might arise while parsing [`email`](https://docs.python.org/3.14/library/email.html#module-email) headers when an anticipated trailing delimiter is absent in certain situations.

[gh-133982](https://github.com/python/cpython/issues/133982): Raise [`RuntimeWarning`](https://docs.python.org/3.14/library/exceptions.html#RuntimeWarning) within the Python implementation of [`io`](https://docs.python.org/3.14/library/io.html#module-io) whenever the [file-like object](https://docs.python.org/3.14/glossary.html#term-file-object) is left unclosed explicitly while several I/O layers are present.

[gh-71253](https://github.com/python/cpython/issues/71253): Raise [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) from [`open()`](https://docs.python.org/3.14/library/functions.html#open) whenever *opener* hands back a negative file-descriptor inside the Python implementation of [`io`](https://docs.python.org/3.14/library/io.html#module-io), matching what the C implementation does.

[gh-134381](https://github.com/python/cpython/issues/134381): Repair the [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) raised when a not-started [`threading.Thread`](https://docs.python.org/3.14/library/threading.html#threading.Thread) is used after a call to [`os.fork()`](https://docs.python.org/3.14/library/os.html#os.fork)

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
