# Constructing and catching ExceptionGroup

### 8.9. Raising and Handling Multiple Unrelated Exceptions

Cases come up where you have to report several exceptions that took place. This frequently happens in concurrency frameworks, where multiple tasks might have failed side by side, but there are further scenarios too where you'd rather keep running and gather up a batch of errors than throw the very first exception.

The builtin [`ExceptionGroup`](https://docs.python.org/3.14/library/exceptions.html#ExceptionGroup) bundles a list of exception instances together so they can be raised as a group. Being an exception in its own right, it can be caught just like any other exception.

```python
>>> def f():
...     excs = [OSError('error 1'), SystemError('error 2')]
...     raise ExceptionGroup('there were problems', excs)
...
>>> f()
  + Exception Group Traceback (most recent call last):
  |   File "<stdin>", line 1, in <module>
  |     f()
  |     ~^^
  |   File "<stdin>", line 3, in f
  |     raise ExceptionGroup('there were problems', excs)
  | ExceptionGroup: there were problems (2 sub-exceptions)
  +-+---------------- 1 ----------------
    | OSError: error 1
    +---------------- 2 ----------------
    | SystemError: error 2
    +------------------------------------
>>> try:
...     f()
... except Exception as e:
...     print(f'caught {type(e)}: {e}')
...
caught <class 'ExceptionGroup'>: there were problems (2 sub-exceptions)
>>>

```

[Subject index](INDEX.md) · [Previous source section](predefined-clean-up-actions.md) · [Following source section](selective-except-star-handling-and-collecting-error-instances.md) · [Related tutorial example and explanation](selective-except-star-handling-and-collecting-error-instances.md)
