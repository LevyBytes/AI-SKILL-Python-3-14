# What's New In Python 3.11 / Summary — Release highlights — sys, tomllib

### What's New In Python 3.11

Editor:

Pablo Galindo Salgado

This document walks through what changed in Python 3.11 relative to 3.10. The 3.11 release shipped on October 24, 2022. The complete record lives in the [changelog](https://docs.python.org/3.14/whatsnew/changelog.html#changelog).

### Summary — Release highlights

- Compared against 3.10, Python 3.11 runs roughly 10-60% quicker; across the standard benchmark suite the average came out to a 1.25x speedup. Consult Faster CPython for the breakdown.

New syntax features:

- PEP 654: Exception Groups and except*

New built-in features:

- PEP 678: Exceptions can be enriched with notes

New standard library modules:

- > [**PEP 680**](https://peps.python.org/pep-0680/): [`tomllib`](https://docs.python.org/3.14/library/tomllib.html#module-tomllib) — Support for parsing [TOML](https://toml.io/) in the Standard Library

Interpreter improvements:

- PEP 657: Fine-grained error locations in tracebacks

- > New [`-P`](https://docs.python.org/3.14/using/cmdline.html#cmdoption-P) command line option and [`PYTHONSAFEPATH`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHONSAFEPATH) environment variable to disable automatically prepending potentially unsafe paths to [`sys.path`](https://docs.python.org/3.14/library/sys.html#sys.path)

New typing features:

- PEP 646: Variadic generics

- PEP 655: Marking individual TypedDict items as required or not-required

- PEP 673: Self type

- PEP 675: Arbitrary literal string type

- PEP 681: Data class transforms

Important deprecations, removals and restrictions:

- > [**PEP 594**](https://peps.python.org/pep-0594/): Many legacy standard library modules have been deprecated and will be removed in Python 3.13

- [**PEP 624**](https://peps.python.org/pep-0624/): Py_UNICODE encoder APIs have been removed

- [**PEP 670**](https://peps.python.org/pep-0670/): Macros converted to static inline functions

[Subject index](INDEX.md) · [Next source section](pep-657-fine-grained-error-locations-in-tracebacks.md)
