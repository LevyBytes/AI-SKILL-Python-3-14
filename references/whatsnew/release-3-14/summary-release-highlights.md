# What's new in Python 3.14 / Summary — Release highlights — compression.zstd

### What's new in Python 3.14

Editors:

Adam Turner and Hugo van Kemenade

This document walks through what Python 3.14 adds relative to 3.13. The 3.14 release shipped on 7 October 2025. For the exhaustive list, consult the [changelog](https://docs.python.org/3.14/whatsnew/changelog.html#changelog).

See also

[**PEP 745**](https://peps.python.org/pep-0745/) — Python 3.14 release schedule

### Summary — Release highlights

The newest stable build of the Python language is 3.14, bundling a blend of adjustments across the language itself, its runtime, and the standard library. Among the headline additions are template string literals, lazily computed annotations, and standard-library support for subinterpreters.

On the library side you get markedly stronger introspection facilities within asyncio, Zstandard handling delivered through a fresh [`compression.zstd`](https://docs.python.org/3.14/library/compression.zstd.html#module-compression.zstd) module, REPL syntax highlighting, plus the customary deprecations and removals alongside gains in ergonomics and correctness.

Rather than serving as an exhaustive specification covering every addition, this page offers a handy summary. The authoritative material lives in the docs, including the [Library Reference](https://docs.python.org/3.14/library/index.html#library-index) and [Language Reference](https://docs.python.org/3.14/reference/index.html#reference-index). When you want the full implementation and the reasoning behind a change, read that feature's PEP; keep in mind, though, that a PEP often stops being maintained after the feature lands. Consult Porting to Python 3.14 when migrating from prior Python releases.

---

Interpreter improvements:

- [**PEP 649**](https://peps.python.org/pep-0649/) and [**PEP 749**](https://peps.python.org/pep-0749/): Deferred evaluation of annotations

- [**PEP 734**](https://peps.python.org/pep-0734/): Multiple interpreters in the standard library

- [**PEP 750**](https://peps.python.org/pep-0750/): Template strings

- [**PEP 758**](https://peps.python.org/pep-0758/): Allow except and except* expressions without brackets

- [**PEP 765**](https://peps.python.org/pep-0765/): Control flow in finally blocks

- [**PEP 768**](https://peps.python.org/pep-0768/): Safe external debugger interface for CPython

- A new type of interpreter

- Free-threaded mode improvements

- Improved error messages

- Incremental garbage collection

Significant improvements in the standard library:

- [**PEP 784**](https://peps.python.org/pep-0784/): Zstandard support in the standard library

- Asyncio introspection capabilities

- Concurrent safe warnings control

-

Syntax highlighting within the default interactive shell, plus colorized output across a number of standard library CLIs

C API improvements:

- [**PEP 741**](https://peps.python.org/pep-0741/): Python configuration C API

Platform support:

- [**PEP 776**](https://peps.python.org/pep-0776/): Emscripten is now an officially supported platform, at [**tier 3**](https://peps.python.org/pep-0011/#tier-3).

Release changes:

- [**PEP 779**](https://peps.python.org/pep-0779/): Free-threaded Python is officially supported

- [**PEP 761**](https://peps.python.org/pep-0761/): PGP signatures have been discontinued for official releases

- The experimental just-in-time compiler is now carried by the Windows and macOS binary releases

- Android now ships with its own binary releases

[Subject index](INDEX.md) · [Next source section](pep-649-pep-749-deferred-evaluation-of-annotations.md)
