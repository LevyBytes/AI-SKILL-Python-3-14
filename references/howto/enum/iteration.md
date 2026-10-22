# Iteration

### Iteration

Walking the members of an enum leaves the aliases out:

```python
>>> list(Shape)
[<Shape.SQUARE: 2>, <Shape.DIAMOND: 1>, <Shape.CIRCLE: 3>]
>>> list(Weekday)
[<Weekday.MONDAY: 1>, <Weekday.TUESDAY: 2>, <Weekday.WEDNESDAY: 4>, <Weekday.THURSDAY: 8>, <Weekday.FRIDAY: 16>, <Weekday.SATURDAY: 32>, <Weekday.SUNDAY: 64>]

```

Observe that the aliases `Shape.ALIAS_FOR_SQUARE` and `Weekday.WEEKEND` are absent.

The special `__members__` attribute is a read-only ordered mapping from names to members. Every name declared in the enumeration appears there, the aliases included:

```python
>>> for name, member in Shape.__members__.items():
...     name, member
...
('SQUARE', <Shape.SQUARE: 2>)
('DIAMOND', <Shape.DIAMOND: 1>)
('CIRCLE', <Shape.CIRCLE: 3>)
('ALIAS_FOR_SQUARE', <Shape.SQUARE: 2>)

```

The `__members__` attribute lends itself to fine-grained programmatic inspection of the enumeration members. As one example, locating every alias:

```python
>>> [name for name, member in Shape.__members__.items() if member.name != name]
['ALIAS_FOR_SQUARE']

```

Note

For flags, aliases cover values with several flags turned on, like `3`, as well as the no-flags case, that is `0`.

[Subject index](INDEX.md) · [Previous source context](using-automatic-values.md) · [Following source context](comparisons.md)
