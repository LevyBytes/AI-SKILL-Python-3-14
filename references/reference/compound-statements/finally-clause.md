# 8.4.4. `finally` clause

### 8.4.4. `finally` clause

When `finally` appears, it designates a ‘cleanup’ handler. The `try` clause runs, taking in any `except` and `else` clauses. Should an exception arise in any of those clauses and go unhandled, the exception is set aside for the moment. The `finally` clause then runs. If an exception was set aside, it gets re-raised once the `finally` clause finishes. Should the `finally` clause raise its own exception, the set-aside exception becomes the context of the fresh one. Should the `finally` clause run a [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return), [`break`](https://docs.python.org/3.14/reference/simple_stmts.html#break) or [`continue`](https://docs.python.org/3.14/reference/simple_stmts.html#continue) statement, the set-aside exception is thrown away. As an illustration, the function below returns 42.

```python
def f():
    try:
        1/0
    finally:
        return 42

```

While the `finally` clause runs, the exception information is not accessible to the program.

Whenever a [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return), [`break`](https://docs.python.org/3.14/reference/simple_stmts.html#break) or [`continue`](https://docs.python.org/3.14/reference/simple_stmts.html#continue) statement runs inside the `try` suite of a `try`…`finally` statement, the `finally` clause runs as well ‘on the way out.’

The value a function returns is set by the final [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return) statement that ran. Because the `finally` clause always runs, a `return` statement that runs inside the `finally` clause will invariably be the last to run. The function that follows returns ‘finally’.

```python
def foo():
    try:
        return 'try'
    finally:
        return 'finally'

```

Changed in version 3.8: An implementation issue meant that, before Python 3.8, placing a [`continue`](https://docs.python.org/3.14/reference/simple_stmts.html#continue) statement within the `finally` clause was not permitted.

Changed in version 3.14: Should a [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return), [`break`](https://docs.python.org/3.14/reference/simple_stmts.html#break) or [`continue`](https://docs.python.org/3.14/reference/simple_stmts.html#continue) turn up inside a `finally` block, the compiler now produces a [`SyntaxWarning`](https://docs.python.org/3.14/library/exceptions.html#SyntaxWarning) (see [**PEP 765**](https://peps.python.org/pep-0765/)).

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](the-try-statement.md) · [Previous source section](else-clause.md) · [Following source section](the-with-statement-suite-to-raise.md)
