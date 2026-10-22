# Python 3.13.0 alpha 1 / core and builtins / doctest

[gh-81283](https://github.com/python/cpython/issues/81283): The compiler henceforth trims indentation out of docstrings. For a module with heavy documentation this shrinks the `pyc` file by 5%. Because the change touches `__doc__`, utilities such as doctest will feel the effect.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
