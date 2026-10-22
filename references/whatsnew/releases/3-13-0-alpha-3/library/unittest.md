# Python 3.13.0 alpha 3 / library / unittest

[gh-113661](https://github.com/python/cpython/issues/113661): unittest runner: Avoid exiting 5 when tests got skipped. Exiting 5 was meant to flag situations where the test suite never got discovered. Skipped tests mean discovery did succeed.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
