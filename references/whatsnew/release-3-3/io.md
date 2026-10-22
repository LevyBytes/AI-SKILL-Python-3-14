# What's New In Python 3.3 / io — io

### io

A new `'x'` mode now sits on the [`open()`](https://docs.python.org/3.14/library/io.html#io.open) function for creating a file exclusively, raising [`FileExistsError`](https://docs.python.org/3.14/library/exceptions.html#FileExistsError) whenever the file is already there. The design tracks the C11 ‘x’ mode supplied to fopen().

David Townshend landed this ([bpo-12760](https://bugs.python.org/issue?@action=redirect&bpo=12760)).

A new *write_through* optional argument joins the constructor of the [`TextIOWrapper`](https://docs.python.org/3.14/library/io.html#io.TextIOWrapper) class. Set *write_through* to `True` and every `write()` skips buffering: whatever you write on the `TextIOWrapper` object passes straight down to its underlying binary buffer.

[Subject index](INDEX.md) · [Previous source section](inspect.md) · [Next source section](itertools.md) · [Release/subject declaration](summary-release-highlights.md)
