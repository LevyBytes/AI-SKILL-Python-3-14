# What’s New In Python 3.8 / Notable changes in Python 3.8.3 — __future__

### Notable changes in Python 3.8.3

Within the [`__future__`](https://docs.python.org/3.14/library/__future__.html#module-__future__) module, the constant values assigned to future flags were revised so they no longer collide with compiler flags. Up to that point `PyCF_ALLOW_TOP_LEVEL_AWAIT` had been colliding with `CO_FUTURE_DIVISION`. (The work here came from Batuhan Taskaya under [gh-83743](https://github.com/python/cpython/issues/83743))

[Subject index](INDEX.md) · [Previous source section](notable-changes-in-python-3-8-2.md) · [Next source section](notable-changes-in-python-3-8-8.md) · [Release/subject declaration](assignment-expressions.md)
