# datetime: `datetime.utcnow()`, `datetime.fromtimestamp()`, `datetime.utcfromtimestamp()`, `datetime.fromordinal()`, `datetime.combine()`

*classmethod *datetime.utcnow()

Return the present UTC date and time, having `tzinfo` set to `None`.

This resembles `now()`, but hands back the present UTC date and time as a naive `datetime` object. You can produce an aware current UTC datetime by invoking `datetime.now(timezone.utc)`. See also `now()`.

Warning

Since a great many `datetime` methods regard naive `datetime` objects as local times, working with aware datetimes for UTC values is the preferred approach. Accordingly, the suggested means of building an object that stands for the current moment in UTC is to call `datetime.now(timezone.utc)`.

Deprecated since version 3.12: Use `datetime.now()` with `UTC` instead.

 *classmethod *datetime.fromtimestamp(*timestamp*, *tz=None*)

Return the local date and time matching the POSIX timestamp, of the kind handed back by [`time.time()`](https://docs.python.org/3.14/library/time.html#time.time). Where the optional *tz* argument is `None` or left out, the timestamp gets mapped to the platform’s local date and time, and the `datetime` object handed back is naive.

Should *tz* be something other than `None`, it has to be an instance of a `tzinfo` subclass, and the timestamp gets converted into *tz*’s time zone.

`fromtimestamp()` can raise [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) when the timestamp lies beyond the span of values the platform C `localtime()` or `gmtime()` functions handle, plus [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) when `localtime()` or `gmtime()` fails. Frequently this span is held to years from 1970 through 2038. Be aware that on non-POSIX systems whose timestamp concept folds in leap seconds, `fromtimestamp()` disregards those leap seconds, so it becomes possible for two timestamps a second apart to map to the same `datetime` object. Favor this method over `utcfromtimestamp()`.

Changed in version 3.3: Where the timestamp falls beyond the span of values the platform C `localtime()` or `gmtime()` functions support, raise [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) rather than [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). Upon `localtime()` or `gmtime()` failure, raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) rather than `ValueError`.

Changed in version 3.6: `fromtimestamp()` may return instances with `fold` set to 1.

 *classmethod *datetime.utcfromtimestamp(*timestamp*)

Return the UTC `datetime` matching the POSIX timestamp, having `tzinfo` set to `None`. (The object produced is naive.)

This can raise [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) when the timestamp lies beyond the span of values the platform C `gmtime()` function handles, plus [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) when `gmtime()` fails. Frequently this span is held to years from 1970 through 2038.

To obtain an aware `datetime` object, invoke `fromtimestamp()`:

```python
datetime.fromtimestamp(timestamp, timezone.utc)

```

On POSIX compliant platforms, this matches the following expression:

```python
datetime(1970, 1, 1, tzinfo=timezone.utc) + timedelta(seconds=timestamp)

```

apart from the fact that the second formula always handles the complete year span: from `MINYEAR` through `MAXYEAR` inclusive.

Warning

Since a great many `datetime` methods regard naive `datetime` objects as local times, working with aware datetimes for UTC values is the preferred approach. Accordingly, the suggested means of building an object that stands for a particular timestamp in UTC is to call `datetime.fromtimestamp(timestamp, tz=timezone.utc)`.

Changed in version 3.3: Where the timestamp falls beyond the span of values the platform C `gmtime()` function supports, raise [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) rather than [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). Upon `gmtime()` failure, raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) rather than `ValueError`.

Changed in version 3.15: Now takes any real number for *timestamp*, rather than only an integer or float.

Deprecated since version 3.12: Use `datetime.fromtimestamp()` with `UTC` instead.

 *classmethod *datetime.fromordinal(*ordinal*)

Return the `datetime` matching the proleptic Gregorian ordinal, in which January 1 of year 1 carries ordinal 1. [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised except when `1 <= ordinal <= datetime.max.toordinal()`. The hour, minute, second and microsecond of the outcome are each 0, with `tzinfo` set to `None`.

 *classmethod *datetime.combine(*date*, *time*, *tzinfo=time.tzinfo*)

Return a fresh `datetime` object whose date components match those of the supplied `date` object, and whose time components match those of the supplied `time` object. When the *tzinfo* argument is given, that value sets the `tzinfo` attribute of the outcome; otherwise the `tzinfo` attribute belonging to the *time* argument is used. Should the *date* argument be a `datetime` object, its time components and `tzinfo` attributes get discarded.

For every `datetime` object `d`, `d == datetime.combine(d.date(), d.time(), d.tzinfo)`.

Changed in version 3.6: Added the *tzinfo* argument.

[Subject index](INDEX.md) · [Previous](datetime-datetime-class.md) · [Continue](datetime-isoformat-parsing.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: `datetime` objects](datetime-datetime-class.md)
