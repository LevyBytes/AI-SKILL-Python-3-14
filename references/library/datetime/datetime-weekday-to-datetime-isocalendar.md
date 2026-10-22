# datetime: `datetime.weekday()`, `datetime.isoweekday()`, `datetime.isocalendar()`

A naive `datetime` is taken to express local time, and this method depends on the platform's C `mktime()` routine to carry out the conversion. Because `datetime` accepts a broader span of values than `mktime()` does on many platforms, calling it may produce [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) or [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) when the moment lies very far back in time or very far ahead.

When the `datetime` is aware, the result is derived like so:

```python
(dt - datetime(1970, 1, 1, tzinfo=timezone.utc)).total_seconds()

```

Note

No method exists that pulls the POSIX timestamp straight from a naive `datetime` that stands for UTC time. Should your program follow that convention while your machine's time zone differs from UTC, you can recover the POSIX timestamp by passing `tzinfo=timezone.utc`:

```python
timestamp = dt.replace(tzinfo=timezone.utc).timestamp()

```

or by computing the timestamp by hand:

```python
timestamp = (dt - datetime(1970, 1, 1)) / timedelta(seconds=1)

```

Added in version 3.3.

Changed in version 3.6: The `timestamp()` method consults the `fold` attribute to tell apart the two times within a repeated interval.

 datetime.weekday()

Give back the weekday as an integer, with Monday being 0 and Sunday being 6. Equivalent to `self.date().weekday()`. See also `isoweekday()`.

 datetime.isoweekday()

Give back the weekday as an integer, with Monday being 1 and Sunday being 7. Equivalent to `self.date().isoweekday()`. See also `weekday()`, `isocalendar()`.

 datetime.isocalendar()

Give back a [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) carrying three fields: `year`, `week` and `weekday`. Equivalent to `self.date().isocalendar()`.

[Subject index](INDEX.md) · [Continue](datetime-isoformat.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: `datetime` objects](datetime-datetime-class.md) · [Owning module, declaration or section: datetime.timestamp](datetime-astimezone-to-datetime-timestamp.md) · [Preceding source contract and version conditions](datetime-astimezone-to-datetime-timestamp.md)
