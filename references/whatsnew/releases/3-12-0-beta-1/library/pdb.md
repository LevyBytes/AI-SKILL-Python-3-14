# Python 3.12.0 beta 1 / library / pdb

[gh-103143](https://github.com/python/cpython/issues/103143): Refine the help text and docstrings throughout [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb).

[gh-103693](https://github.com/python/cpython/issues/103693): Bring a convenience variable capability to [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb)

[gh-103578](https://github.com/python/cpython/issues/103578): Resolved a defect where [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) crashed while reading a source file under a different encoding, swapping [`io.open()`](https://docs.python.org/3.14/library/io.html#io.open) for [`io.open_code()`](https://docs.python.org/3.14/library/io.html#io.open_code). That fresh method additionally triggers any hook registered through [`PyFile_SetOpenCodeHook()`](https://docs.python.org/3.14/c-api/file.html#c.PyFile_SetOpenCodeHook).

[gh-104301](https://github.com/python/cpython/issues/104301): Permit leading whitespace ahead of disambiguated statements within [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb).

[gh-103225](https://github.com/python/cpython/issues/103225): Repair a defect in [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) affecting how line numbers of module-level source code are shown.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
