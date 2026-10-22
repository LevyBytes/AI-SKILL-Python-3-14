# What's New In Python 3.3 / PEP 3155: Qualified name for classes and functions

### PEP 3155: Qualified name for classes and functions

A fresh [`__qualname__`](https://docs.python.org/3.14/library/stdtypes.html#definition.__qualname__) attribute on function and class objects captures the ?path? running from the module top-level down to where they are defined. With global functions and classes this matches [`__name__`](https://docs.python.org/3.14/library/stdtypes.html#definition.__name__). For the rest, it conveys better detail about where they were truly defined and how the global scope might reach them.

Example with (non-bound) methods:

```python
>>> class C:
...     def meth(self):
...         pass
...
>>> C.meth.__name__
'meth'
>>> C.meth.__qualname__
'C.meth'

```

Example with nested classes:

```python
>>> class C:
...     class D:
...         def meth(self):
...             pass
...
>>> C.D.__name__
'D'
>>> C.D.__qualname__
'C.D'
>>> C.D.meth.__name__
'meth'
>>> C.D.meth.__qualname__
'C.D.meth'

```

Example with nested functions:

```python
>>> def outer():
...     def inner():
...         pass
...     return inner
...
>>> outer().__name__
'inner'
>>> outer().__qualname__
'outer.<locals>.inner'

```

How these objects render as strings is likewise updated to carry the new, sharper information:

```python
>>> str(C.D)
"<class '__main__.C.D'>"
>>> str(C.D.meth)
'<function C.D.meth at 0x7f46b9fe31e0>'

```

See also

[**PEP 3155**](https://peps.python.org/pep-3155/) - Qualified name for classes and functions

PEP written and implemented by Antoine Pitrou.

[Subject index](INDEX.md) · [Previous source section](pep-414-explicit-unicode-literals.md) · [Next source section](pep-412-key-sharing-dictionary.md) · [Release/subject declaration](summary-release-highlights.md)
