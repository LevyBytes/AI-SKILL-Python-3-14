# zoneinfo - Using `ZoneInfo`

### Using `ZoneInfo`

As a concrete realization of the [`datetime.tzinfo`](https://docs.python.org/3.14/library/datetime.html#datetime.tzinfo) abstract base class, `ZoneInfo` is meant to be hooked up to `tzinfo` — whether through the constructor, the [`datetime.replace`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.replace) method, or [`datetime.astimezone`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.astimezone):

```python
>>> from zoneinfo import ZoneInfo
>>> import datetime as dt

>>> when = dt.datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
>>> print(when)
2020-10-31 12:00:00-07:00

>>> when.tzname()
'PDT'

```

Datetimes built like this play nicely with datetime arithmetic and deal with daylight saving time transitions on their own, needing no extra effort:

```python
>>> when_add = when + dt.timedelta(days=1)

>>> print(when_add)
2020-11-01 12:00:00-08:00

>>> when_add.tzname()
'PST'

```

These time zones honor the [`fold`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.fold) attribute that arrived with [**PEP 495**](https://peps.python.org/pep-0495/) as well. Across offset transitions that produce ambiguous times (a daylight saving time to standard time shift, for instance), `fold=0` selects the offset from *before* the transition while `fold=1` selects the offset *after* it, as in:

```python
>>> when = dt.datetime(2020, 11, 1, 1, tzinfo=ZoneInfo("America/Los_Angeles"))
>>> print(when)
2020-11-01 01:00:00-07:00

>>> print(when.replace(fold=1))
2020-11-01 01:00:00-08:00

```

Converting in from a different time zone sets the fold to the right value:

```python
>>> LOS_ANGELES = ZoneInfo("America/Los_Angeles")
>>> when_utc = dt.datetime(2020, 11, 1, 8, tzinfo=dt.timezone.utc)

>>> # Before the PDT -> PST transition
>>> print(when_utc.astimezone(LOS_ANGELES))
2020-11-01 01:00:00-07:00

>>> # After the PDT -> PST transition
>>> print((when_utc + dt.timedelta(hours=1)).astimezone(LOS_ANGELES))
2020-11-01 01:00:00-08:00

```

[Subject index](INDEX.md) · [Previous](zoneinfo-iana-time-zone-support.md) · [Continue](data-sources.md) · [Owning module, declaration or section: zoneinfo](zoneinfo-iana-time-zone-support.md)
