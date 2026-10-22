# datetime: `date.day`, `date.replace()`, `date.timetuple()`, `date.toordinal()`

date.day

From 1 up through however many days that particular month of that particular year holds.

Supported operations:

| Operation | Result |
| --- | --- |
| `date2 = date1 + timedelta` | `date2` will be `timedelta.days` days after `date1`. (1) |
| `date2 = date1 - timedelta` | Computes `date2` such that `date2 + timedelta == date1`. (2) |
| `timedelta = date1 - date2` | (3) |
| `date1 == date2` `date1 != date2` | Equality comparison. (4) |
| `date1 < date2` `date1 > date2` `date1 <= date2` `date1 >= date2` | Order comparison. (5) |

Notes:

1.

*date2* shifts later in time when `timedelta.days > 0`, or earlier when `timedelta.days < 0`. Afterward `date2 - date1 == timedelta.days`. Both `timedelta.seconds` and `timedelta.microseconds` get disregarded. Whenever `date2.year` would drop below `MINYEAR` or climb above `MAXYEAR`, [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) is raised.

2.

`timedelta.seconds` and `timedelta.microseconds` are ignored.

3.

This is exact, and cannot overflow. `timedelta.seconds` and `timedelta.microseconds` are 0, and `date2 + timedelta == date1` after.

4.

`date` objects are equal if they represent the same date.

A `date` object that is not likewise a `datetime` instance never compares equal to any `datetime` object, even where the two stand for one and the same date.

5.

*date1* counts as less than *date2* whenever *date1* comes before *date2* in time. Put differently, `date1 < date2` holds exactly when `date1.toordinal() < date2.toordinal()`.

Ordering a `date` object that is not likewise a `datetime` instance against a `datetime` object raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

Changed in version 3.13: When a `datetime` object is compared with an instance of the `date` subclass that isn’t itself a `datetime` subclass, the latter is no longer coerced to `date` with its time part and time zone dropped. Overriding the special comparison methods in subclasses lets you alter this default behavior.

In Boolean contexts, all `date` objects are considered to be true.

Instance methods:

 date.replace(*year=self.year*, *month=self.month*, *day=self.day*)

Give back a fresh `date` object carrying the same values, except that the parameters you name are updated.

Example:

```python
>>> import datetime as dt
>>> d = dt.date(2002, 12, 31)
>>> d.replace(day=26)
datetime.date(2002, 12, 26)

```

The generic function [`copy.replace()`](https://docs.python.org/3.14/library/copy.html#copy.replace) also supports `date` objects.

 date.timetuple()

Return a [`time.struct_time`](https://docs.python.org/3.14/library/time.html#time.struct_time) such as returned by [`time.localtime()`](https://docs.python.org/3.14/library/time.html#time.localtime).

Hours, minutes and seconds come out as 0, while the DST flag comes out as -1.

`d.timetuple()` is equivalent to:

```python
time.struct_time((d.year, d.month, d.day, 0, 0, 0, d.weekday(), yday, -1))

```

in which `yday = d.toordinal() - date(d.year, 1, 1).toordinal() + 1` gives the day count inside the present year, counting from 1 at January 1st.

 date.toordinal()

Give back the date’s proleptic Gregorian ordinal, in which ordinal 1 falls on January 1 of year 1. For any `date` object `d`, `date.fromordinal(d.toordinal()) == d`.

[Subject index](INDEX.md) · [Previous](date-min-to-date-month.md) · [Continue](date-weekday-to-date-format.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: datetime.date](datetime-date-class.md) · [Owning module, declaration or section: `date` objects](datetime-date-class.md)
