# 8.4. Raising Exceptions

### 8.4. Raising Exceptions

By using the [`raise`](https://docs.python.org/3.14/reference/simple_stmts.html#raise) statement, the programmer can compel a chosen exception to be raised. As an example:

```python
>>> raise NameError('HiThere')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    raise NameError('HiThere')
NameError: HiThere

```

What the single argument to [`raise`](https://docs.python.org/3.14/reference/simple_stmts.html#raise) names is the exception you want raised. It has to be either an exception instance or an exception class (one descending from [`BaseException`](https://docs.python.org/3.14/library/exceptions.html#BaseException), like [`Exception`](https://docs.python.org/3.14/library/exceptions.html#Exception) or any of its subclasses). When an exception class is supplied, it gets instantiated for you automatically, its constructor called with no arguments:

```python
raise ValueError  # shorthand for 'raise ValueError()'

```

Should you want to find out whether an exception was raised yet have no plans to deal with it, a more concise variant of the [`raise`](https://docs.python.org/3.14/reference/simple_stmts.html#raise) statement lets you re-raise that exception:

```python
>>> try:
...     raise NameError('HiThere')
... except NameError:
...     print('An exception flew by!')
...     raise
...
An exception flew by!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    raise NameError('HiThere')
NameError: HiThere

```

[Subject index](INDEX.md) · [Previous source section](exception-arguments-reraising-and-else.md) · [Following source section](exception-chaining.md)
