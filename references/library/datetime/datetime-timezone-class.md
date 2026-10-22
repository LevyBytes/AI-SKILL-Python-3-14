# datetime: `datetime.timezone`

*class *datetime.timezone

A class realizing the `tzinfo` abstract base class as a constant offset away from UTC.

Added in version 3.2.

Objects of these types are immutable.

Subclass relationships:

  (Figure: timedelta, tzinfo, time, and date inherit from object; timezone inherits from tzinfo; and datetime inherits from date.)

### `timezone` objects

Being a subclass of `tzinfo`, the `timezone` class produces instances that each stand for a time zone given by a fixed offset relative to UTC.

You cannot use objects of this class to capture time zone details for places that apply different offsets on different days of the year, or where civil time has been altered by historical changes.

 *class *datetime.timezone(*offset*, *name=None*)

You must give the *offset* argument as a `timedelta` object that captures the gap between local time and UTC. Its value has to fall strictly within `-timedelta(hours=24)` and `timedelta(hours=24)`, or else [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

Supplying the *name* argument is optional. When you do supply it, it has to be a string, and that string becomes the value the `datetime.tzname()` method returns.

Added in version 3.2.

Changed in version 3.7: A whole number of minutes no longer bounds the UTC offset.

[Subject index](INDEX.md) · [Previous](datetime-tzinfo-class.md) · [Continue](common-properties.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: Available types](datetime-date-class.md) · [Previous](datetime-and-right-at-the-dst-transition-points.md) · [Continue](timezone-utcoffset-to-timezone-utc.md)
