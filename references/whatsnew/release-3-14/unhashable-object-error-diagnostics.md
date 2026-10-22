# Python 3.14 changes: Unhashable objects and context-manager diagnostics

Better diagnostics now appear when code attempts to insert an instance of an unhashable type into a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) or [`set`](https://docs.python.org/3.14/library/stdtypes.html#set). (Contributed by CF Bolz-Tereick and Victor Stinner in [gh-132828](https://github.com/python/cpython/issues/132828).)

```pycon
>>> s = set()
>>> s.add({'pages': 12, 'grade': 'A'})
Traceback (most recent call last):
  File "<python-input-1>", line 1, in <module>
    s.add({'pages': 12, 'grade': 'A'})
    ~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
TypeError: cannot use 'dict' as a set element (unhashable type: 'dict')
>>> d = {}
>>> l = [1, 2, 3]
>>> d[l] = 12
Traceback (most recent call last):
  File "<python-input-4>", line 1, in <module>
    d[l] = 12
    ~^^^
TypeError: cannot use 'list' as a dict key (unhashable type: 'list')

```

- The error text is also clearer whenever an object implementing the synchronous context manager protocol gets entered through [`async with`](https://docs.python.org/3.14/reference/compound_stmts.html#async-with) rather than [`with`](https://docs.python.org/3.14/reference/compound_stmts.html#with), and the mirror case applies for the asynchronous context manager protocol. (Contributed by Bénédikt Tran in [gh-128398](https://github.com/python/cpython/issues/128398).)

[Subject index](INDEX.md) · [Next source section](pep-784-zstandard-support-in-the-standard-library.md) · [Release/subject declaration](summary-release-highlights.md) · [Release/subject declaration](syntax-error-hints.md) · [Preceding release/subject continuation](invalid-as-target-errors.md)
