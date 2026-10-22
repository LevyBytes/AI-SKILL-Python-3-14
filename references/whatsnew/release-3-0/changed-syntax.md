# What's New In Python 3.0 / Changed Syntax

### Changed Syntax

- [**PEP 3109**](https://peps.python.org/pep-3109/) and [**PEP 3134**](https://peps.python.org/pep-3134/): a fresh [`raise`](https://docs.python.org/3.14/reference/simple_stmts.html#raise) statement syntax: `raise [*expr* [from *expr*]]`. See below.

- The words `as` and [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) are reserved now. (As of 2.6, in fact.)

- The words `True`, `False`, and `None` are reserved. (2.6 already enforced part of the `None` restrictions.)

- Shift from [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) *exc*, *var* to `except` *exc* `as` *var*. See [**PEP 3110**](https://peps.python.org/pep-3110/).

- [**PEP 3115**](https://peps.python.org/pep-3115/): New Metaclass Syntax. In place of:

```python
class C:
    __metaclass__ = M
    ...

```

what you must write now is:

```python
class C(metaclass=M):
    ...

```

The module-global variable `__metaclass__` is no longer honored. (It served as a crutch for defaulting to new-style classes without making every class derive from [`object`](https://docs.python.org/3.14/library/functions.html#object).)

- List comprehensions have dropped the syntactic shape `[... for *var* in *item1*, *item2*, ...]`. Use `[... for *var* in (*item1*, *item2*, ...)]` in its place. Note as well that list comprehensions now carry different semantics: they sit nearer to syntactic sugar for a generator expression nested inside a [`list()`](https://docs.python.org/3.14/library/stdtypes.html#list) constructor, and in particular the loop control variables no longer escape into the enclosing scope.

- The *ellipsis* (`...`) now serves as an atomic expression in any position. (Formerly it was permitted only within slices.) On top of that, the spelling `...` is now mandatory. (Formerly the spelling `. . .` worked too, through a sheer fluke of the grammar.)

[Subject index](INDEX.md) · [Previous source section](new-syntax.md) · [Next source section](removed-syntax.md) · [Release/subject declaration](common-stumbling-blocks.md)
