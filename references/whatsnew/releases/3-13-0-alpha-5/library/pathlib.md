# Python 3.13.0 alpha 5 / library / pathlib

[gh-114610](https://github.com/python/cpython/issues/114610): Resolve a defect in which [`pathlib.PurePath.with_stem()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.with_stem) turned a non-empty suffix into a stem if the *stem* argument it received was empty. The call now produces [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError), mirroring what [`pathlib.PurePath.with_suffix()`](https://docs.python.org/3.14/library/pathlib.html#pathlib.PurePath.with_suffix) raises when invoked on an empty-stem path together with a non-empty *suffix* argument.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
