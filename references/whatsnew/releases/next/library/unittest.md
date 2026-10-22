# Python next / library / unittest

[gh-120665](https://github.com/python/cpython/issues/120665): Corrected a defect under which `unittest` loaders would import then instantiate [`unittest.TestCase`](https://docs.python.org/3.14/library/unittest.html#unittest.TestCase)-derived subclasses that double as abstract base classes, which cannot be instantiated.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
