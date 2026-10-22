# Python 3.14.2 final / library / dataclasses

[gh-142214](https://github.com/python/cpython/issues/142214): Correct two regressions tied to annotations that landed in [`dataclasses`](https://docs.python.org/3.14/library/dataclasses.html#module-dataclasses) for Python 3.14.1.

  - No exception is thrown anymore when `slots=True` is set yet the `__init__` method lacks an `__annotate__` attribute (most likely because `init=False` was given).

  - No exception is thrown anymore when annotations are asked for on the `__init__` method while one of the fields is absent from the class annotations. Certain dynamic scenarios can trigger this.

Patch by Jelle Zijlstra.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
