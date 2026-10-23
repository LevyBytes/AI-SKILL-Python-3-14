# What's New In Python 3.13 / ctypes - ctypes

### ctypes

- Owing to required internal refactoring, the internal metaclasses now run their setup inside `__init__` instead of within `__new__`. Projects subclassing these internal metaclasses for custom initialization feel the effect. As a rule:

  - Whatever custom logic ran in `__new__` following the `super().__new__` call ought to migrate into `__init__`.

  - When making a class, invoke the metaclass itself, not merely the metaclass's `__new__` method.

Consult [gh-124520](https://github.com/python/cpython/issues/124520) for the discussion plus links to the modifications across several affected projects.

- [`ctypes.Structure`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure) objects carry a fresh [`_align_`](https://docs.python.org/3.14/library/ctypes.html#ctypes.Structure._align_) attribute letting you state outright the alignment used as the structure is packed into or out of memory. (Contributed by Matt Sanderson in [gh-112433](https://github.com/python/cpython/issues/112433))

[Subject index](INDEX.md) · [Previous source section](copy.md) · [Next source section](dbm.md) · [Release/subject declaration](summary-release-highlights.md)
