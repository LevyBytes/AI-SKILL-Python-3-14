# numbers — `numbers` — Numeric abstract base classes

## numbers — Numeric abstract base classes

### `numbers` — Numeric abstract base classes

**Source code:** [Lib/numbers.py](https://github.com/python/cpython/tree/3.14/Lib/numbers.py)

---

Through [**PEP 3141**](https://peps.python.org/pep-3141/), the `numbers` module lays out a tiered set of numeric [abstract base classes](https://docs.python.org/3.14/glossary.html#term-abstract-base-class), each tier adding further operations. The types it declares are not meant to be instantiated.

 *class *numbers.Number

Sits at the top of the numeric hierarchy. To merely test whether some argument *x* is a number of any sort, reach for `isinstance(x, Number)`.

[Subject index](INDEX.md) · [Continue](numbers-complex-class.md)
