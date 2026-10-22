# typing — `typing` — Support for type hints

### `typing` — Support for type hints

Added in version 3.5.

**Source code:** [Lib/typing.py](https://github.com/python/cpython/tree/3.14/Lib/typing.py)

Note

Type annotations on functions and variables are never checked by the Python runtime itself. Their value is to outside tooling — [type checkers](https://docs.python.org/3.14/glossary.html#term-static-type-checker), editors, linters, and so on.

---

What this module supplies is runtime machinery backing type hints.

Take the following function as an illustration:

```python
def surface_area_of_cube(edge_length: float) -> str:
    return f"The surface area of the cube is {6 * edge_length ** 2}."

```

Here `surface_area_of_cube` expects its argument to be a [`float`](https://docs.python.org/3.14/library/functions.html#float) instance — that is what the [type hint](https://docs.python.org/3.14/glossary.html#term-type-hint) `edge_length: float` conveys. Its return value is meant to be a [`str`](https://docs.python.org/3.14/library/stdtypes.html#str) instance, which the `-> str` hint records.

Hints can be plain classes such as [`float`](https://docs.python.org/3.14/library/functions.html#float) or [`str`](https://docs.python.org/3.14/library/stdtypes.html#str), yet they may go well beyond that. A richer vocabulary of type hints comes from the `typing` module.

The `typing` module gains new capabilities on a regular basis. To carry those additions back to earlier Python releases, reach for the [typing_extensions](https://pypi.org/project/typing_extensions/) package, which ships backports of them.

See also

[Typing cheat sheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)

A quick overview of type hints (hosted at the mypy docs)

Type System Reference section of [the mypy docs](https://mypy.readthedocs.io/en/stable/index.html)

Because PEPs standardise Python's typing system, this material should hold for most Python type checkers in general. (A few pieces could remain mypy-only.)

[Static Typing with Python](https://typing.python.org/en/latest/)

Community-authored, checker-agnostic documentation covering type system features, handy typing tooling, and recommended typing practices.

[Subject index](INDEX.md) · [Continue](specification-for-the-python-type-system.md)
