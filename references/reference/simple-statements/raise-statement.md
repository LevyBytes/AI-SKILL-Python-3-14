# simple statements: Raising, reraising and explicitly chaining exceptions

### 7.8. The `raise` statement

```text

raise_stmt: "raise" [expression "from" [expression]]
```

When no expressions appear, `raise` re-raises whichever exception is presently being handled, otherwise known as the *active exception*. Should no active exception currently exist, a [`RuntimeError`](https://docs.python.org/3.14/library/exceptions.html#RuntimeError) exception is raised to signal that this is an error.

Otherwise, `raise` evaluates the first expression to obtain the exception object. That object has to be either a subclass or an instance of [`BaseException`](https://docs.python.org/3.14/library/exceptions.html#BaseException). When it is a class, the exception instance gets produced as needed by instantiating that class with no arguments.

The *type* of the exception is the class of the exception instance, while the *value* is the instance itself.

Ordinarily a traceback object is built automatically the moment an exception is raised and is attached to it as the [`__traceback__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__traceback__) attribute. You may build an exception and supply your own traceback in a single step using the [`with_traceback()`](https://docs.python.org/3.14/library/exceptions.html#BaseException.with_traceback) exception method (which gives back the very same exception instance, its traceback set to the argument), as in:

```python
raise Exception("foo occurred").with_traceback(tracebackobj)

```

The `from` clause exists for exception chaining: when supplied, the second *expression* must be another exception class or instance. When the second expression is an exception instance, it gets attached to the raised exception as the [`__cause__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__cause__) attribute (which is writable). When the expression is an exception class, that class gets instantiated and the resulting exception instance gets attached to the raised exception as the `__cause__` attribute. Should the raised exception go unhandled, both exceptions get printed:

```pycon
>>> try:
...     print(1 / 0)
... except Exception as exc:
...     raise RuntimeError("Something bad happened") from exc
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    print(1 / 0)
          ~~^~~
ZeroDivisionError: division by zero

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError("Something bad happened") from exc
RuntimeError: Something bad happened

```

A comparable mechanism kicks in implicitly whenever a fresh exception is raised while an exception is already being handled. An exception may be handled inside an [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) or [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) clause, or inside a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement. The earlier exception then gets attached as the new exception's [`__context__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__context__) attribute:

[Subject index](INDEX.md) · [Owning language section](simple-statements.md) · [Following source contract continuation](raise-and-implicit-exception-chaining.md) · [Previous source section](the-yield-statement.md)
