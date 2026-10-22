# Flag chores and automatic values

Right, let's arrange a few chores:

```python
>>> chores_for_ethan = {
...     'feed the cat': Weekday.MONDAY | Weekday.WEDNESDAY | Weekday.FRIDAY,
...     'do the dishes': Weekday.TUESDAY | Weekday.THURSDAY,
...     'answer SO questions': Weekday.SATURDAY,
...     }

```

Plus a routine to print the chores tied to a particular day:

```python
>>> def show_chores(chores, day):
...     for chore, days in chores.items():
...         if day in days:
...             print(chore)
...
>>> show_chores(chores_for_ethan, Weekday.SATURDAY)
answer SO questions

```

When the concrete values of the members are irrelevant, you can spare yourself the effort and hand [`auto()`](https://docs.python.org/3.14/library/enum.html#enum.auto) the job of filling them in:

```python
>>> from enum import auto
>>> class Weekday(Flag):
...     MONDAY = auto()
...     TUESDAY = auto()
...     WEDNESDAY = auto()
...     THURSDAY = auto()
...     FRIDAY = auto()
...     SATURDAY = auto()
...     SUNDAY = auto()
...     WEEKEND = SATURDAY | SUNDAY

```

[Subject index](INDEX.md) · [Enum creation, names, values and member types](enum-creation-names-values-and-member-types.md) · [Weekday class method and date lookup](weekday-class-method-and-date-lookup.md) · [Flag combinations and iteration](flag-combinations-and-iteration.md) · [Previous source context](flag-combinations-and-iteration.md) · [Following source context](enum-member-and-attribute-access.md)
