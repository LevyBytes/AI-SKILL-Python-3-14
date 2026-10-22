# datetime: `datetime.isoformat()`

datetime.isoformat(*sep='T'*, *timespec='auto'*)

Give back a string that renders the date and time in ISO 8601 format:

- `YYYY-MM-DDTHH:MM:SS.ffffff`, if `microsecond` is not 0

- `YYYY-MM-DDTHH:MM:SS`, if `microsecond` is 0

Should `utcoffset()` not return `None`, the string gains a suffix that states the UTC offset:

- `YYYY-MM-DDTHH:MM:SS.ffffff+HH:MM[:SS[.ffffff]]`, if `microsecond` is not 0

- `YYYY-MM-DDTHH:MM:SS+HH:MM[:SS[.ffffff]]`, if `microsecond` is 0

Examples:

```python
>>> import datetime as dt
>>> dt.datetime(2019, 5, 18, 15, 17, 8, 132263).isoformat()
'2019-05-18T15:17:08.132263'
>>> dt.datetime(2019, 5, 18, 15, 17, tzinfo=dt.timezone.utc).isoformat()
'2019-05-18T15:17:00+00:00'

```

The optional *sep* argument (which defaults to `'T'`) is a single-character separator dropped between the date and time halves of the output. For instance:

```python
>>> import datetime as dt
>>> class TZ(dt.tzinfo):
...     """A time zone with an arbitrary, constant -06:39 offset."""
...     def utcoffset(self, when):
...         return dt.timedelta(hours=-6, minutes=-39)
...
>>> dt.datetime(2002, 12, 25, tzinfo=TZ()).isoformat(' ')
'2002-12-25 00:00:00-06:39'
>>> dt.datetime(2009, 11, 27, microsecond=100, tzinfo=TZ()).isoformat()
'2009-11-27T00:00:00.000100-06:39'

```

The optional *timespec* argument sets how many extra time components get included (`'auto'` by default). Its value may be any of these:

- `'auto'`: Same as `'seconds'` if `microsecond` is 0, same as `'microseconds'` otherwise.

- `'hours'`: Include the `hour` in the two-digit `HH` format.

- `'minutes'`: Include `hour` and `minute` in `HH:MM` format.

- `'seconds'`: Include `hour`, `minute`, and `second` in `HH:MM:SS` format.

- `'milliseconds'`: Include full time, but truncate fractional second part to milliseconds. `HH:MM:SS.sss` format.

- `'microseconds'`: Include full time in `HH:MM:SS.ffffff` format.

Note

Time components left out are cut off rather than rounded.

[`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised when the *timespec* argument is invalid:

```python
>>> import datetime as dt
>>> dt.datetime.now().isoformat(timespec='minutes')
'2002-12-25T00:00'
>>> my_datetime = dt.datetime(2015, 1, 1, 12, 30, 59, 0)
>>> my_datetime.isoformat(timespec='microseconds')
'2015-01-01T12:30:59.000000'

```

Changed in version 3.6: Added the *timespec* parameter.

[Subject index](INDEX.md) · [Previous](datetime-weekday-to-datetime-isocalendar.md) · [Continue](datetime-str-to-datetime-format.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: `datetime` objects](datetime-datetime-class.md)
