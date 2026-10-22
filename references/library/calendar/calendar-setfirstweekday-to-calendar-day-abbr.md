# calendar: Calendar computation, formatting and weekday names

calendar.setfirstweekday(*weekday*)

Picks the weekday (`0` is Monday, `6` is Sunday) on which each week opens. The constants `MONDAY`, `TUESDAY`, `WEDNESDAY`, `THURSDAY`, `FRIDAY`, `SATURDAY`, and `SUNDAY` exist for convenience. As an example, to make Sunday the first weekday:

```python
import calendar
calendar.setfirstweekday(calendar.SUNDAY)

```

 calendar.firstweekday()

Returns the weekday currently set to open each week.

 calendar.isleap(*year*)

Returns [`True`](https://docs.python.org/3.14/library/constants.html#True) when *year* is a leap year, and [`False`](https://docs.python.org/3.14/library/constants.html#False) otherwise.

 calendar.leapdays(*y1*, *y2*)

Returns how many leap years fall in the range from *y1* through *y2* (exclusive), where *y1* and *y2* are years.

This function holds up across ranges that cross a century boundary.

 calendar.weekday(*year*, *month*, *day*)

Returns the day of the week (`0` is Monday) for *year* (`1970`–…), *month* (`1`–`12`), *day* (`1`–`31`).

 calendar.weekheader(*n*)

Return a header made of abbreviated weekday names. *n* sets the character width given to one weekday.

 calendar.monthrange(*year*, *month*)

Returns the weekday of the month's first day along with the day count of the month, for the named *year* and *month*.

 calendar.monthcalendar(*year*, *month*)

Returns a matrix that depicts a month's calendar. Each row stands for a week; days lying outside the month show up as zeros. Each week opens on Monday unless changed via `setfirstweekday()`.

 calendar.prmonth(*theyear*, *themonth*, *w=0*, *l=0*)

Prints a month's calendar exactly as `month()` returns it.

 calendar.month(*theyear*, *themonth*, *w=0*, *l=0*)

Returns a month's calendar as a multi-line string by way of the `formatmonth()` of the `TextCalendar` class.

 calendar.prcal(*year*, *w=0*, *l=0*, *c=6*, *m=3*)

Prints the whole year's calendar exactly as `calendar()` returns it.

 calendar.calendar(*year*, *w=2*, *l=1*, *c=6*, *m=3*)

Returns a 3-column calendar covering a whole year as a multi-line string by way of the `formatyear()` of the `TextCalendar` class.

 calendar.timegm(*tuple*)

An unrelated yet convenient function that accepts a time tuple of the kind the [`gmtime()`](https://docs.python.org/3.14/library/time.html#time.gmtime) function in the [`time`](https://docs.python.org/3.14/library/time.html#module-time) module returns, and gives back the matching Unix timestamp value, presuming an epoch of 1970 and the POSIX encoding. Indeed, `time.gmtime()` and `timegm()` invert one another.

The `calendar` module exports the following data attributes:

 calendar.day_name

A sequence standing for the days of the week in the active locale, where Monday is day number 0.

```python
>>> import calendar
>>> list(calendar.day_name)
['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

```

 calendar.day_abbr

A sequence standing for the shortened days of the week in the active locale, where Mon is day number 0.

```python
>>> import calendar
>>> list(calendar.day_abbr)
['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

```

[Subject index](INDEX.md) · [Previous](calendar-localehtmlcalendar-class.md) · [Continue](calendar-monday-to-calendar-sunday.md) · [Owning module, declaration or section: calendar](calendar-calendar-class.md)
