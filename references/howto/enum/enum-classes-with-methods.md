# `Enum` classes with methods

### `Enum` classes with methods

When you add extra methods to your enum subclass — as the Planet class does below — those methods appear in a [`dir()`](https://docs.python.org/3.14/library/functions.html#dir) of the member, yet not in one of the class:

```python
>>> dir(Planet)
['EARTH', 'JUPITER', 'MARS', 'MERCURY', 'NEPTUNE', 'SATURN', 'URANUS', 'VENUS', '__class__', '__doc__', '__members__', '__module__']
>>> dir(Planet.EARTH)
['__class__', '__doc__', '__module__', 'mass', 'name', 'radius', 'surface_gravity', 'value']

```

[Subject index](INDEX.md) · [Previous source context](boolean-value-of-enum-classes-and-members.md) · [Following source context](combining-members-of-flag.md)
