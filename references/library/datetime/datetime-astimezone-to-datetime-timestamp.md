# datetime: `datetime.astimezone()`, `datetime.utcoffset()`, `datetime.dst()`, `datetime.tzname()`, `datetime.timetuple()`, `datetime.utctimetuple()`, `datetime.toordinal()`, `datetime.timestamp()`

datetime.astimezone(*tz=None*)

Return a `datetime` object whose `tzinfo` attribute is the new *tz*, with the date and time data shifted so the outcome marks the same UTC instant as *self*, but expressed in *tz*’s local time.

When supplied, *tz* has to be an instance of a `tzinfo` subclass, and neither its `utcoffset()` nor its `dst()` method may return `None`. Should *self* be naive, it is taken to stand for time in the system time zone.

Where the call carries no arguments (or `tz=None`), the system local time zone fills the role of target. On the converted datetime instance, the `.tzinfo` attribute gets assigned a `timezone` instance whose zone name and offset are drawn from the OS.

When `self.tzinfo` is *tz*, `self.astimezone(tz)` equals *self*: no shifting of date or time data takes place. Otherwise the outcome is local time within the time zone *tz*, marking the same UTC instant as *self*: after `astz = dt.astimezone(tz)`, `astz - astz.utcoffset()` will hold the same date and time data as `dt - dt.utcoffset()`.

When you simply wish to bind a `timezone` object *tz* onto a datetime *dt* without shifting date and time data, use `dt.replace(tzinfo=tz)`. When you simply wish to strip the `timezone` object off an aware datetime *dt* without converting date and time data, use `dt.replace(tzinfo=None)`.

Note that overriding the default `tzinfo.fromutc()` method within a `tzinfo` subclass can alter the outcome that `astimezone()` returns. Setting error cases aside, `astimezone()` behaves like:

```python
def astimezone(self, tz):
    if self.tzinfo is tz:
        return self
    # Convert self to UTC, and attach the new timezone object.
    utc = (self - self.utcoffset()).replace(tzinfo=tz)
    # Convert from UTC to tz's local time.
    return tz.fromutc(utc)

```

Changed in version 3.3: *tz* now can be omitted.

Changed in version 3.6: You may now invoke the `astimezone()` method on naive instances, which are taken to stand for system local time.

 datetime.utcoffset()

When `tzinfo` is `None`, returns `None`; otherwise returns `self.tzinfo.utcoffset(self)`, and raises an exception should the latter fail to return either `None` or a `timedelta` object whose magnitude is under one day.

Changed in version 3.7: A whole number of minutes no longer bounds the UTC offset.

 datetime.dst()

When `tzinfo` is `None`, returns `None`; otherwise returns `self.tzinfo.dst(self)`, and raises an exception should the latter fail to return either `None` or a `timedelta` object whose magnitude is under one day.

Changed in version 3.7: A whole number of minutes no longer bounds the DST offset.

 datetime.tzname()

When `tzinfo` is `None`, returns `None`; otherwise returns `self.tzinfo.tzname(self)`, raising an exception should the latter fail to return either `None` or a string object,

 datetime.timetuple()

Return a [`time.struct_time`](https://docs.python.org/3.14/library/time.html#time.struct_time) of the sort handed back by [`time.localtime()`](https://docs.python.org/3.14/library/time.html#time.localtime).

`d.timetuple()` is equivalent to:

```python
time.struct_time((d.year, d.month, d.day,
                  d.hour, d.minute, d.second,
                  d.weekday(), yday, dst))

```

where `yday = d.toordinal() - date(d.year, 1, 1).toordinal() + 1` gives the day number inside the current year, beginning at 1 for January 1st. The [`tm_isdst`](https://docs.python.org/3.14/library/time.html#time.struct_time.tm_isdst) flag of the outcome follows the `dst()` method: when `tzinfo` is `None` or `dst()` returns `None`, `tm_isdst` is set to `-1`; otherwise, when `dst()` returns a non-zero value, `tm_isdst` is set to 1; otherwise `tm_isdst` is set to 0.

 datetime.utctimetuple()

Where the `datetime` instance `d` is naive, this matches `d.timetuple()` save that [`tm_isdst`](https://docs.python.org/3.14/library/time.html#time.struct_time.tm_isdst) gets forced to 0 no matter what `d.dst()` returns. DST is never in effect for a UTC time.

Where `d` is aware, `d` gets normalized to UTC time by subtracting `d.utcoffset()`, and a [`time.struct_time`](https://docs.python.org/3.14/library/time.html#time.struct_time) for that normalized time is handed back. `tm_isdst` gets forced to 0. Bear in mind that [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) can surface where `d.year` held `MINYEAR` or `MAXYEAR` and the UTC adjustment pushes past a year boundary.

Warning

Since a great many `datetime` methods regard naive `datetime` objects as local times, working with aware datetimes for UTC values is the preferred approach; consequently, relying on `datetime.utctimetuple()` can produce misleading outcomes. Where you hold a naive `datetime` standing for UTC, use `datetime.replace(tzinfo=timezone.utc)` to make it aware, after which you can use `datetime.timetuple()`.

 datetime.toordinal()

Return the proleptic Gregorian ordinal of the date. The same as `self.date().toordinal()`.

 datetime.timestamp()

Return POSIX timestamp matching the `datetime` instance. The value handed back is a [`float`](https://docs.python.org/3.14/library/functions.html#float) akin to the one handed back by [`time.time()`](https://docs.python.org/3.14/library/time.html#time.time).

[Subject index](INDEX.md) · [Previous](datetime-fold-to-datetime-replace.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: `datetime` objects](datetime-datetime-class.md) · [Required continuation of the source contract](datetime-weekday-to-datetime-isocalendar.md)
