# Python 3.14.1 final / library / exceptions

[gh-138859](https://github.com/python/cpython/issues/138859): Stops generic type parameterization from raising a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) when a `ParamSpec` whose default is not a list of types is left out.

[gh-140633](https://github.com/python/cpython/issues/140633): While loading an extension module that ships as an Apple Framework, any [`AttributeError`](https://docs.python.org/3.14/library/exceptions.html#AttributeError) raised when assigning a module's `__file__` attribute is now ignored.

[gh-140938](https://github.com/python/cpython/issues/140938): An infinity or a NaN among the inputs now triggers a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) from the [`statistics.stdev()`](https://docs.python.org/3.14/library/statistics.html#statistics.stdev) and [`statistics.pstdev()`](https://docs.python.org/3.14/library/statistics.html#statistics.pstdev) functions.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
