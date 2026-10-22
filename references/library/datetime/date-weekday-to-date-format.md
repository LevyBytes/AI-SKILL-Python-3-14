# datetime: `date.weekday()`, `date.isoweekday()`, `date.isocalendar()`, `date.isoformat()`, `date.__str__()`, `date.ctime()`, `date.strftime()`, `date.__format__()`

date.weekday()

Give back the weekday as an integer, counting Monday as 0 through Sunday as 6. As an illustration, `date(2002, 12, 4).weekday() == 2`, a Wednesday. See also `isoweekday()`.

 date.isoweekday()

Give back the weekday as an integer, counting Monday as 1 through Sunday as 7. As an illustration, `date(2002, 12, 4).isoweekday() == 3`, a Wednesday. See also `weekday()`, `isocalendar()`.

 date.isocalendar()

Return a [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) object with three components: `year`, `week` and `weekday`.

A broadly adopted variant of the Gregorian calendar is the ISO calendar. [3]

An ISO year is made of either 52 or 53 complete weeks, each week running from Monday through Sunday. An ISO year’s first week is the earliest (Gregorian) calendar week of a year that contains a Thursday. That week is labeled week number 1, and the ISO year of that Thursday matches its Gregorian year.

Take 2004, which opens on a Thursday: ISO year 2004’s opening week therefore runs from Monday, 29 Dec 2003 through Sunday, 4 Jan 2004:

```python
>>> import datetime as dt
>>> dt.date(2003, 12, 29).isocalendar()
datetime.IsoCalendarDate(year=2004, week=1, weekday=1)
>>> dt.date(2004, 1, 4).isocalendar()
datetime.IsoCalendarDate(year=2004, week=1, weekday=7)

```

Changed in version 3.9: Result changed from a tuple to a [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple).

 date.isoformat()

Return a string representing the date in ISO 8601 format, `YYYY-MM-DD`:

```python
>>> import datetime as dt
>>> dt.date(2002, 12, 4).isoformat()
'2002-12-04'

```

 date.__str__()

For a date `d`, `str(d)` is equivalent to `d.isoformat()`.

 date.ctime()

Return a string representing the date:

```python
>>> import datetime as dt
>>> dt.date(2002, 12, 4).ctime()
'Wed Dec  4 00:00:00 2002'

```

`d.ctime()` is equivalent to:

```python
time.ctime(time.mktime(d.timetuple()))

```

on any platform whose native C `ctime()` function — the one [`time.ctime()`](https://docs.python.org/3.14/library/time.html#time.ctime) calls, though `date.ctime()` itself does not — follows the C standard.

 date.strftime(*format*)

Give back a string that renders the date, governed by a format string you spell out. Any format codes pointing at hours, minutes or seconds will land on 0 values. See also strftime() and strptime() behavior and `date.isoformat()`.

 date.__format__(*format*)

[Subject index](INDEX.md) · [Previous](date-day-to-date-toordinal.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: datetime.date](datetime-date-class.md) · [Owning module, declaration or section: `date` objects](datetime-date-class.md) · [Required continuation of the source contract](examples-of-usage-date.md)
