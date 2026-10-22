# datetime — `tzinfo` objects — Signature and initial contract

tzinfo.fromutc(*dt*)

The default `datetime.astimezone()` implementation invokes this. In that situation, `dt.tzinfo` equals *self*, while the date and time fields of *dt* should be treated as denoting a UTC time. What `fromutc()` exists to do is shift those date and time fields so it hands back an equivalent datetime expressed in *self*'s local time.

For the great majority of `tzinfo` subclasses, inheriting the default `fromutc()` implementation will work fine. That implementation copes well with fixed-offset time zones, plus time zones that track both standard and daylight time — even when the years differ in when their DST transitions land. One situation the default `fromutc()` implementation might mishandle is a zone whose standard offset (relative to UTC) varies with the exact date and time supplied, something that political decisions can cause. The default `astimezone()` and `fromutc()` implementations might not give you the outcome you expect when that outcome lands in one of the hours bracketing the instant the standard offset shifts.

Leaving out the error-handling code, the default `fromutc()` implementation behaves roughly like:

```python
import datetime as dt

def fromutc(self, when):
    # raise ValueError error if when.tzinfo is not self
    dtoff = when.utcoffset()
    dtdst = when.dst()
    # raise ValueError if dtoff is None or dtdst is None
    delta = dtoff - dtdst  # this is self's standard offset
    if delta:
        when += delta   # convert to standard local time
        dtdst = when.dst()
        # raise ValueError if dtdst is None
    if dtdst:
        return when + dtdst
    else:
        return when

```

The [`tzinfo_examples.py`](https://docs.python.org/3.14/_downloads/6dc1f3f4f0e6ca13cb42ddf4d6cbc8af/tzinfo_examples.py) file shown below contains a few sample `tzinfo` classes:

[Subject index](INDEX.md) · [Previous](datetime-tzinfo-methods-and-dt-none-protocol.md) · [Continue](local-timezone-imports-and-implementation.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: datetime.tzinfo](datetime-tzinfo-class.md) · [Owning module, declaration or section: `tzinfo` objects](datetime-tzinfo-class.md)
