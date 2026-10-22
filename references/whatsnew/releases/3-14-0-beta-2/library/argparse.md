# Python 3.14.0 beta 2 / library / argparse

[gh-133653](https://github.com/python/cpython/issues/133653): Repair [`argparse.ArgumentParser`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser) when the *formatter_class* argument is supplied. Repair the TypeError raised when *formatter_class* is a custom subclass of `HelpFormatter`. Repair the TypeError raised when *formatter_class* is not a subclass of `HelpFormatter` and a non-standard *prefix_char* is used. Repair colorizing support when *formatter_class* is not a subclass of `HelpFormatter`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
