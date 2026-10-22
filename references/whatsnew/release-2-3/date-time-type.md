# What’s New in Python 2.3 / Date/Time Type — datetime

### Date/Time Type

The [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime) module introduced date and time types fit for representing timestamps. These types skip alternate calendars and elaborate extras, keeping to the essentials of representing time.

There are three core types: [`date`](https://docs.python.org/3.14/library/datetime.html#datetime.date), which holds a day, month, and year; [`time`](https://docs.python.org/3.14/library/datetime.html#datetime.time), made up of hour, minute, and second; and [`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime), which carries every attribute of both `date` and `time`. A [`timedelta`](https://docs.python.org/3.14/library/datetime.html#datetime.timedelta) class also exists to represent the gap between two moments in time, and time zone behavior comes from classes deriving from the abstract [`tzinfo`](https://docs.python.org/3.14/library/datetime.html#datetime.tzinfo) class.

You can build instances of [`date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) and [`time`](https://docs.python.org/3.14/library/datetime.html#datetime.time) either by handing keyword arguments to the relevant constructor, e.g. `datetime.date(year=1972, month=10, day=15)`, or through one of several class methods. As an example, the [`today()`](https://docs.python.org/3.14/library/datetime.html#datetime.date.today) class method gives back the current local date.

After creation, every instance of the date/time classes is immutable. Several methods exist for generating formatted strings from these objects:

```python
>>> import datetime as dt
>>> now = dt.datetime.now()
>>> now.isoformat()
'2002-12-30T21:27:03.994956'
>>> now.ctime()  # Only available on date, datetime
'Mon Dec 30 21:27:03 2002'
>>> now.strftime('%Y %d %b')
'2002 30 Dec'

```

With the [`replace()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.replace) method you can change one or several fields of a [`date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) or [`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) instance, which yields a fresh instance:

```python
>>> d = dt.datetime.now()
>>> d
datetime.datetime(2002, 12, 30, 22, 15, 38, 827738)
>>> d.replace(year=2001, hour=12)
datetime.datetime(2001, 12, 30, 12, 15, 38, 827738)
>>>

```

These instances support comparison, hashing, and conversion into strings (the outcome matches that of [`isoformat()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.isoformat)). You can subtract [`date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) and [`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) instances from one another, and add them to [`timedelta`](https://docs.python.org/3.14/library/datetime.html#datetime.timedelta) instances. The biggest gap is the lack of any standard library facility for parsing strings to recover a `date` or `datetime`.

Consult the module's reference documentation for further details. (Contributed by Tim Peters.)

[Subject index](INDEX.md) · [Previous source section](unicode-network-hostnames-and-stringprep.md) · [Next source section](the-optparse-module.md) · [Release/subject declaration](standard-set-type.md)
