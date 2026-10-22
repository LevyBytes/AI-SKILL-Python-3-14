# What’s New in Python 2.6 / PEP 3119: Abstract Base Classes

```python
>>> class Circle(Drawable):
...     pass
...
>>> c = Circle()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't instantiate abstract class Circle with abstract methods draw
>>>

```

The `@abstractproperty` decorator lets you declare abstract data attributes:

```python
from abc import abstractproperty
...

@abstractproperty
def readonly(self):
   return self._x

```

A `readonly` property then has to be defined by subclasses.

See also

[**PEP 3119**](https://peps.python.org/pep-3119/) - Introducing Abstract Base Classes

PEP authored by Guido van Rossum and Talin. Implementation by Guido van Rossum. The 2.6 backport was the work of Benjamin Aranguren, together with Alex Martelli.

[Subject index](INDEX.md) · [Previous source section](abstract-base-class-protocols.md) · [Next source section](pep-3127-integer-literal-support-and-syntax.md) · [Release/subject declaration](python-3-0.md) · [Release/subject declaration](abstract-base-class-protocols.md)
