# simple statements: Suppressing exception chaining and traceback changes

```pycon
>>> try:
...     print(1 / 0)
... except:
...     raise RuntimeError("Something bad happened")
...
Traceback (most recent call last):
  File "<stdin>", line 2, in <module>
    print(1 / 0)
          ~~^~~
ZeroDivisionError: division by zero

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
    raise RuntimeError("Something bad happened")
RuntimeError: Something bad happened

```

You shut off exception chaining outright by writing [`None`](https://docs.python.org/3.14/library/constants.html#None) into the `from` clause:

```pycon
>>> try:
...     print(1 / 0)
... except:
...     raise RuntimeError("Something bad happened") from None
...
Traceback (most recent call last):
  File "<stdin>", line 4, in <module>
RuntimeError: Something bad happened

```

You will find more on exceptions over in the [Exceptions](https://docs.python.org/3.14/reference/executionmodel.html#exceptions) section, while coverage of how to handle them sits in the [The try statement](https://docs.python.org/3.14/reference/compound_stmts.html#try) section.

Changed in version 3.3: Supplying [`None`](https://docs.python.org/3.14/library/constants.html#None) as `Y` within `raise X from Y` is now allowed.

The [`__suppress_context__`](https://docs.python.org/3.14/library/exceptions.html#BaseException.__suppress_context__) attribute was added so the exception context's automatic display can be turned off.

Changed in version 3.11: Where the active exception's traceback gets altered inside an [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) clause, any later `raise` statement re-raises that exception carrying the altered traceback. Formerly, re-raising used the traceback the exception held at the moment it was caught.

[Subject index](INDEX.md) · [Owning language section](simple-statements.md) · [Owning language section](raise-statement.md) · [Previous source contract continuation](raise-statement.md) · [Following source section](the-break-statement.md)
