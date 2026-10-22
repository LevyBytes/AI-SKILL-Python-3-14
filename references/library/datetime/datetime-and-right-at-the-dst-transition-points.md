# datetime — `tzinfo` objects — Contract: Be aware that a `tzinfo` subclass tracking both standard and daylight time runs into inescapable corner cases twice each year, right at the DST transition points.

Be aware that a `tzinfo` subclass tracking both standard and daylight time runs into inescapable corner cases twice each year, right at the DST transition points. To make this concrete, take US Eastern (UTC -0500): EDT kicks in the minute past 1:59 (EST) on March's second Sunday, and wraps up the minute past 1:59 (EDT) on November's first Sunday:

```python
  UTC   3:MM  4:MM  5:MM  6:MM  7:MM  8:MM
  EST  22:MM 23:MM  0:MM  1:MM  2:MM  3:MM
  EDT  23:MM  0:MM  1:MM  2:MM  3:MM  4:MM

start  22:MM 23:MM  0:MM  1:MM  3:MM  4:MM

  end  23:MM  0:MM  1:MM  1:MM  2:MM  3:MM

```

As DST begins (the "start" line), the wall clock jumps locally from 1:59 straight to 3:00. On that day a wall time written as 2:MM has no real meaning, and so `astimezone(Eastern)` will not produce a value whose `hour == 2` on the day DST starts. As an illustration, here is what comes back at the 2016 Spring forward transition:

```python
>>> import datetime as dt
>>> from tzinfo_examples import HOUR, Eastern
>>> u0 = dt.datetime(2016, 3, 13, 5, tzinfo=dt.timezone.utc)
>>> for i in range(4):
...     u = u0 + i*HOUR
...     t = u.astimezone(Eastern)
...     print(u.time(), 'UTC =', t.time(), t.tzname())
...
05:00:00 UTC = 00:00:00 EST
06:00:00 UTC = 01:00:00 EST
07:00:00 UTC = 03:00:00 EDT
08:00:00 UTC = 04:00:00 EDT

```

As DST finishes (the "end" line), a possibly nastier issue arises: one hour exists that has no unambiguous spelling in local wall time — namely the final hour of daylight time. For Eastern, those are the 5:MM UTC values on the day daylight time wraps up. Locally the wall clock falls back from 1:59 (daylight time) to 1:00 (standard time) once more. So local times written as 1:MM become ambiguous. To echo what the local clock does, `astimezone()` folds two neighboring UTC hours onto the same local hour at that point. Within the Eastern example, both 5:MM and 6:MM UTC values land on 1:MM after conversion to Eastern, yet the earlier ones carry a `fold` attribute of 0 while the later ones carry 1. As an illustration, here is what comes back at the 2016 Fall back transition:

```python
>>> import datetime as dt
>>> from tzinfo_examples import HOUR, Eastern
>>> u0 = dt.datetime(2016, 11, 6, 4, tzinfo=dt.timezone.utc)
>>> for i in range(4):
...     u = u0 + i*HOUR
...     t = u.astimezone(Eastern)
...     print(u.time(), 'UTC =', t.time(), t.tzname(), t.fold)
...
04:00:00 UTC = 00:00:00 EDT 0
05:00:00 UTC = 01:00:00 EDT 0
06:00:00 UTC = 01:00:00 EST 1
07:00:00 UTC = 02:00:00 EST 0

```

Be aware that `datetime` instances which diverge solely in their `fold` attribute count as equal under comparison.

Code that can't tolerate wall-time ambiguity ought to inspect the `fold` attribute directly, or steer clear of hybrid `tzinfo` subclasses; ambiguity never arises with `timezone` or any other fixed-offset `tzinfo` subclass — think of a class modeling EST alone (a fixed -5 hour offset) or EDT alone (a fixed -4 hour offset).

See also

>

[`zoneinfo`](https://docs.python.org/3.14/library/zoneinfo.html#module-zoneinfo)

A simple `timezone` class lives in the `datetime` module (for working with arbitrary fixed offsets relative to UTC), along with its `timezone.utc` attribute (a UTC `timezone` instance).

`zoneinfo` makes the *IANA time zone database* (the Olson database, as it's also known) available in Python, and using it is the recommended approach.

[IANA time zone database](https://www.iana.org/time-zones)

The Time Zone Database (frequently abbreviated tz, tzdata or zoneinfo) holds code and data capturing how local time has evolved across many representative places worldwide. Periodic updates keep it current with changes that political bodies make to time zone boundaries, UTC offsets, and daylight-saving rules.

[Subject index](INDEX.md) · [Previous](us-timezone-complete-example.md) · [Continue](datetime-timezone-class.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: datetime.tzinfo](datetime-tzinfo-class.md) · [Owning module, declaration or section: `tzinfo` objects](datetime-tzinfo-class.md) · [Owning module, declaration or section: tzinfo.fromutc](tzinfo-fromutc.md)
