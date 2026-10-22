# Duplicating enum members and values

### Duplicating enum members and values

Declaring two enum members under one shared name is not permitted:

```python
>>> class Shape(Enum):
...     SQUARE = 2
...     SQUARE = 3
...
Traceback (most recent call last):
...
TypeError: 'SQUARE' already defined as 2

```

That said, a single enum member may be reachable under additional names. Suppose two entries `A` and `B` share a value, with `A` declared earlier; then `B` becomes an alias of member `A`. Looking up the value of `A` returns member `A`. A by-name lookup of `A` yields member `A`. And a by-name lookup of `B` likewise yields member `A`:

```python
>>> class Shape(Enum):
...     SQUARE = 2
...     DIAMOND = 1
...     CIRCLE = 3
...     ALIAS_FOR_SQUARE = 2
...
>>> Shape.SQUARE
<Shape.SQUARE: 2>
>>> Shape.ALIAS_FOR_SQUARE
<Shape.SQUARE: 2>
>>> Shape(2)
<Shape.SQUARE: 2>

```

Note

You may not declare a member sharing a name with an attribute that already exists (a different member, a method, and so on), nor declare an attribute sharing a name with an existing member.

[Subject index](INDEX.md) · [Previous source context](enum-member-and-attribute-access.md) · [Following source context](ensuring-unique-enumeration-values.md)
