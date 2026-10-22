# 8.4.2. `except*` clause

### 8.4.2. `except*` clause

One or more handlers for groups of exceptions ([`BaseExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#BaseExceptionGroup) instances) are named by the `except*` clause(s). Within a single `try` statement you may use either `except` or `except*` clauses, never a mix of both. With `except*`, the exception type used for matching is required, so `except*:` is a syntax error. That type is read the same way it is for `except`, but the matching applies to the exceptions held inside the group currently being handled. A [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised should a matching type be a subclass of `BaseExceptionGroup`, since the semantics there would be ambiguous.

Whenever an exception group is raised inside the try block, every `except*` clause splits (see [`split()`](https://docs.python.org/3.14/library/exceptions.html#BaseExceptionGroup.split)) it into the matching and non-matching subgroups. Should the matching subgroup be non-empty, it turns into the handled exception (the value [`sys.exception()`](https://docs.python.org/3.14/library/sys.html#sys.exception) returns) and is bound to the target of the `except*` clause (if one is given). The body of the `except*` clause then runs. Should the non-matching subgroup be non-empty, the next `except*` handles it the same way. This carries on until every exception in the group has been matched, or until the final `except*` clause has run.

Once all the `except*` clauses have run, the group of exceptions left unhandled is combined with whatever exceptions were raised or re-raised from inside the `except*` clauses. That combined exception group then propagates onward.:

```python
>>> try:
...     raise ExceptionGroup("eg",
...         [ValueError(1), TypeError(2), OSError(3), OSError(4)])
... except* TypeError as e:
...     print(f'caught {type(e)} with nested {e.exceptions}')
... except* OSError as e:
...     print(f'caught {type(e)} with nested {e.exceptions}')
...
caught <class 'ExceptionGroup'> with nested (TypeError(2),)
caught <class 'ExceptionGroup'> with nested (OSError(3), OSError(4))
  + Exception Group Traceback (most recent call last):
  |   File "<doctest default[0]>", line 2, in <module>
  |     raise ExceptionGroup("eg",
  |         [ValueError(1), TypeError(2), OSError(3), OSError(4)])
  | ExceptionGroup: eg (1 sub-exception)
  +-+---------------- 1 ----------------
    | ValueError: 1
    +------------------------------------

```

Should the exception raised by the `try` block not be an exception group while its type still fits one of the `except*` clauses, it gets caught and wrapped inside an exception group bearing an empty message string. This keeps the type of the target `e` reliably [`BaseExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#BaseExceptionGroup):

```python
>>> try:
...     raise BlockingIOError
... except* BlockingIOError as e:
...     print(repr(e))
...
ExceptionGroup('', (BlockingIOError(),))

```

[`break`](https://docs.python.org/3.14/reference/simple_stmts.html#break), [`continue`](https://docs.python.org/3.14/reference/simple_stmts.html#continue) and [`return`](https://docs.python.org/3.14/reference/simple_stmts.html#return) cannot appear in an `except*` clause.

[Subject index](INDEX.md) · [Owning language section](compound-statements.md) · [Owning language section](the-try-statement.md) · [Previous source section](except-clause-foo-to-foo.md) · [Following source section](else-clause.md)
