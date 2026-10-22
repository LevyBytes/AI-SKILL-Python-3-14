# datetime: `time.isoformat()`, `time.__str__()`, `time.strftime()`, `time.__format__()`

time.isoformat(*timespec='auto'*)

Give back a string that renders the time in ISO 8601 format, one of:

- `HH:MM:SS.ffffff`, if `microsecond` is not 0

- `HH:MM:SS`, if `microsecond` is 0

- `HH:MM:SS.ffffff+HH:MM[:SS[.ffffff]]`, if `utcoffset()` does not return `None`

- `HH:MM:SS+HH:MM[:SS[.ffffff]]`, if `microsecond` is 0 and `utcoffset()` does not return `None`

The optional *timespec* argument sets how many extra time components get included (`'auto'` by default). Its value may be any of these:

- `'auto'`: Same as `'seconds'` if `microsecond` is 0, same as `'microseconds'` otherwise.

- `'hours'`: Include the `hour` in the two-digit `HH` format.

- `'minutes'`: Include `hour` and `minute` in `HH:MM` format.

- `'seconds'`: Include `hour`, `minute`, and `second` in `HH:MM:SS` format.

- `'milliseconds'`: Include full time, but truncate fractional second part to milliseconds. `HH:MM:SS.sss` format.

- `'microseconds'`: Include full time in `HH:MM:SS.ffffff` format.

Note

Time components left out are cut off rather than rounded.

[`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) gets raised when the *timespec* argument is invalid.

Example:

```python
>>> import datetime as dt
>>> dt.time(hour=12, minute=34, second=56, microsecond=123456).isoformat(timespec='minutes')
'12:34'
>>> my_time = dt.time(hour=12, minute=34, second=56, microsecond=0)
>>> my_time.isoformat(timespec='microseconds')
'12:34:56.000000'
>>> my_time.isoformat(timespec='auto')
'12:34:56'

```

Changed in version 3.6: Added the *timespec* parameter.

 time.__str__()

For some time `t`, `str(t)` is the same as `t.isoformat()`.

 time.strftime(*format*)

Give back a string that renders the time, driven by an explicit format string. See also strftime() and strptime() behavior and `time.isoformat()`.

 time.__format__(*format*)

Same as `time.strftime()`. This lets you hand a format string to a `time` object inside [formatted string literals](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings) and while using [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format). See also strftime() and strptime() behavior and `time.isoformat()`.

[Subject index](INDEX.md) · [Previous](time-replace.md) · [Continue](time-utcoffset-to-time-tzname.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: datetime.time](datetime-time-class.md) · [Owning module, declaration or section: `time` objects](datetime-time-class.md)
