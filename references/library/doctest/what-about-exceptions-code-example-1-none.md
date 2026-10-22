# doctest — What About Exceptions? — Code example: >>> 1 + None

```python
>>> 1 + None
  File "<stdin>", line 1
    1 + None
    ~~^~~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'

```

Because the lines pinpointing the error's location appear ahead of the exception type and detail, doctest does not check them. As an illustration, the test below would still pass, even with the `^` caret planted in the wrong spot:

```python
>>> 1 + None
  File "<stdin>", line 1
    1 + None
    ^~~~~~~~
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'

```

[Subject index](INDEX.md) · [Previous](doctest-exception-testing-overview.md) · [Continue](doctest-dont-accept-true-for-1-to-doctest-fail-fast.md) · [Owning module, declaration or section: doctest](interactive-example-testing-overview.md) · [Owning module, declaration or section: What About Exceptions?](doctest-exception-testing-overview.md)
