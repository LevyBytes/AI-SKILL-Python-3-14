# What's New In Python 3.7 / dataclasses - dataclasses

### dataclasses

A fresh [`dataclass()`](https://docs.python.org/3.14/library/dataclasses.html#dataclasses.dataclass) decorator gives you a means to define *data classes*. Such a class spells out its fields through class-variable annotations. The decorator builds its constructor along with other dunder methods automatically, including [`__repr__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__repr__), [`__eq__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__eq__), and [`__hash__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__hash__).

Example:

```python
@dataclass
class Point:
    x: float
    y: float
    z: float = 0.0

p = Point(1.5, 2.5)
print(p)   # produces "Point(x=1.5, y=2.5, z=0.0)"

```

See also

[**PEP 557**](https://peps.python.org/pep-0557/) ? Data Classes

PEP written and implemented by Eric V. Smith

[Subject index](INDEX.md) · [Previous source section](contextvars.md) · [Next source section](importlib-resources.md) · [Release/subject declaration](summary-release-highlights.md)
