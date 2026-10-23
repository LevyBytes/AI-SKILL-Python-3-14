# What’s New In Python 3.12 / Summary – Release highlights - asyncio, os, pathlib, sqlite3, typing, uuid

### What’s New In Python 3.12

Editor:

Adam Turner

Here the additions in Python 3.12 are described, set against 3.11. The release of Python 3.12 happened on October 2, 2023. The [changelog](https://docs.python.org/3.14/whatsnew/changelog.html#changelog) carries the exhaustive list.

See also

[**PEP 693**](https://peps.python.org/pep-0693/) – Python 3.12 Release Schedule

### Summary – Release highlights

As a stable edition of the Python language, Python 3.12 blends adjustments to both the language itself and the standard library. Where the library is concerned, the work centers on retiring deprecated APIs, on usability, and on correctness. One notable item: the standard library no longer ships the `distutils` package. Within [`os`](https://docs.python.org/3.14/library/os.html#module-os) and [`pathlib`](https://docs.python.org/3.14/library/pathlib.html#module-pathlib), filesystem handling gained numerous refinements, while several modules now run faster.

On the language side, the emphasis is usability: many former constraints on [f-strings](https://docs.python.org/3.14/glossary.html#term-f-string) are gone, and the ‘Did you mean …’ hints keep getting better. Ergonomics around [generic types](https://docs.python.org/3.14/glossary.html#term-generic-type) and [type aliases](https://docs.python.org/3.14/glossary.html#term-type-alias) with static type checkers benefit from the fresh type parameter syntax together with the [`type`](https://docs.python.org/3.14/reference/simple_stmts.html#type) statement.

Rather than fully specifying every new capability, this write-up offers a handy survey. The documentation holds the exhaustive treatment — see the [Library Reference](https://docs.python.org/3.14/library/index.html#library-index) plus the [Language Reference](https://docs.python.org/3.14/reference/index.html#reference-index). For the full picture of how a change was built and why, consult the relevant PEP; keep in mind, though, that once a feature lands fully, its PEP is generally no longer maintained.

---

New syntax features:

- PEP 695, type parameter syntax and the [`type`](https://docs.python.org/3.14/reference/simple_stmts.html#type) statement

New grammar features:

- PEP 701, [f-strings](https://docs.python.org/3.14/glossary.html#term-f-string) in the grammar

Interpreter improvements:

- PEP 684, a unique per-interpreter [GIL](https://docs.python.org/3.14/glossary.html#term-global-interpreter-lock)

- PEP 669, low impact monitoring

- Improved ‘Did you mean …’ suggestions for [`NameError`](https://docs.python.org/3.14/library/exceptions.html#NameError), [`ImportError`](https://docs.python.org/3.14/library/exceptions.html#ImportError), and [`SyntaxError`](https://docs.python.org/3.14/library/exceptions.html#SyntaxError) exceptions

Python data model improvements:

- PEP 688, using the [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects) from Python

Significant improvements in the standard library:

- Subclassing is now permitted for the [`pathlib.Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) class

- Windows support within the [`os`](https://docs.python.org/3.14/library/os.html#module-os) module picked up a handful of refinements

- The [`sqlite3`](https://docs.python.org/3.14/library/sqlite3.html#module-sqlite3) module gained a [command-line interface](https://docs.python.org/3.14/library/sqlite3.html#sqlite3-cli)

- Running [`isinstance()`](https://docs.python.org/3.14/library/functions.html#isinstance) tests against [`runtime-checkable protocols`](https://docs.python.org/3.14/library/typing.html#typing.runtime_checkable) is now between two and 20 times faster

- Several performance gains landed in the [`asyncio`](https://docs.python.org/3.14/library/asyncio.html#module-asyncio) package, and a few benchmarks report as much as a 75% speed up.

- The [`uuid`](https://docs.python.org/3.14/library/uuid.html#module-uuid) module gained a [command-line interface](https://docs.python.org/3.14/library/uuid.html#uuid-cli)

[Subject index](INDEX.md) · [Next source section](tokenization-and-library-highlights.md)
