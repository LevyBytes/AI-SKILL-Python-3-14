# Python 3.13.0 beta 1 / library / pdb

[gh-113081](https://github.com/python/cpython/issues/113081): Renders a colorized exception in [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb), matching the built-in traceback

[gh-83151](https://github.com/python/cpython/issues/83151): The [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) shell now permits arbitrary statements and evaluations to reach the local variables of the current frame, which let multi-scope code such as generators or nested functions function correctly.

[gh-117618](https://github.com/python/cpython/issues/117618): The `break` command of [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) now accepts `package.module` as a `filename`

[gh-118500](https://github.com/python/cpython/issues/118500): Bring [`pdb`](https://docs.python.org/3.14/library/pdb.html#module-pdb) support to zipapps

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
