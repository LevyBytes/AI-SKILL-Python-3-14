# datetime: `datetime.fromisoformat()`, `datetime.fromisocalendar()`

*classmethod *datetime.fromisoformat(*date_string*)

Return a `datetime` matching a *date_string* in any valid ISO 8601 format, subject to these exceptions:

1.

Time zone offsets may have fractional seconds.

2.

The `T` separator may be replaced by any single unicode character.

3.

Fractional hours and minutes are not supported.

4.

Reduced precision dates are not currently supported (`YYYY-MM`, `YYYY`).

5.

Extended date representations are not currently supported (`±YYYYYY-MM-DD`).

6.

Ordinal dates are not currently supported (`YYYY-OOO`).

Examples:

```python
>>> import datetime as dt
>>> dt.datetime.fromisoformat('2011-11-04')
datetime.datetime(2011, 11, 4, 0, 0)
>>> dt.datetime.fromisoformat('20111104')
datetime.datetime(2011, 11, 4, 0, 0)
>>> dt.datetime.fromisoformat('2011-11-04T00:05:23')
datetime.datetime(2011, 11, 4, 0, 5, 23)
>>> dt.datetime.fromisoformat('2011-11-04T00:05:23Z')
datetime.datetime(2011, 11, 4, 0, 5, 23, tzinfo=datetime.timezone.utc)
>>> dt.datetime.fromisoformat('20111104T000523')
datetime.datetime(2011, 11, 4, 0, 5, 23)
>>> dt.datetime.fromisoformat('2011-W01-2T00:05:23.283')
datetime.datetime(2011, 1, 4, 0, 5, 23, 283000)
>>> dt.datetime.fromisoformat('2011-11-04 00:05:23.283')
datetime.datetime(2011, 11, 4, 0, 5, 23, 283000)
>>> dt.datetime.fromisoformat('2011-11-04 00:05:23.283+00:00')
datetime.datetime(2011, 11, 4, 0, 5, 23, 283000, tzinfo=datetime.timezone.utc)
>>> dt.datetime.fromisoformat('2011-11-04T00:05:23+04:00')
datetime.datetime(2011, 11, 4, 0, 5, 23,
    tzinfo=datetime.timezone(datetime.timedelta(seconds=14400)))

```

Added in version 3.7.

Changed in version 3.11: Up to this point, the method handled only those formats producible via `date.isoformat()` or `datetime.isoformat()`.

 *classmethod *datetime.fromisocalendar(*year*, *week*, *day*)

Return a `datetime` matching the ISO calendar date named by *year*, *week* and *day*. The datetime’s non-date components take on their usual default values. This serves as the inverse of the function `datetime.isocalendar()`.

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](datetime-objects-classmethod-datetime-utcnow.md) · [Continue](datetime-min-to-datetime-tzinfo.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: `datetime` objects](datetime-datetime-class.md)
