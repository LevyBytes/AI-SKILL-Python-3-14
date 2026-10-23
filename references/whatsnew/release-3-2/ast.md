# What's New In Python 3.2 / ast - ast

### ast

A handy general-purpose helper now lives in the [`ast`](https://docs.python.org/3.14/library/ast.html#module-ast) module for safely evaluating expression strings written in Python literal syntax. As a secure stand-in for the readily-misused builtin [`eval()`](https://docs.python.org/3.14/library/functions.html#eval), the [`ast.literal_eval()`](https://docs.python.org/3.14/library/ast.html#ast.literal_eval) function does the job. With Python 3.2, the roster of accepted types grows to include [`bytes`](https://docs.python.org/3.14/library/stdtypes.html#bytes) and [`set`](https://docs.python.org/3.14/library/stdtypes.html#set) literals, joining strings, bytes, numbers, tuples, lists, dicts, sets, booleans, and `None`.

```python
>>> from ast import literal_eval

>>> request = "{'req': 3, 'func': 'pow', 'args': (2, 0.5)}"
>>> literal_eval(request)
{'args': (2, 0.5), 'req': 3, 'func': 'pow'}

>>> request = "os.system('do something harmful')"
>>> literal_eval(request)
Traceback (most recent call last):
  ...
ValueError: malformed node or string: <_ast.Call object at 0x101739a10>

```

(Implemented by Benjamin Peterson and Georg Brandl.)

[Subject index](INDEX.md) · [Previous source section](hashlib.md) · [Next source section](os.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
