# Python 3.14.0 alpha 3 / library / argparse

[gh-127133](https://github.com/python/cpython/issues/127133): Invoking [`argparse.ArgumentParser.add_argument_group()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.add_argument_group) on an argument group, or invoking `argparse.ArgumentParser.add_argument_group()` along with [`argparse.ArgumentParser.add_mutually_exclusive_group()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.add_mutually_exclusive_group) on a mutually exclusive group, now raises exceptions. Such nesting was never a supported pattern, frequently misbehaved, and leaked out by accident through inheritance. Python 3.11 already flagged this behavior as deprecated.

[gh-86463](https://github.com/python/cpython/issues/86463): The `usage` argument of [`argparse.ArgumentParser`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser) no longer changes the default that subparsers give to the `prog` parameter.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
