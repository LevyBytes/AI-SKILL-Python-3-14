# Python 3.14.3 final / tests / build and platforms

[gh-144415](https://github.com/python/cpython/issues/144415): The Android testbed now tells apart stdout/stderr messages produced by a newline from those produced by an explicit `flush` call. This corrects how progress indicators and similar output get logged.

[gh-142836](https://github.com/python/cpython/issues/142836): `test_pdb.test_script_target_anonymous_pipe` was adjusted to handle Solaris.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
