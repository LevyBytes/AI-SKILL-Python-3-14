# Python 3.12.0 alpha 1 / library / argparse

[gh-85308](https://github.com/python/cpython/issues/85308): Switched [`argparse.ArgumentParser`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser) over to the [filesystem encoding and error handler](https://docs.python.org/3.14/glossary.html#term-filesystem-encoding-and-error-handler) rather than the default text encoding when reading arguments out of a file (the `fromfile_prefix_chars` option, for instance). The impact lands on Windows; such argument files should now be saved as UTF-8 in place of the ANSI Codepage.

[gh-92445](https://github.com/python/cpython/issues/92445): Correct an [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) bug where `nargs="*"` raised an error rather than yielding an empty list once 0 arguments were supplied, in cases where choice had also been set within `parser.add_argument`.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
