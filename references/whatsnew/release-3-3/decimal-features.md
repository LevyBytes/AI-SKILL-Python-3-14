# What's New In Python 3.3 / decimal / Features — decimal

#### Features

- You can switch on tighter rules for combining floats with Decimals through the [`FloatOperation`](https://docs.python.org/3.14/library/decimal.html#decimal.FloatOperation) signal.

- When Python is built with threading turned off, the C build drops the costly thread-local context plumbing on its own. Under that build the [`HAVE_THREADS`](https://docs.python.org/3.14/library/decimal.html#decimal.HAVE_THREADS) variable holds `False`.

[Subject index](INDEX.md) · [Previous source section](decimal.md) · [Next source section](decimal-api-changes.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](decimal.md)
