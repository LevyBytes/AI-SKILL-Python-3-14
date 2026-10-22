# What’s New In Python 3.12 / PEP 688: Making the buffer protocol accessible in Python — collections.abc, inspect

### PEP 688: Making the buffer protocol accessible in Python

A means of reaching the [buffer protocol](https://docs.python.org/3.14/c-api/buffer.html#bufferobjects) straight from Python code is brought in by [**PEP 688**](https://peps.python.org/pep-0688/). Any class defining the [`__buffer__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__buffer__) method now counts as a buffer type.

To represent buffer objects in a uniform fashion — for instance within type annotations — the new [`collections.abc.Buffer`](https://docs.python.org/3.14/library/collections.abc.html#collections.abc.Buffer) ABC is provided. The flags that tune how a buffer is created are captured by the new [`inspect.BufferFlags`](https://docs.python.org/3.14/library/inspect.html#inspect.BufferFlags) enum. (Contributed by Jelle Zijlstra in [gh-102500](https://github.com/python/cpython/issues/102500).)

[Subject index](INDEX.md) · [Previous source section](pep-669-low-impact-monitoring-for-cpython.md) · [Next source section](pep-709-comprehension-inlining.md) · [Release/subject declaration](summary-release-highlights.md)
