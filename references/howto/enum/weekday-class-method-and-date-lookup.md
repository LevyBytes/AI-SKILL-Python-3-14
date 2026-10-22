# Weekday class method and date lookup

Where most languages reduce enumerations to mere name/value pairs, Python lets you attach behavior to them. As an illustration, [`datetime.date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) exposes two weekday-returning methods, [`weekday()`](https://docs.python.org/3.14/library/datetime.html#datetime.date.weekday) and [`isoweekday()`](https://docs.python.org/3.14/library/datetime.html#datetime.date.isoweekday), where one numbers the days 0-6 and the other 1-7. To avoid juggling that distinction by hand, we can attach a method to the `Weekday` enum that pulls the day out of a `date` instance and hands back the corresponding enum member:

```python
@classmethod
def from_date(cls, date):
    return cls(date.isoweekday())

```

With that added, the full `Weekday` enum reads as follows:

```python
>>> class Weekday(Enum):
...     MONDAY = 1
...     TUESDAY = 2
...     WEDNESDAY = 3
...     THURSDAY = 4
...     FRIDAY = 5
...     SATURDAY = 6
...     SUNDAY = 7
...     #
...     @classmethod
...     def from_date(cls, date):
...         return cls(date.isoweekday())

```

So now we can discover today's day! Watch:

```python
>>> import datetime as dt
>>> Weekday.from_date(dt.date.today())
<Weekday.TUESDAY: 2>

```

Naturally, anyone reading this on a different day will get that day in the result instead.

[Subject index](INDEX.md) · [Enum creation, names, values and member types](enum-creation-names-values-and-member-types.md) · [Flag combinations and iteration](flag-combinations-and-iteration.md) · [Flag chores and automatic values](flag-chores-and-automatic-values.md) · [Previous source context](enum-creation-names-values-and-member-types.md) · [Following source context](flag-combinations-and-iteration.md)
