# datetime: `datetime.__str__()`, `datetime.ctime()`, `datetime.strftime()`, `datetime.__format__()`

datetime.__str__()

For some `datetime` instance `d`, `str(d)` is the same as `d.isoformat(' ')`.

 datetime.ctime()

Give back a string that renders the date and time:

```python
>>> import datetime as dt
>>> dt.datetime(2002, 12, 4, 20, 30, 40).ctime()
'Wed Dec  4 20:30:40 2002'

```

That output string carries *no* time zone detail, whether the input happens to be aware or naive.

`d.ctime()` is the same as:

```python
time.ctime(time.mktime(d.timetuple()))

```

on platforms where the native C `ctime()` function (the one [`time.ctime()`](https://docs.python.org/3.14/library/time.html#time.ctime) calls, though `datetime.ctime()` itself does not call it) follows the C standard.

 datetime.strftime(*format*)

Give back a string that renders the date and time, driven by an explicit format string. See also strftime() and strptime() behavior and `datetime.isoformat()`.

 datetime.__format__(*format*)

Same as `datetime.strftime()`. This lets you hand a format string to a `datetime` object inside [formatted string literals](https://docs.python.org/3.14/reference/lexical_analysis.html#f-strings) and while using [`str.format()`](https://docs.python.org/3.14/library/stdtypes.html#str.format). See also strftime() and strptime() behavior and `datetime.isoformat()`.

[Subject index](INDEX.md) · [Previous](datetime-isoformat.md) · [Continue](datetime-usage-overview.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: `datetime` objects](datetime-datetime-class.md)
