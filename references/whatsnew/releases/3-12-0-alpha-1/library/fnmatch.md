# Python 3.12.0 alpha 1 / library / fnmatch

[gh-89973](https://github.com/python/cpython/issues/89973): Quash the `re.error` thrown inside [`fnmatch`](https://docs.python.org/3.14/library/fnmatch.html#module-fnmatch) whenever a pattern holds a character range whose upper bound sits below its lower bound (`[c-a]`, say). Such ranges are now treated as empty ones.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
