# datetime: `datetime.strptime()`, `datetime.min`, `datetime.max`, `datetime.resolution`, `datetime.year`, `datetime.month`, `datetime.day`, `datetime.hour`, `datetime.minute`, `datetime.second`, `datetime.microsecond`, `datetime.tzinfo`

*classmethod *datetime.strptime(*date_string*, *format*)

Return a `datetime` matching *date_string*, parsed in accordance with *format*.

When *format* carries neither microseconds nor time zone information, this matches:

```python
datetime(*(time.strptime(date_string, format)[0:6]))

```

[`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised when [`time.strptime()`](https://docs.python.org/3.14/library/time.html#time.strptime) cannot parse the date_string and format, or when it yields a value that is not a time tuple. Consult also strftime() and strptime() behavior and `datetime.fromisoformat()`.

Changed in version 3.13: Should *format* name a day of month while omitting a year, a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) now gets emitted. The point is to head off a quadrennial leap year defect: when code tries to parse just a month plus a day, the year that fills in for a missing one in the format is not itself a leap year. Beginning with Python 3.15, *format* values of that kind may trigger an error. To get around it, always carry a year inside your *format*. When you parse *date_string* values lacking a year, deliberately prepend a leap year ahead of parsing:

```pycon
>>> import datetime as dt
>>> date_string = "02/29"
>>> when = dt.datetime.strptime(f"{date_string};1984", "%m/%d;%Y")  # Avoids leap year bug.
>>> when.strftime("%B %d")
'February 29'

```

Class attributes:

 datetime.min

The earliest representable `datetime`, `datetime(MINYEAR, 1, 1, tzinfo=None)`.

 datetime.max

The latest representable `datetime`, `datetime(MAXYEAR, 12, 31, 23, 59, 59, 999999, tzinfo=None)`.

 datetime.resolution

The smallest possible difference between non-equal `datetime` objects, `timedelta(microseconds=1)`.

Instance attributes (read-only):

 datetime.year

Between `MINYEAR` and `MAXYEAR` inclusive.

 datetime.month

Between 1 and 12 inclusive.

 datetime.day

From 1 up through however many days the named month of the named year holds.

 datetime.hour

In `range(24)`.

 datetime.minute

In `range(60)`.

 datetime.second

In `range(60)`.

 datetime.microsecond

In `range(1000000)`.

 datetime.tzinfo

The object handed in as the *tzinfo* argument to the `datetime` constructor, or `None` when nothing was handed in.

[Subject index](INDEX.md) · [Previous](datetime-isoformat-parsing.md) · [Continue](datetime-fold-to-datetime-replace.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: `datetime` objects](datetime-datetime-class.md)
