# What's new in Python 3.14 / argparse — argparse

> (Contributed by Jim Baker, Guido van Rossum, Paul Everitt, Koudai Aono, Lysandros Nikolaou, Dave Peck, Adam Turner, Jelle Zijlstra, Bénédikt Tran, and Pablo Galindo Salgado in [gh-132661](https://github.com/python/cpython/issues/132661).)

### Improved modules

### argparse

- How the Python interpreter was told to locate the `__main__` module code is now mirrored by the default value of the [program name](https://docs.python.org/3.14/library/argparse.html#prog) for [`argparse.ArgumentParser`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser). (Contributed by Serhiy Storchaka and Alyssa Coghlan in [gh-66436](https://github.com/python/cpython/issues/66436).)

- A new optional *suggest_on_error* parameter has been added to [`argparse.ArgumentParser`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser), which turns on suggestions for argument choices and subparser names whenever a user mistypes them. (Contributed by Savannah Ostrowski in [gh-124456](https://github.com/python/cpython/issues/124456).)

- Turn on color for help text, which the optional *color* parameter to [`argparse.ArgumentParser`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser) can disable. [environment variables](https://docs.python.org/3.14/using/cmdline.html#using-on-controlling-color) may also govern this. (Contributed by Hugo van Kemenade in [gh-130645](https://github.com/python/cpython/issues/130645).)

### Removed

### argparse

- Drop the *type*, *choices*, and *metavar* parameters from `BooleanOptionalAction`. They have carried a deprecation since Python 3.12. (Contributed by Nikita Sobolev in [gh-118805](https://github.com/python/cpython/issues/118805).)

- Invoking [`add_argument_group()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.add_argument_group) on an argument group now triggers a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). In the same way, calling `add_argument_group()` or [`add_mutually_exclusive_group()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.add_mutually_exclusive_group) on a mutually exclusive group now each raise `ValueError`s. Such ?nesting? was never a supported feature, frequently misbehaved, and got unintentionally surfaced via inheritance. That capability has carried a deprecation since Python 3.11. (Contributed by Savannah Ostrowski in [gh-127186](https://github.com/python/cpython/issues/127186).)

[Subject index](INDEX.md) · [Previous source section](new-modules.md) · [Next source section](ast.md) · [Release/subject declaration](summary-release-highlights.md) · [Previous source section](zlib.md)
