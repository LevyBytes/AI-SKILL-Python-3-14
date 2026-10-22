# Enum creation, names, values and member types

### Enum HOWTO

An [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) groups symbolic names that each map to a distinct value. While they resemble global variables, they add a friendlier [`repr()`](https://docs.python.org/3.14/library/functions.html#repr), the ability to group related names, type-safety, and several extra conveniences.

Their sweet spot is a variable restricted to one of a small, fixed set of choices. Take the days of the week as an illustration:

```python
>>> from enum import Enum
>>> class Weekday(Enum):
...     MONDAY = 1
...     TUESDAY = 2
...     WEDNESDAY = 3
...     THURSDAY = 4
...     FRIDAY = 5
...     SATURDAY = 6
...     SUNDAY = 7

```

Alternatively, consider the RGB primary colors:

```python
>>> from enum import Enum
>>> class Color(Enum):
...     RED = 1
...     GREEN = 2
...     BLUE = 3

```

As shown, building an [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) just means declaring a class that derives from `Enum` directly.

Note

Case of Enum Members

Since Enums stand in for constants, and to sidestep collisions between enum names and the methods or attributes pulled in from mixin classes, the strong recommendation is to name members in UPPER_CASE, and that convention appears throughout our examples.

Whether a member's value carries meaning depends on the particular enum, yet regardless of that, the value lets you look up the matching member:

```python
>>> Weekday(3)
<Weekday.WEDNESDAY: 3>

```

Notice that a member's `repr()` displays the enum name together with the member name and its value. By contrast, the `str()` of a member prints just the enum name and the member name:

```python
>>> print(Weekday.THURSDAY)
Weekday.THURSDAY

```

A member's *type* is whichever enumeration it was declared in:

```python
>>> type(Weekday.MONDAY)
<enum 'Weekday'>
>>> isinstance(Weekday.FRIDAY, Weekday)
True

```

Every Enum member exposes a `name` attribute holding only its name:

```python
>>> print(Weekday.TUESDAY.name)
TUESDAY

```

In the same way, each one carries a `value` attribute:

```python
>>> Weekday.WEDNESDAY.value
3

```

[Subject index](INDEX.md) · [Weekday class method and date lookup](weekday-class-method-and-date-lookup.md) · [Flag combinations and iteration](flag-combinations-and-iteration.md) · [Flag chores and automatic values](flag-chores-and-automatic-values.md) · [Following source context](weekday-class-method-and-date-lookup.md)
