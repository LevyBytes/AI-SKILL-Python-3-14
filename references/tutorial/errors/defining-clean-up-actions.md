# 8.7. Defining Clean-up Actions

### 8.7. Defining Clean-up Actions

The [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) statement carries yet another optional clause whose purpose is to spell out clean-up actions that have to run no matter what. As an example:

```python
>>> try:
...     raise KeyboardInterrupt
... finally:
...     print('Goodbye, world!')
...
Goodbye, world!
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    raise KeyboardInterrupt
KeyboardInterrupt

```

Whenever a [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) clause is there, the `finally` clause runs as the final action right before the [`try`](https://docs.python.org/3.14/reference/compound_stmts.html#try) statement finishes. The `finally` clause executes regardless of whether the `try` statement throws an exception. The bullet points below go over the trickier scenarios that arise when an exception shows up:

- Should an exception arise while the `try` clause runs, an [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) clause may take care of it. When no `except` clause handles the exception, it is re-raised once the `finally` clause has finished running.

- It's possible for an exception to arise while an `except` or `else` clause runs. Once more, that exception is re-raised after the `finally` clause has finished running.

- When the `finally` clause runs a [`break`](https://docs.python.org/3.14/reference/simple_stmts.html#break), [`continue`](https://docs.python.org/3.14/reference/simple_stmts.html#continue) or [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return) statement, exceptions don't get re-raised. Because this can be puzzling, it's discouraged. Starting with version 3.14 the compiler raises a [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning) for it (refer to [**PEP 765**](https://peps.python.org/pep-0765/)).

- When the `try` statement hits a [`break`](https://docs.python.org/3.14/reference/simple_stmts.html#break), [`continue`](https://docs.python.org/3.14/reference/simple_stmts.html#continue) or [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return) statement, the `finally` clause runs right before that `break`, `continue` or `return` statement executes.

- When a `finally` clause carries a `return` statement, the value handed back will be the one coming from the `finally` clause's `return` statement, rather than the value from the `try` clause's `return` statement. Because this can be puzzling, it's discouraged. Starting with version 3.14 the compiler raises a [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning) for it (refer to [**PEP 765**](https://peps.python.org/pep-0765/)).

As an example:

```python
>>> def bool_return():
...     try:
...         return True
...     finally:
...         return False
...
>>> bool_return()
False

```

A more involved example:

```python
>>> def divide(x, y):
...     try:
...         result = x / y
...     except ZeroDivisionError:
...         print("division by zero!")
...     else:
...         print("result is", result)
...     finally:
...         print("executing finally clause")
...
>>> divide(2, 1)
result is 2.0
executing finally clause
>>> divide(2, 0)
division by zero!
executing finally clause
>>> divide("2", "1")
executing finally clause
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    divide("2", "1")
    ~~~~~~^^^^^^^^^^
  File "<stdin>", line 3, in divide
    result = x / y
             ~~^~~
TypeError: unsupported operand type(s) for /: 'str' and 'str'

```

As is evident, the [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) clause runs no matter what. The [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) that arises from dividing one string by another goes uncaught by the [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) clause and is thus re-raised once the `finally` clause has finished running.

Out in real-world software, the [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) clause earns its keep by freeing external resources (files or network connections, say), whether or not the resource was used successfully.

[Subject index](INDEX.md) · [Previous source section](user-defined-exceptions.md) · [Following source section](predefined-clean-up-actions.md)
