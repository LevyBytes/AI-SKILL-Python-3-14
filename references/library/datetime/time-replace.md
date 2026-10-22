# datetime: `time.fromisoformat()`, `time.strptime()`, `time.replace()`

*classmethod *time.fromisoformat(*time_string*)

Give back a `time` matching a *time_string* in any valid ISO 8601 format, subject to these exceptions:

1.

Time zone offsets may have fractional seconds.

2.

The leading `T`, ordinarily needed where a date and a time might be confused, is not needed here.

3.

A fractional-seconds field may carry any digit count (whatever runs past 6 gets truncated).

4.

Fractional hours and minutes are not supported.

Examples:

```pycon
>>> import datetime as dt
>>> dt.time.fromisoformat('04:23:01')
datetime.time(4, 23, 1)
>>> dt.time.fromisoformat('T04:23:01')
datetime.time(4, 23, 1)
>>> dt.time.fromisoformat('T042301')
datetime.time(4, 23, 1)
>>> dt.time.fromisoformat('04:23:01.000384')
datetime.time(4, 23, 1, 384)
>>> dt.time.fromisoformat('04:23:01,000384')
datetime.time(4, 23, 1, 384)
>>> dt.time.fromisoformat('04:23:01+04:00')
datetime.time(4, 23, 1, tzinfo=datetime.timezone(datetime.timedelta(seconds=14400)))
>>> dt.time.fromisoformat('04:23:01Z')
datetime.time(4, 23, 1, tzinfo=datetime.timezone.utc)
>>> dt.time.fromisoformat('04:23:01+00:00')
datetime.time(4, 23, 1, tzinfo=datetime.timezone.utc)

```

Added in version 3.7.

Changed in version 3.11: Earlier on, this method handled only the formats that `time.isoformat()` could emit.

 *classmethod *time.strptime(*date_string*, *format*)

Give back a `time` matching *date_string*, parsed in line with *format*.

When *format* carries no microseconds or timezone information, this amounts to:

```python
time(*(time.strptime(date_string, format)[3:6]))

```

[`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised when the *date_string* and *format* cannot be parsed by `time.strptime()` or when it yields a value that is not a time tuple. See also strftime() and strptime() behavior and `time.fromisoformat()`.

Added in version 3.14.

Instance methods:

 time.replace(*hour=self.hour*, *minute=self.minute*, *second=self.second*, *microsecond=self.microsecond*, *tzinfo=self.tzinfo*, ***, *fold=0*)

Give back a fresh `time` holding the same values, except that the named parameters are updated. Note that `tzinfo=None` can be supplied to produce a naive `time` out of an aware `time`, leaving the time data unconverted.

`time` objects are likewise supported by the generic function [`copy.replace()`](https://docs.python.org/3.14/library/copy.html#copy.replace).

Changed in version 3.6: Added the *fold* parameter.

[Subject index](INDEX.md) · [Previous](time-min-to-time-fold.md) · [Continue](time-isoformat-to-time-format.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: datetime.time](datetime-time-class.md) · [Owning module, declaration or section: `time` objects](datetime-time-class.md)
