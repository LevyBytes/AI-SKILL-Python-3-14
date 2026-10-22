# __import__(‘x.y.z’) returns <module ‘x’>; how do I get z?

### __import__(‘x.y.z’) returns <module ‘x’>; how do I get z?

A better option is to reach for the handy [`import_module()`](https://docs.python.org/3.14/library/importlib.html#importlib.import_module) helper that [`importlib`](https://docs.python.org/3.14/library/importlib.html#module-importlib) provides:

```python
z = importlib.import_module('x.y.z')

```

[Subject index](INDEX.md)
