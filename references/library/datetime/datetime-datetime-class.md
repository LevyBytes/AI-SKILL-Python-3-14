# datetime: `datetime.datetime`, `datetime.today()`, `datetime.now()`

*class *datetime.datetime

A pairing of a date together with a time. Attributes: `year`, `month`, `day`, `hour`, `minute`, `second`, `microsecond`, and `tzinfo`.

### `datetime` objects

A `datetime` object is a lone object that bundles together every piece of data held by a `date` object alongside the data held by a `time` object.

Just as a `date` object does, `datetime` works from the current Gregorian calendar projected forward and backward without limit; and just as a `time` object does, `datetime` treats each day as containing precisely 3600*24 seconds.

Constructor:

 *class *datetime.datetime(*year*, *month*, *day*, *hour=0*, *minute=0*, *second=0*, *microsecond=0*, *tzinfo=None*, ***, *fold=0*)

You must supply the *year*, *month* and *day* arguments. *tzinfo* may be `None`, or an instance of a `tzinfo` subclass. Every other argument has to be an integer falling within these ranges:

- `MINYEAR <= year <= MAXYEAR`,

- `1 <= month <= 12`,

- `1 <= day <= number of days in the given month and year`,

- `0 <= hour < 24`,

- `0 <= minute < 60`,

- `0 <= second < 60`,

- `0 <= microsecond < 1000000`,

- `fold in [0, 1]`.

Supplying an argument that falls outside those ranges causes [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) to be raised.

Changed in version 3.6: Added the *fold* parameter.

Other constructors, all class methods:

 *classmethod *datetime.today()

Return the present local date and time, having `tzinfo` set to `None`.

Equivalent to:

```python
datetime.fromtimestamp(time.time())

```

See also `now()`, `fromtimestamp()`.

In behavior this method matches `now()`, except that it takes no `tz` parameter.

 *classmethod *datetime.now(*tz=None*)

Return the present local date and time.

When the optional *tz* argument is `None` or omitted, the behavior resembles `today()`, except that, where the platform allows it, it offers finer precision than what a round trip through a [`time.time()`](https://docs.python.org/3.14/library/time.html#time.time) timestamp could provide (on systems exposing the C `gettimeofday()` function, for instance).

Should *tz* be something other than `None`, it has to be an instance of a `tzinfo` subclass, and the present date and time get converted into *tz*’s time zone.

Reach for this function ahead of `today()` and `utcnow()`.

Note

Depending on how precise the underlying clock is, back-to-back calls to `datetime.now()` can hand back the very same instant.

[Subject index](INDEX.md) · [Previous](datetime-time-class.md) · [Continue](datetime-timedelta-class.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: Available types](datetime-date-class.md) · [Previous](examples-of-usage-date.md) · [Continue](datetime-objects-classmethod-datetime-utcnow.md)
