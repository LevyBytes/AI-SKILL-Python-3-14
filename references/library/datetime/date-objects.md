# datetime: `date.today()`, `date.fromtimestamp()`, `date.fromordinal()`, `date.fromisoformat()`, `date.fromisocalendar()`

*classmethod *date.today()

Return the current local date.

This is equivalent to `date.fromtimestamp(time.time())`.

 *classmethod *date.fromtimestamp(*timestamp*)

Give back the local date that matches the POSIX *timestamp*, of the kind [`time.time()`](https://docs.python.org/3.14/library/time.html#time.time) produces.

It can raise [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) when the timestamp lies outside the range the platform’s C `localtime()` function handles, and [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) if `localtime()` fails. Frequently this is capped at the years from 1970 through 2038. Note that on non-POSIX systems whose timestamp concept folds in leap seconds, `fromtimestamp()` disregards those leap seconds.

Changed in version 3.3: Where the timestamp falls beyond the value range the platform C `localtime()` function handles, raise [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) rather than [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError). On a `localtime()` failure, raise [`OSError`](https://docs.python.org/3.14/library/exceptions.html#OSError) rather than `ValueError`.

 *classmethod *date.fromordinal(*ordinal*)

Give back the date that matches the proleptic Gregorian *ordinal*, in which ordinal 1 belongs to January 1 of year 1.

Unless `1 <= ordinal <= date.max.toordinal()`, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised. For any date `d`, `date.fromordinal(d.toordinal()) == d`.

 *classmethod *date.fromisoformat(*date_string*)

Give back a `date` that matches a *date_string* supplied in whichever valid ISO 8601 format, save for these exceptions:

1.

Reduced precision dates are not currently supported (`YYYY-MM`, `YYYY`).

2.

Extended date representations are not currently supported (`±YYYYYY-MM-DD`).

3.

Ordinal dates are not currently supported (`YYYY-OOO`).

Examples:

```python
>>> import datetime as dt
>>> dt.date.fromisoformat('2019-12-04')
datetime.date(2019, 12, 4)
>>> dt.date.fromisoformat('20191204')
datetime.date(2019, 12, 4)
>>> dt.date.fromisoformat('2021-W01-1')
datetime.date(2021, 1, 4)

```

Added in version 3.7.

Changed in version 3.11: Previously, this method only supported the format `YYYY-MM-DD`.

 *classmethod *date.fromisocalendar(*year*, *week*, *day*)

Give back a `date` that matches the ISO calendar date pinned down by *year*, *week* and *day*. It inverts the function `date.isocalendar()`.

Added in version 3.8.

[Subject index](INDEX.md) · [Previous](datetime-date-class.md) · [Continue](date-min-to-date-month.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: datetime.date](datetime-date-class.md) · [Owning module, declaration or section: `date` objects](datetime-date-class.md)
