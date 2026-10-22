# 8.5. Exception Chaining

### 8.5. Exception Chaining

Whenever an unhandled exception crops up within an [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) section, the exception currently being handled gets attached to it and folded into the error message:

```python
>>> try:
...     open("database.sqlite")
... except OSError:
...     raise RuntimeError("unable to handle error")
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    open("database.sqlite")
    ~~~~^^^^^^^^^^^^^^^^^^^
FileNotFoundError: [Errno 2] No such file or directory: 'database.sqlite'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError("unable to handle error")
RuntimeError: unable to handle error

```

So as to mark one exception as a straight outcome of another, an optional `from` clause is permitted on the [`raise`](https://docs.python.org/3.14/reference/simple_stmts.html#raise) statement:

```python
# exc must be exception instance or None.
raise RuntimeError from exc

```

This proves handy whenever you're translating one exception into another. As an example:

```python
>>> def func():
...     raise ConnectionError
...
>>> try:
...     func()
... except ConnectionError as exc:
...     raise RuntimeError('Failed to open database') from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    func()
    ~~~~^^
  File "<stdin>", line 2, in func
ConnectionError

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError('Failed to open database') from exc
RuntimeError: Failed to open database

```

On top of that, the automatic chaining of exceptions can be switched off through the `from None` idiom:

```python
>>> try:
...     open('database.sqlite')
... except OSError:
...     raise RuntimeError from None
...
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError from None
RuntimeError

```

To read further on how chaining works, consult [Built-in Exceptions](https://docs.python.org/3.14/library/exceptions.html#bltin-exceptions).

[Subject index](INDEX.md) · [Previous source section](raising-exceptions.md) · [Following source section](user-defined-exceptions.md)
