# datetime: `datetime.timedelta`

*class *datetime.timedelta

A span that captures, down to microsecond precision, the gap between a pair of `datetime` or `date` instances.

*class *datetime.timedelta(*days=0*, *seconds=0*, *microseconds=0*, *milliseconds=0*, *minutes=0*, *hours=0*, *weeks=0*)

Every argument is optional, each defaulting to 0. Arguments accept integers or floats and can be positive or negative.

Internally, the object keeps only *days*, *seconds* and *microseconds*. The other arguments get converted into those units:

- A millisecond is converted to 1000 microseconds.

- A minute is converted to 60 seconds.

- An hour is converted to 3600 seconds.

- A week is converted to 7 days.

after which days, seconds and microseconds undergo normalization to make the representation one of a kind, satisfying

- `0 <= microseconds < 1000000`

- `0 <= seconds < 3600*24` (the number of seconds in one day)

- `-999999999 <= days <= 999999999`

The example below shows the way arguments other than *days*, *seconds* and *microseconds* get “merged” and normalized down to those three final attributes:

```python
>>> import datetime as dt
>>> delta = dt.timedelta(
...     days=50,
...     seconds=27,
...     microseconds=10,
...     milliseconds=29000,
...     minutes=5,
...     hours=8,
...     weeks=2
... )
>>> # Only days, seconds, and microseconds remain
>>> delta
datetime.timedelta(days=64, seconds=29156, microseconds=10)

```

Tip

Prefer `import datetime as dt` over `import datetime` or `from datetime import datetime`, which keeps the module from being mixed up with the class. See [How I Import Python’s datetime Module](https://adamj.eu/tech/2019/09/12/how-i-import-pythons-datetime-module/).

When any argument is a float and fractional microseconds result, the leftover fractional microseconds from all the arguments are pooled and that total is rounded to the closest microsecond, breaking ties toward even. When none of the arguments is a float, conversion and normalization run exactly, losing nothing.

Should the normalized days value fall beyond the stated range, [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) is raised.

Be aware that normalizing negative values can look unexpected at first glance. As an illustration:

```python
>>> import datetime as dt
>>> d = dt.timedelta(microseconds=-1)
>>> (d.days, d.seconds, d.microseconds)
(-1, 86399, 999999)

```

Because the way `timedelta` objects print can be misleading, the recipe below yields output that reads more clearly:

```pycon
>>> def pretty_timedelta(td):
...     if td.days >= 0:
...         return str(td)
...     return f'-({-td!s})'
...
>>> d = timedelta(hours=-1)
>>> str(d)  # not human-friendly
'-1 day, 23:00:00'
>>> pretty_timedelta(d)
'-(1:00:00)'

```

Class attributes:

[Subject index](INDEX.md) · [Previous](datetime-datetime-class.md) · [Continue](datetime-tzinfo-class.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: Available types](datetime-date-class.md) · [Previous](timedelta-objects.md) · [Continue](timedelta-min-to-timedelta-seconds.md) · [Owning module, declaration or section: `timedelta` objects](timedelta-objects.md)
