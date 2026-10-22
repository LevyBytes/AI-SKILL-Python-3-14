# Python 3.13.0 alpha 4 / library / functions and types

[gh-112903](https://github.com/python/cpython/issues/112903): Repair the ?issubclass() arg 1 must be a class? errors that arose in some multiple-inheritance scenarios involving generic aliases (a regression from the early 3.13 alpha releases).

[gh-113267](https://github.com/python/cpython/issues/113267): Undo the modifications from [gh-106584](https://github.com/python/cpython/issues/106584) that had left the `TestResult` methods `startTest()` and `stopTest()` out of balance.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
