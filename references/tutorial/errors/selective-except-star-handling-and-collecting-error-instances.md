# Selective except-star handling and collecting error instances

Swapping in `except*` for `except` lets us handle, on a selective basis, just the exceptions within the group matching a particular type. The example below, which displays a nested exception group, has each `except*` clause pull out of the group the exceptions of one given type while leaving every other exception to travel on to the remaining clauses and ultimately be reraised.

```python
>>> def f():
...     raise ExceptionGroup(
...         "group1",
...         [
...             OSError(1),
...             SystemError(2),
...             ExceptionGroup(
...                 "group2",
...                 [
...                     OSError(3),
...                     RecursionError(4)
...                 ]
...             )
...         ]
...     )
...
>>> try:
...     f()
... except* OSError as e:
...     print("There were OSErrors")
... except* SystemError as e:
...     print("There were SystemErrors")
...
There were OSErrors
There were SystemErrors
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 2, in <module>
  |     f()
  |     ~^^
  |   File "<stdin>", line 2, in f
  |     raise ExceptionGroup(
  |     ...<12 lines>...
  |     )
  | ExceptionGroup: group1 (1 sub-exception)
  +-+---------------- 1 ----------------
    | ExceptionGroup: group2 (1 sub-exception)
    +-+---------------- 1 ----------------
      | RecursionError: 4
      +------------------------------------
>>>

```

Take note that the exceptions tucked inside an exception group have to be instances rather than types. The reason is that these exceptions would normally, in actual use, be ones the program had already raised and caught, following the pattern below:

```python
>>> excs = []
... for test in tests:
...     try:
...         test.run()
...     except Exception as e:
...         excs.append(e)
...
>>> if excs:
...    raise ExceptionGroup("Test Failures", excs)
...

```

[Subject index](INDEX.md) · [Previous source section](constructing-and-catching-exceptiongroup.md) · [Following source section](enriching-exceptions-with-notes.md) · [Related tutorial example and explanation](constructing-and-catching-exceptiongroup.md)
