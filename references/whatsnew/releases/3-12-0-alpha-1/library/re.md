# Python 3.12.0 alpha 1 / library / re

[gh-91524](https://github.com/python/cpython/issues/91524): Accelerate regular-expression substitution (the [`re.sub()`](https://docs.python.org/3.14/library/re.html#re.sub) and [`re.subn()`](https://docs.python.org/3.14/library/re.html#re.subn) functions plus their matching [`re.Pattern`](https://docs.python.org/3.14/library/re.html#re.Pattern) methods) by a factor of 2–3 for replacement strings that contain group references.

[gh-91404](https://github.com/python/cpython/issues/91404): Roll back the [`re`](https://docs.python.org/3.14/library/re.html#module-re) memory-leak fix that handled a match terminated by a signal or a failed allocation, because that fix introduced a substantial performance regression.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
