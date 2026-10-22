# Python 3.12.0 alpha 4 / library / datetime

[gh-85432](https://github.com/python/cpython/issues/85432): In the pure-Python [`datetime.time.strftime()`](https://docs.python.org/3.14/library/datetime.html#datetime.time.strftime), rename the *fmt* parameter to *format*. Rename the *t* parameter of [`datetime.datetime.fromtimestamp()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.fromtimestamp) to *timestamp*. After these renames the pure-Python parameter names line up with those of the C implementation. Alex Waygood wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
