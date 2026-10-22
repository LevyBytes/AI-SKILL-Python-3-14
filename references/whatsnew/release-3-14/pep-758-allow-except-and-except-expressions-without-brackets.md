# What's new in Python 3.14 / PEP 758: Allow `except` and `except*` expressions without brackets

### PEP 758: Allow `except` and `except*` expressions without brackets

Brackets may now be left off the [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) and [`except*`](https://docs.python.org/3.14/reference/compound_stmts.html#except-star) expressions when multiple exception types are present and no `as` clause appears. As an example:

```python
try:
    connect_to_server()
except TimeoutError, ConnectionRefusedError:
    print('The network has ceased to be!')

```

(Contributed by Pablo Galindo and Brett Cannon in [**PEP 758**](https://peps.python.org/pep-0758/) and [gh-131831](https://github.com/python/cpython/issues/131831).)

[Subject index](INDEX.md) · [Previous source section](command-line-and-environment.md) · [Next source section](pep-765-control-flow-in-finally-blocks.md) · [Release/subject declaration](summary-release-highlights.md)
