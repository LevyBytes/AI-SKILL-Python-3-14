# datetime: `timedelta.min`, `timedelta.max`, `timedelta.resolution`, `timedelta.days`, `timedelta.seconds`

timedelta.min

The most negative `timedelta` object, `timedelta(-999999999)`.

 timedelta.max

The most positive `timedelta` object, `timedelta(days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999)`.

 timedelta.resolution

The smallest possible difference between non-equal `timedelta` objects, `timedelta(microseconds=1)`.

Keep in mind that, owing to normalization, `timedelta.max` exceeds `-timedelta.min`. As a `timedelta` object, `-timedelta.max` cannot be represented.

Instance attributes (read-only):

 timedelta.days

Between -999,999,999 and 999,999,999 inclusive.

 timedelta.seconds

Between 0 and 86,399 inclusive.

Caution

A fairly frequent mistake is for code to reach for this attribute by accident when what it really wants is the `total_seconds()` value instead:

```pycon
>>> import datetime as dt
>>> duration = dt.timedelta(seconds=11235813)
>>> duration.days, duration.seconds
(130, 3813)
>>> duration.total_seconds()
11235813.0

```

[Subject index](INDEX.md) · [Previous](datetime-timedelta-class.md) · [Continue](timedelta-microseconds-to-timedelta-total-seconds.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: datetime.timedelta](datetime-timedelta-class.md) · [Owning module, declaration or section: `timedelta` objects](timedelta-objects.md)
