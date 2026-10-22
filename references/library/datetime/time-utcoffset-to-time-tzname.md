# datetime: `time.utcoffset()`, `time.dst()`, `time.tzname()`

time.utcoffset()

When `tzinfo` is `None`, returns `None`; otherwise returns `self.tzinfo.utcoffset(None)`, and throws an exception if that call fails to return `None` or a `timedelta` object whose magnitude is under one day.

Changed in version 3.7: The UTC offset no longer has to land on an exact whole minute.

 time.dst()

When `tzinfo` is `None`, returns `None`; otherwise returns `self.tzinfo.dst(None)`, and throws an exception if that call fails to return `None`, or a `timedelta` object whose magnitude is under one day.

Changed in version 3.7: The DST offset no longer has to land on an exact whole minute.

 time.tzname()

When `tzinfo` is `None`, returns `None`; otherwise returns `self.tzinfo.tzname(None)`, or throws an exception if that call fails to return `None` or a string object.

[Subject index](INDEX.md) · [Previous](time-isoformat-to-time-format.md) · [Continue](examples-of-usage-time.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: datetime.time](datetime-time-class.md) · [Owning module, declaration or section: `time` objects](datetime-time-class.md)
