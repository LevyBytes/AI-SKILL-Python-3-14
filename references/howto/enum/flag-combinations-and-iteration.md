# Flag combinations and iteration

That `Weekday` enum serves us well when the variable holds a single day, but suppose we want more than one at a time? Imagine a routine that schedules chores across a week, where we'd rather not lean on a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list) – another flavor of [`Enum`](https://docs.python.org/3.14/library/enum.html#enum.Enum) fits better:

```python
>>> from enum import Flag
>>> class Weekday(Flag):
...     MONDAY = 1
...     TUESDAY = 2
...     WEDNESDAY = 4
...     THURSDAY = 8
...     FRIDAY = 16
...     SATURDAY = 32
...     SUNDAY = 64

```

Two adjustments were made: the base class is now [`Flag`](https://docs.python.org/3.14/library/enum.html#enum.Flag), and each value is a power of 2.

Exactly as with the earlier `Weekday` enum, a lone selection works fine:

```python
>>> first_week_day = Weekday.MONDAY
>>> first_week_day
<Weekday.MONDAY: 1>

```

Yet [`Flag`](https://docs.python.org/3.14/library/enum.html#enum.Flag) additionally lets us fold multiple members together into one variable:

```python
>>> weekend = Weekday.SATURDAY | Weekday.SUNDAY
>>> weekend
<Weekday.SATURDAY|SUNDAY: 96>

```

It's even possible to iterate across a [`Flag`](https://docs.python.org/3.14/library/enum.html#enum.Flag) variable:

```python
>>> for day in weekend:
...     print(day)
Weekday.SATURDAY
Weekday.SUNDAY

```

[Subject index](INDEX.md) · [Enum creation, names, values and member types](enum-creation-names-values-and-member-types.md) · [Weekday class method and date lookup](weekday-class-method-and-date-lookup.md) · [Flag chores and automatic values](flag-chores-and-automatic-values.md) · [Previous source context](weekday-class-method-and-date-lookup.md) · [Following source context](flag-chores-and-automatic-values.md)
