# What's New In Python 3.13 / Summary ? Release Highlights - argparse, base64, copy, dbm

> Whatsnew reference. Wording is paraphrased; identifiers stay verbatim.

### What's New In Python 3.13

Editors:

Adam Turner and Thomas Wouters

These notes describe what is new in Python 3.13 relative to version 3.12. The 3.13 release shipped on October 7, 2024. Consult the [changelog](https://docs.python.org/3.14/whatsnew/changelog.html#changelog) for an exhaustive listing.

See also

[**PEP 719**](https://peps.python.org/pep-0719/) ? Python 3.13 Release Schedule

### Summary - Release Highlights

This is a stable edition of the Python language, bundling a combination of adjustments to the language itself, its runtime, and the standard library. Among the headline additions are a reworked interactive interpreter, trial-stage support for a free-threaded mode ([**PEP 703**](https://peps.python.org/pep-0703/)), plus a Just-In-Time compiler ([**PEP 744**](https://peps.python.org/pep-0744/)).

Diagnostics keep getting better: tracebacks are now shown in color out of the box. The [`locals()`](https://docs.python.org/3.14/library/functions.html#locals) builtin gained well-specified behavior for altering the mapping it hands back, and type parameters can now carry default values.

On the library side you will find deprecated APIs and modules pulled out, alongside the customary gains in ergonomics and accuracy. A handful of older standard library modules have at last been dropped after being deprecated back in Python 3.11 ([**PEP 594**](https://peps.python.org/pep-0594/)).

Rather than fully specifying every addition, this document offers a handy survey. Turn to the documentation for the fine print, for instance the [Library Reference](https://docs.python.org/3.14/library/index.html#library-index) and [Language Reference](https://docs.python.org/3.14/reference/index.html#reference-index). When you need the entire implementation story and the reasoning behind a change, the relevant PEP is the place to look; be aware, though, that PEPs are typically not maintained after a feature lands fully. Consult Porting to Python 3.13 for advice on moving up from older Python releases.

---

Interpreter improvements:

- A substantially upgraded interactive interpreter together with better error messages.

- [**PEP 667**](https://peps.python.org/pep-0667/): The [`locals()`](https://docs.python.org/3.14/library/functions.html#locals) builtin now carries defined semantics when the mapping it returns is mutated. Debuggers for Python and comparable tooling can henceforth update local variables in optimized scopes more dependably, even while code runs concurrently.

- [**PEP 703**](https://peps.python.org/pep-0703/): CPython 3.13 ships trial support for execution with the [global interpreter lock](https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock) turned off. Refer to Free-threaded CPython for further specifics.

- [**PEP 744**](https://peps.python.org/pep-0744/): A rudimentary JIT compiler landed. For now it stays off by default (we might switch it on down the road). The speedups are slight ? we anticipate refining this across the coming releases.

- Color is available in the fresh interactive interpreter, plus in tracebacks and doctest output. You can switch it off via the [`PYTHON_COLORS`](https://docs.python.org/3.14/using/cmdline.html#envvar-PYTHON_COLORS) and [`NO_COLOR`](https://no-color.org/) environment variables.

Python data model improvements:

- [`__static_attributes__`](https://docs.python.org/3.14/reference/datamodel.html#type.__static_attributes__) keeps the names of attributes reached through `self.X` within any function inside a class body.

- [`__firstlineno__`](https://docs.python.org/3.14/reference/datamodel.html#type.__firstlineno__) holds the first line number where a class is defined.

Significant improvements in the standard library:

- A fresh [`PythonFinalizationError`](https://docs.python.org/3.14/library/exceptions.html#PythonFinalizationError) exception was added; it fires when an operation is disallowed during [finalization](https://docs.python.org/3.14/glossary.html#term-interpreter-shutdown).

- The [`argparse`](https://docs.python.org/3.14/library/argparse.html#module-argparse) module can now deprecate command-line options, positional arguments, and subcommands.

- Two new functions, [`base64.z85encode()`](https://docs.python.org/3.14/library/base64.html#base64.z85encode) and [`base64.z85decode()`](https://docs.python.org/3.14/library/base64.html#base64.z85decode), handle encoding and decoding of [Z85 data](https://rfc.zeromq.org/spec/32/).

- The [`copy`](https://docs.python.org/3.14/library/copy.html#module-copy) module gained a [`copy.replace()`](https://docs.python.org/3.14/library/copy.html#copy.replace) function that works with numerous builtin types plus any class that defines the [`__replace__()`](https://docs.python.org/3.14/library/copy.html#object.__replace__) method.

- The brand-new [`dbm.sqlite3`](https://docs.python.org/3.14/library/dbm.html#module-dbm.sqlite3) module serves as the default [`dbm`](https://docs.python.org/3.14/library/dbm.html#module-dbm) backend going forward.

-

- Drop the `typing.io` and `typing.re` namespaces.

- Drop chained [`classmethod`](https://docs.python.org/3.14/library/functions.html#classmethod) descriptors.

Release schedule changes:

[**PEP 602**](https://peps.python.org/pep-0602/) (?Annual Release Cycle for Python?) was revised so that the full-support (?bugfix?) window for fresh releases now lasts two years. Under this revised policy:

- Python 3.9–3.12 receive one and a half years of full support, then three and a half years of security fixes.

- Python 3.13 and beyond receive two years of full support, then three years of security fixes.

[Subject index](INDEX.md) · [Next source section](timer-notification-and-library-highlights.md) · [Previous source section](timer-notification-and-library-highlights.md) · [Next source section](a-better-interactive-interpreter.md)
