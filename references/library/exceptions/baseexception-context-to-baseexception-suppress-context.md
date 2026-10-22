# Exception context

### Exception context

Exception objects carry three attributes that describe the surrounding circumstances under which the exception came to be raised:

 BaseException.__context__

 BaseException.__cause__

 BaseException.__suppress_context__

Should a fresh exception get raised while a previous one is still being dealt with, the `__context__` attribute on the new exception is set, without intervention, to that exception being dealt with. Handling of an exception happens when an [`except`](https://docs.python.org/3.14/reference/compound_stmts.html#except) or [`finally`](https://docs.python.org/3.14/reference/compound_stmts.html#finally) clause, or alternatively a [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with) statement, comes into play.

You can augment this implicit exception context with an explicit cause by pairing `from` with [`raise`](https://docs.python.org/3.14/reference/simple_stmts.html#raise):

```python
raise new_exc from original_exc

```

Whatever expression comes after [`from`](https://docs.python.org/3.14/reference/simple_stmts.html#raise) has to be either an exception or `None`. That expression becomes the `__cause__` on the exception being raised. Assigning `__cause__` also turns the `__suppress_context__` attribute to `True` as a side effect, which means writing `raise new_exc from None` will, for display purposes, swap the old exception out in favor of the new one (say, turning a `KeyError` into an `AttributeError`), all while keeping the old exception reachable in `__context__` so it can be inspected during debugging.

Alongside the traceback for the exception proper, the default traceback display code renders these chained exceptions too. Whenever an exception is explicitly chained in `__cause__`, it is always displayed. By contrast, an exception implicitly chained in `__context__` appears only when `__cause__` equals [`None`](https://docs.python.org/3.14/library/constants.html#None) and `__suppress_context__` is false.

Either way, the exception proper is invariably displayed following any chained exceptions, ensuring the traceback's last line always reports the exception that was most recently raised.

[Subject index](INDEX.md) · [Previous](built-in-exceptions.md) · [Continue](inheriting-from-built-in-exceptions.md)
