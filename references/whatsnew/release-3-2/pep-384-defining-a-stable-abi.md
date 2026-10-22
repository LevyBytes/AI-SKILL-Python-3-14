# What's New In Python 3.2 / PEP 384: Defining a Stable ABI

### What's New In Python 3.2

Author:

Raymond Hettinger

The following walkthrough describes how Python 3.2 differs from 3.1. The 3.2 release shipped on February 20, 2011. A handful of notable items are covered here, each paired with sample code. Consult the [Misc/NEWS](https://github.com/python/cpython/blob/076ca6c3c8df3030307e548d9be792ce3c1c6eea/Misc/NEWS) file for the complete record.

See also

[**PEP 392**](https://peps.python.org/pep-0392/) - Python 3.2 Release Schedule

### PEP 384: Defining a Stable ABI

Historically, an extension module compiled against a single Python version frequently failed to load under a different version. On Windows in particular, each Python feature release meant recompiling every extension module a developer relied upon. That necessity stemmed from how openly extension modules were permitted to reach into Python interpreter internals.

Python 3.2 introduces a different path: an extension module that confines itself to a limited API (by defining Py_LIMITED_API) loses access to much of the internals, yet gains a guaranteed-stable collection of API functions across multiple releases. The upshot is that a module compiled for 3.2 under that regime keeps working on 3.3, 3.4, and onward. Modules relying on the layout of memory structures remain buildable, though each feature release forces a fresh recompile.

See also

[**PEP 384**](https://peps.python.org/pep-0384/) - Defining a Stable ABI

PEP written by Martin von Löwis.

[Subject index](INDEX.md) · [Next source section](argparse-command-line-parsing.md)
