# Python 3.14.0 alpha 2 / library / argparse

[gh-125355](https://github.com/python/cpython/issues/125355): Repair multiple bugs within [`argparse.ArgumentParser.parse_intermixed_args()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.parse_intermixed_args).

  - While parsing proceeds, the parser is no longer altered for the duration.

  - Default values get processed only once now.

  - Required mutually exclusive groups that hold positional arguments are supported at last.

  - Reports of missing arguments now list every required optional plus positional argument by name.

  - Within parse_known_intermixed_args(), unknown options may be interleaved among positional arguments.

[gh-126068](https://github.com/python/cpython/issues/126068): Adjust exceptions raised by the [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) module so translation now applies solely to error text for ArgumentError together with ArgumentTypeError. From now on, ArgumentError covers only command line errors and never logical program errors. TypeError now replaces ValueError for certain logical errors.

[gh-58032](https://github.com/python/cpython/issues/58032): Mark the [`argparse.FileType`](https://docs.python.org/3.14/library/argparse.html#argparse.FileType) type converter for deprecation.

[gh-125542](https://github.com/python/cpython/issues/125542): Mark for deprecation the keyword-only *prefix_chars* argument when passed to [`argparse.ArgumentParser.add_argument_group()`](https://docs.python.org/3.14/library/argparse.html#argparse.ArgumentParser.add_argument_group).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
