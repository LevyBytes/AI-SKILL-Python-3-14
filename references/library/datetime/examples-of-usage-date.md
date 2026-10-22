# datetime — Examples of usage: `date`

Behaves identically to `date.strftime()`. This lets you supply a format string for a `date` object inside [formatted string literals](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings) and through [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format). Consult strftime() and strptime() behavior and `date.isoformat()` for further detail.

### Examples of usage: `date`

Here is a sample that counts the days remaining until an event:

```python
>>> import time
>>> import datetime as dt
>>> today = dt.date.today()
>>> today
datetime.date(2007, 12, 5)
>>> today == dt.date.fromtimestamp(time.time())
True
>>> my_birthday = dt.date(today.year, 6, 24)
>>> if my_birthday < today:
...     my_birthday = my_birthday.replace(year=today.year + 1)
...
>>> my_birthday
datetime.date(2008, 6, 24)
>>> time_to_birthday = abs(my_birthday - today)
>>> time_to_birthday.days
202

```

Some additional examples that exercise `date`:

```pycon
>>> import datetime as dt
>>> d = dt.date.fromordinal(730920) # 730920th day after 1. 1. 0001
>>> d
datetime.date(2002, 3, 11)

>>> # Methods related to formatting string output
>>> d.isoformat()
'2002-03-11'
>>> d.strftime("%d/%m/%y")
'11/03/02'
>>> d.strftime("%A %d. %B %Y")
'Monday 11. March 2002'
>>> d.ctime()
'Mon Mar 11 00:00:00 2002'
>>> 'The {1} is {0:%d}, the {2} is {0:%B}.'.format(d, "day", "month")
'The day is 11, the month is March.'

>>> # Methods for extracting 'components' under different calendars
>>> t = d.timetuple()
>>> for i in t:
...     print(i)
2002                # year
3                   # month
11                  # day
0
0
0
0                   # weekday (0 = Monday)
70                  # 70th day in the year
-1
>>> ic = d.isocalendar()
>>> for i in ic:
...     print(i)
2002                # ISO year
11                  # ISO week number
1                   # ISO day number ( 1 = Monday )

>>> # A date object is immutable; all operations produce a new object
>>> d.replace(year=2005)
datetime.date(2005, 3, 11)

```

[Subject index](INDEX.md) · [Continue](datetime-datetime-class.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: datetime.date](datetime-date-class.md) · [Owning module, declaration or section: `date` objects](datetime-date-class.md) · [Owning module, declaration or section: date.__format__](date-weekday-to-date-format.md) · [Preceding source contract and version conditions](date-weekday-to-date-format.md)
