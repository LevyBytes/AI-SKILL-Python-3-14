# Python 3.12.0 beta 1 / library / pathlib

[gh-81079](https://github.com/python/cpython/issues/81079): Provide a *case_sensitive* keyword-only argument on [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) and [`rglob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.rglob).

[gh-101362](https://github.com/python/cpython/issues/101362): Accelerate [`pathlib.Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path) construction by leaving the path anchor out of the internal list of path parts.

[gh-78079](https://github.com/python/cpython/issues/78079): Correct the faulty normalization of UNC device path roots, together with partial UNC share path roots, inside [`pathlib.PurePath`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath). Such paths no longer receive a trailing slash from Pathlib.

[bpo-45606](https://bugs.python.org/issue?@action=redirect&bpo=45606): Corrected a flaw in [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) – formerly an exact-match pattern would skip over a dangling symlink, whereas a pattern carrying a wildcard or the recursive wildcard (`**`) would still locate it. After this fix, both kinds of pattern locate a dangling symlink.

[gh-103548](https://github.com/python/cpython/issues/103548): Boost the speed of [`pathlib.Path.absolute()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.absolute) and [`cwd()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.cwd) by combining paths solely where required. The throughput of [`pathlib.PurePath.is_absolute()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.is_absolute) on Posix also rises through bypassing path parsing and normalization.

[gh-103525](https://github.com/python/cpython/issues/103525): Repair the confusing exception text raised when mixed `str` and `bytes` arguments reach [`pathlib.PurePath`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath) and [`Path`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path).

[gh-104484](https://github.com/python/cpython/issues/104484): Add a *case_sensitive* argument to [`pathlib.PurePath.match()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.match)

[gh-102613](https://github.com/python/cpython/issues/102613): Correct a problem where [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) threw [`RecursionError`](https://docs.python.org/3.14/library/exceptions.html#RecursionError) while traversing deeply nested directory trees.

[gh-87695](https://github.com/python/cpython/issues/87695): Correct a problem where [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) threw [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) upon meeting a symlink pointing at an excessively long path.

[gh-102613](https://github.com/python/cpython/issues/102613): Speed up [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) during recursive wildcard ("`**`") expansion by combining neighboring wildcards and de-duplicating results only where it is needed.

[gh-100479](https://github.com/python/cpython/issues/100479): Introduce [`pathlib.PurePath.with_segments()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.with_segments), which builds a path object out of arguments. Every time a derivative path comes into being — for example via [`pathlib.PurePath.parent`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.parent) — this method gets invoked. Subclasses are free to override it to pass information between path objects.

[gh-90208](https://github.com/python/cpython/issues/90208): Corrected a problem where [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) gave back incomplete results after running into a [`PermissionError`](https://docs.python.org/3.14/library/exceptions.html#PermissionError). The method now swallows every [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError), apart from those that arise from calling [`is_dir()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.is_dir) on the top-level path.

[gh-104114](https://github.com/python/cpython/issues/104114): Correct a problem where [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) yields paths that take the case of non-wildcard segments for the matching path segments, instead of the actual filesystem case.

[gh-104104](https://github.com/python/cpython/issues/104104): Boost [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) performance by employing [`re.IGNORECASE`](https://docs.python.org/3.14/library/re.html#re.IGNORECASE) for case-insensitive matching.

[gh-104102](https://github.com/python/cpython/issues/104102): Boost [`pathlib.Path.glob()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.Path.glob) performance while evaluating patterns containing `'../'` segments.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
