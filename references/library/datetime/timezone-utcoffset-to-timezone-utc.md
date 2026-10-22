# datetime — `timezone` objects

timezone.utcoffset(*dt*)

Hand back the fixed value that was set when the `timezone` instance was built.

The *dt* argument plays no role. What comes back is a `timedelta` instance matching the gap between local time and UTC.

Changed in version 3.7: A whole number of minutes no longer bounds the UTC offset.

 timezone.tzname(*dt*)

Hand back the fixed value that was set when the `timezone` instance was built.

When the constructor receives no *name*, the name that `tzname(dt)` returns is built from the `offset` value in this way. Where *offset* equals `timedelta(0)`, the name becomes "UTC"; otherwise it takes the form `UTC±HH:MM`, with ± being the sign of `offset` and HH and MM being two-digit renderings of `offset.hours` and `offset.minutes` in turn.

Changed in version 3.6: Name generated from `offset=timedelta(0)` is now plain `'UTC'`, not `'UTC+00:00'`.

 timezone.dst(*dt*)

Always returns `None`.

 timezone.fromutc(*dt*)

Return `dt + offset`. The *dt* argument must be an aware `datetime` instance, with `tzinfo` set to `self`.

Class attributes:

 timezone.utc

The UTC time zone, `timezone(timedelta(0))`.

[Subject index](INDEX.md) · [Previous](datetime-timezone-class.md) · [Continue](strftime-and-strptime-behavior.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: datetime.timezone](datetime-timezone-class.md) · [Owning module, declaration or section: `timezone` objects](datetime-timezone-class.md)
