# datetime - Examples of usage: `datetime` - Code example: import datetime as dt

```python
import datetime as dt

class KabulTz(dt.tzinfo):
    # Kabul used +4 until 1945, when they moved to +4:30
    UTC_MOVE_DATE = dt.datetime(1944, 12, 31, 20, tzinfo=dt.timezone.utc)

    def utcoffset(self, when):
        if when.year < 1945:
            return dt.timedelta(hours=4)
        elif (1945, 1, 1, 0, 0) <= when.timetuple()[:5] < (1945, 1, 1, 0, 30):
            # An ambiguous ("imaginary") half-hour range representing
            # a 'fold' in time due to the shift from +4 to +4:30.
            # If when falls in the imaginary range, use fold to decide how
            # to resolve. See PEP 495.
            return dt.timedelta(hours=4, minutes=(30 if when.fold else 0))
        else:
            return dt.timedelta(hours=4, minutes=30)

    def fromutc(self, when):
        # Follow same validations as in datetime.tzinfo
        if not isinstance(when, dt.datetime):
            raise TypeError("fromutc() requires a datetime argument")
        if when.tzinfo is not self:
            raise ValueError("when.tzinfo is not self")

        # A custom implementation is required for fromutc as
        # the input to this function is a datetime with utc values
        # but with a tzinfo set to self.
        # See datetime.astimezone or fromtimestamp.
        if when.replace(tzinfo=dt.timezone.utc) >= self.UTC_MOVE_DATE:
            return when + dt.timedelta(hours=4, minutes=30)
        else:
            return when + dt.timedelta(hours=4)

    def dst(self, when):
        # Kabul does not observe daylight saving time.
        return dt.timedelta(0)

    def tzname(self, when):
        if when >= self.UTC_MOVE_DATE:
            return "+04:30"
        return "+04"

```

Putting the `KabulTz` defined above to use:

```python
>>> tz1 = KabulTz()

>>> # Datetime before the change
>>> dt1 = dt.datetime(1900, 11, 21, 16, 30, tzinfo=tz1)
>>> print(dt1.utcoffset())
4:00:00

>>> # Datetime after the change
>>> dt2 = dt.datetime(2006, 6, 14, 13, 0, tzinfo=tz1)
>>> print(dt2.utcoffset())
4:30:00

>>> # Convert datetime to another time zone
>>> dt3 = dt2.astimezone(dt.timezone.utc)
>>> dt3
datetime.datetime(2006, 6, 14, 8, 30, tzinfo=datetime.timezone.utc)
>>> dt2
datetime.datetime(2006, 6, 14, 13, 0, tzinfo=KabulTz())
>>> dt2 == dt3
True

```

[Subject index](INDEX.md) · [Previous](datetime-usage-overview.md) · [Continue](datetime-time-class.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: Examples of usage: `datetime`](datetime-usage-overview.md)
