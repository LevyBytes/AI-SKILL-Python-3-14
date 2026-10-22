# datetime — `tzinfo` objects

tzinfo.utcoffset(*dt*)

Give back the offset of local time from UTC, as a `timedelta` object that runs positive to the east of UTC. When local time sits west of UTC, this ought to be negative.

This stands for the *total* offset away from UTC; for instance, when a `tzinfo` object covers both time zone and DST adjustments, `utcoffset()` ought to give back their sum. When the UTC offset isn’t known, give back `None`. Otherwise the value returned has to be a `timedelta` object lying strictly between `-timedelta(hours=24)` and `timedelta(hours=24)` (the offset's magnitude must stay under one day). The bulk of `utcoffset()` implementations will probably resemble one of these two:

```python
return CONSTANT                 # fixed-offset class
return CONSTANT + self.dst(dt)  # daylight-aware class

```

When `utcoffset()` does not return `None`, `dst()` ought not to return `None` either.

The default implementation of `utcoffset()` raises [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

Changed in version 3.7: The UTC offset no longer has to land on an exact whole minute.

 tzinfo.dst(*dt*)

Give back the daylight saving time (DST) adjustment, as a `timedelta` object, or `None` when the DST information isn’t known.

Give back `timedelta(0)` when DST is not in force. When DST is in force, give back the offset as a `timedelta` object (consult `utcoffset()` for the specifics). Bear in mind that the DST offset, where it applies, has already been folded into the UTC offset that `utcoffset()` gives back, so there’s no reason to query `dst()` unless you specifically want the DST info on its own. For example, `datetime.timetuple()` calls its `tzinfo` attribute’s `dst()` method to work out how the [`tm_isdst`](https://docs.python.org/3.14/library/time.html#time.struct_time.tm_isdst) flag ought to be set, and `tzinfo.fromutc()` calls `dst()` to handle DST shifts when moving across time zones.

Take an instance *tz* of some `tzinfo` subclass that captures both standard and daylight times; it has to stay consistent in this respect:

`tz.utcoffset(dt) - tz.dst(dt)`

has to give back the same result for every `datetime` *dt* where `dt.tzinfo == tz`. For sensible `tzinfo` subclasses, this expression produces the time zone’s “standard offset”, which ought not depend on the date or the time but solely on geographic location. The implementation of `datetime.astimezone()` leans on this yet cannot spot violations; ensuring it falls to the programmer. Where a `tzinfo` subclass can’t guarantee this, it may instead be able to override the default implementation of `tzinfo.fromutc()` so that it cooperates with `astimezone()` all the same.

The bulk of `dst()` implementations will probably resemble one of these two:

```python
import datetime as dt

def dst(self, when):
    # a fixed-offset class:  doesn't account for DST
    return dt.timedelta(0)

```

or:

```python
import datetime as dt

def dst(self, when):
    # Code to set dston and dstoff to the time zone's DST
    # transition times based on the input when.year, and expressed
    # in standard local time.

    if dston <= when.replace(tzinfo=None) < dstoff:
        return dt.timedelta(hours=1)
    else:
        return dt.timedelta(0)

```

The default implementation of `dst()` raises [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

Changed in version 3.7: The DST offset no longer has to land on an exact whole minute.

 tzinfo.tzname(*dt*)

Give back the name of the time zone tied to the `datetime` object *dt*, as a string. The `datetime` module defines nothing about these string names, and there’s no demand that they carry any particular meaning. For instance, `"GMT"`, `"UTC"`, `"-500"`, `"-5:00"`, `"EDT"`, `"US/Eastern"`, `"America/New York"` are all acceptable answers. Give back `None` whenever no string name is available. Bear in mind this is a method instead of a constant string mainly because certain `tzinfo` subclasses will want to hand back varying names according to the exact *dt* value supplied, particularly where the `tzinfo` class is taking daylight time into account.

The default implementation of `tzname()` raises [`NotImplementedError`](https://docs.python.org/3.14/library/exceptions.html#NotImplementedError).

A `datetime` or `time` object invokes these methods in reply to its own methods of matching names. Where a `datetime` object hands itself in as the argument, a `time` object instead supplies `None`. The methods on a `tzinfo` subclass should therefore stand ready for a *dt* argument that is `None`, or of class `datetime`.

[Subject index](INDEX.md) · [Previous](datetime-tzinfo-class.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: datetime.tzinfo](datetime-tzinfo-class.md) · [Owning module, declaration or section: `tzinfo` objects](datetime-tzinfo-class.md) · [Required continuation of the source contract](datetime-tzinfo-methods-and-dt-none-protocol.md)
