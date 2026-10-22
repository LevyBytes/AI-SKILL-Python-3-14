# What's New In Python 3.3 / PEP 409: Suppressing exception context

### PEP 409: Suppressing exception context

New syntax comes with PEP 409 that lets you turn off the display of the chained exception context. This makes for tidier error messages in applications that translate one exception type into another:

```python
>>> class D:
...     def __init__(self, extra):
...         self._extra_attributes = extra
...     def __getattr__(self, attr):
...         try:
...             return self._extra_attributes[attr]
...         except KeyError:
...             raise AttributeError(attr) from None
...
>>> D({}).x
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in __getattr__
AttributeError: x

```

Leave off the `from None` suffix that suppresses the cause, and the original exception would be shown by default:

```python
>>> class C:
...     def __init__(self, extra):
...         self._extra_attributes = extra
...     def __getattr__(self, attr):
...         try:
...             return self._extra_attributes[attr]
...         except KeyError:
...             raise AttributeError(attr)
...
>>> C({}).x
Traceback (most recent call last):
  File "<stdin>", line 6, in __getattr__
KeyError: 'x'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 8, in __getattr__
AttributeError: x

```

Nothing is given up on the debugging front, because the original exception context stays reachable should you need it (say, if some intervening library has wrongly hidden valuable underlying details):

```python
>>> try:
...     D({}).x
... except AttributeError as exc:
...     print(repr(exc.__context__))
...
KeyError('x',)

```

See also

[**PEP 409**](https://peps.python.org/pep-0409/) - Suppressing exception context

PEP written by Ethan Furman; implemented by Ethan Furman and Nick Coghlan.

[Subject index](INDEX.md) · [Previous source section](pep-380-syntax-for-delegating-to-a-subgenerator.md) · [Next source section](pep-414-explicit-unicode-literals.md) · [Release/subject declaration](summary-release-highlights.md)
