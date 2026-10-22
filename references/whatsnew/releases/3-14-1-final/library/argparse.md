# Python 3.14.1 final / library / argparse

[gh-139809](https://github.com/python/cpython/issues/139809): Keeps the subparser `prog` from being colorized too early in [`argparse.ArgumentParser.add_subparsers()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.add_subparsers), so that color environment variable changes made after the parser exists are still honored.

[gh-139736](https://github.com/python/cpython/issues/139736): Trims overly deep indentation in the default [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) `HelpFormatter`. Alexander Edland authored the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
