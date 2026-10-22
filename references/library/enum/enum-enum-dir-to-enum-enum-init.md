# enum.Enum: `__dir__()`, `_generate_next_value_()`, `__init__()`

__dir__(*self*)

Yields `['__class__', '__doc__', '__module__', 'name', 'value']` plus whatever public methods are declared on *self.__class__*:

```python
>>> from enum import Enum
>>> import datetime as dt
>>> class Weekday(Enum):
...     MONDAY = 1
...     TUESDAY = 2
...     WEDNESDAY = 3
...     THURSDAY = 4
...     FRIDAY = 5
...     SATURDAY = 6
...     SUNDAY = 7
...     @classmethod
...     def today(cls):
...         print(f'today is {cls(dt.date.today().isoweekday()).name}')
...
>>> dir(Weekday.SATURDAY)
['__class__', '__doc__', '__eq__', '__hash__', '__module__', 'name', 'today', 'value']

```

 _generate_next_value_(*name*, *start*, *count*, *last_values*)

>

name:

The name of the member being defined (e.g. ‘RED’).

start:

The start value for the Enum; the default is 1.

count:

The number of members currently defined, not including this one.

last_values:

A list of the previous values.

A *staticmethod* whose role is deciding the upcoming value handed back by `auto`.

Note

In ordinary `Enum` classes the next value selected equals the highest value observed so far plus one.

In `Flag` classes the next value selected is the following highest power-of-two.

Overriding this method is possible, for instance:

```python
>>> from enum import auto, Enum
>>> class PowersOfThree(Enum):
...     @staticmethod
...     def _generate_next_value_(name, start, count, last_values):
...         return 3 ** (count + 1)
...     FIRST = auto()
...     SECOND = auto()
...
>>> PowersOfThree.SECOND.value
9

```

Added in version 3.6.

Changed in version 3.13: Earlier versions relied on the most recently seen value rather than the highest value.

 __init__(*self*, **args*, ***kwds*)

By default this does nothing. When more than one value appears in the member assignment, each of those values arrives as a distinct argument to `__init__`; for example

```python
>>> from enum import Enum
>>> class Weekday(Enum):
...     MONDAY = 1, 'Mon'

```

[Subject index](INDEX.md) · [Previous](enum-enum-class.md) · [Continue](weekday-init-to-enum-enum-repr.md) · [Owning module, declaration or section: enum](enum-support-for-enumerations.md) · [Owning module, declaration or section: enum.Enum](enum-enum-class.md) · [Owning module, declaration or section: Data types](enum-enumtype-class.md)
