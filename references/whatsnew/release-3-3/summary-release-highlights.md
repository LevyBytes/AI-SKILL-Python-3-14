# What's New In Python 3.3 / Summary ? Release highlights - faulthandler, importlib, ipaddress, lzma, unittest.mock, venv

### What's New In Python 3.3

This document describes the additions in Python 3.3 relative to 3.2. The 3.3 release landed on September 29, 2012. Consult the [changelog](https://docs.python.org/3.3/whatsnew/changelog.html) for the complete record.

See also

[**PEP 398**](https://peps.python.org/pep-0398/) - Python 3.3 Release Schedule

### Summary - Release highlights

Additions to the syntax:

- A fresh `yield from` expression for delegating between generators.

- Once more, the `u'unicode'` form is permitted for [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) objects.

Fresh library modules:

- [`faulthandler`](https://docs.python.org/3.14/library/faulthandler.html#module-faulthandler) (aids in tracking down low-level crashes)

- [`ipaddress`](https://docs.python.org/3.14/library/ipaddress.html#module-ipaddress) (high-level objects representing IP addresses and masks)

- [`lzma`](https://docs.python.org/3.14/library/lzma.html#module-lzma) (compress data using the XZ / LZMA algorithm)

- [`unittest.mock`](https://docs.python.org/3.14/library/unittest.mock.html#module-unittest.mock) (swap out parts of your system under test with mock objects)

- [`venv`](https://docs.python.org/3.14/library/venv.html#module-venv) (Python virtual environments, as in the popular `virtualenv` package)

Fresh built-in capabilities:

- A redesigned I/O exception hierarchy.

Gains in the implementation:

- Import machinery rebuilt on top of [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib).

- Unicode strings that take less space.

- Attribute dictionaries that take less space.

Library modules that improved substantially:

- A C Accelerator backing the decimal module.

- Stronger unicode treatment within the email module ([provisional](https://docs.python.org/3.14/glossary.html#term-provisional-package)).

Gains for security:

- Randomized hashing is enabled out of the box.

Continue reading below for an exhaustive rundown of the changes visible to users.

[Subject index](INDEX.md) · [Next source section](pep-405-virtual-environments.md)
