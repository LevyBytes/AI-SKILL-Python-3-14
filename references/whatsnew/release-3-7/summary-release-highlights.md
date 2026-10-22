# What's New In Python 3.7 / Summary — Release Highlights — asyncio, contextvars, dataclasses, time

### What's New In Python 3.7

Editor:

Elvis Pranskevichus <[elvis@magic.io](mailto:elvis%40magic.io)>

This writeup covers what arrived in Python 3.7 relative to 3.6. The 3.7 release shipped on June 27, 2018. The complete record lives in the [changelog](https://docs.python.org/3.14/whatsnew/changelog.html#changelog).

### Summary — Release Highlights

New syntax features:

- PEP 563, postponed evaluation of type annotations.

Backwards incompatible syntax changes:

- [`async`](https://docs.python.org/3.14/reference/compound_stmts.html#async) and [`await`](https://docs.python.org/3.14/reference/expressions.html#await) have become reserved keywords.

New library modules:

- [`contextvars`](https://docs.python.org/3.14/library/contextvars.html#module-contextvars): PEP 567 — Context Variables

- [`dataclasses`](https://docs.python.org/3.14/library/dataclasses.html#module-dataclasses): PEP 557 — Data Classes

- importlib.resources

New built-in features:

- PEP 553, the new [`breakpoint()`](https://docs.python.org/3.14/library/functions.html#breakpoint) function.

Python data model improvements:

- PEP 562, customization of access to module attributes.

- PEP 560, core support for typing module and generic types.

- the property that [dict](https://docs.python.org/3.14/library/stdtypes.html#typesmapping) objects keep keys in insertion order [has been declared](https://mail.python.org/pipermail/python-dev/2017-December/151283.html) an official guarantee of the Python language specification.

Significant improvements in the standard library:

- The [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) module picked up fresh capabilities along with sizable usability and speed gains.

- The [`time`](https://docs.python.org/3.14/library/time.html#module-time) module added functions that operate at nanosecond resolution.

CPython implementation improvements:

- Steering away from ASCII as the implicit text encoding:

  - PEP 538, legacy C locale coercion

  - PEP 540, forced UTF-8 runtime mode

- PEP 552, deterministic .pycs

- New Python Development Mode

- PEP 565, improved [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) handling

C API improvements:

- PEP 539, new C API for thread-local storage

Documentation improvements:

- PEP 545, Python documentation translations

- New documentation translations: [Japanese](https://docs.python.org/ja/), [French](https://docs.python.org/fr/), and [Korean](https://docs.python.org/ko/).

This version brings worthwhile speed gains across numerous components. The Optimizations section enumerates each one.

To review what might break against earlier Python versions, consult the Porting to Python 3.7 section.

[Subject index](INDEX.md) · [Next source section](pep-563-postponed-evaluation-of-annotations.md)
