# datetime: `date.strptime()`, `date.min`, `date.max`, `date.resolution`, `date.year`, `date.month`

*classmethod *date.strptime(*date_string*, *format*)

Return a `date` corresponding to *date_string*, parsed according to *format*. This is equivalent to:

```python
date(*(time.strptime(date_string, format)[0:3]))

```

Should [`time.strptime()`](https://docs.python.org/3.14/library/time.html#time.strptime) fail to parse the date_string and format, or hand back something that is not a time tuple, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised. See also strftime() and strptime() behavior and `date.fromisoformat()`.

Note

When a *format* names a day of month but omits a year, a [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning) is issued. The point is to dodge a once-every-four-years leap year bug in code that parses just a month and day, since the fallback year applied when the format supplies none is not a leap year. From Python 3.15 onward, such *format* values may raise an error. To work around it, always put a year into your *format*. When parsing *date_string* values lacking a year, deliberately prepend a leap-year year before you parse:

```pycon
>>> import datetime as dt
>>> date_string = "02/29"
>>> when = dt.date.strptime(f"{date_string};1984", "%m/%d;%Y")  # Avoids leap year bug.
>>> when.strftime("%B %d")
'February 29'

```

Added in version 3.14.

Class attributes:

 date.min

The earliest representable date, `date(MINYEAR, 1, 1)`.

 date.max

The latest representable date, `date(MAXYEAR, 12, 31)`.

 date.resolution

The smallest possible difference between non-equal date objects, `timedelta(days=1)`.

Instance attributes (read-only):

 date.year

Between `MINYEAR` and `MAXYEAR` inclusive.

 date.month

Between 1 and 12 inclusive.

[Subject index](INDEX.md) · [Previous](date-objects.md) · [Continue](date-day-to-date-toordinal.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: datetime.date](datetime-date-class.md) · [Owning module, declaration or section: `date` objects](datetime-date-class.md)
