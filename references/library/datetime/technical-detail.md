# datetime — Technical detail

### Technical detail

In broad terms, `d.strftime(fmt)` behaves much like the [`time`](https://docs.python.org/3.14/library/time.html#module-time) module's `time.strftime(fmt, d.timetuple())`, though not every object provides a `timetuple()` method.

With the `datetime.strptime()` and `date.strptime()` class methods, the default is `1900-01-01T00:00:00.000`: whatever components the format string omits get drawn from that default.

Note

Lacking separators, format strings can be ambiguous to parse. As an example, under `%Y%m%d` the string `2026111` could come out either as `2026-11-01` or as `2026-01-11`. Add separators so the input is parsed the way you mean it.

Note

While parsing partial dates that omit a year, `datetime.strptime()` and `date.strptime()` will raise on February 29, since the default year 1900 is *not* a leap year. Be sure to prepend a default leap year onto partial date strings before you parse them.

```pycon
>>> import datetime as dt
>>> value = "2/29"
>>> dt.datetime.strptime(value, "%m/%d")
Traceback (most recent call last):
...
ValueError: day 29 must be in range 1..28 for month 2 in year 1900
>>> dt.datetime.strptime(f"1904 {value}", "%Y %m/%d")
datetime.datetime(1904, 2, 29, 0, 0)

```

Calling `datetime.strptime(date_string, format)` amounts to:

```python
datetime(*(time.strptime(date_string, format)[0:6]))

```

apart from cases where the format carries sub-second pieces or time zone offset details, which `datetime.strptime` handles but `time.strptime` throws away.

With `time` objects you should avoid the format codes for year, month, and day, because `time` objects hold no such fields. Use them regardless and you get 1900 filling in for the year, with 1 for both the month and the day.

With `date` objects you should avoid the format codes for hours, minutes, seconds, and microseconds, because `date` objects hold no such fields. Use them regardless and 0 fills in for each.

By the same logic, dealing with format strings that hold Unicode code points unrepresentable in the current locale's charset is platform-dependent as well. Certain platforms keep such code points intact in the output, whereas on others `strftime` may raise [`UnicodeError`](https://docs.python.org/3.14/library/exceptions.html#UnicodeError) or hand back an empty string in their place.

Notes:

1.

Since the format hinges on the current locale, be cautious about assuming what the output value will look like. The order of fields shifts (say, "month/day/year" against "day/month/year"), and non-ASCII characters may show up in the output.

2.

While the `strptime()` method can parse any year across the full [1, 9999] span, years < 1000 have to be zero-filled out to 4-digit width.

Changed in version 3.2: Earlier releases held the `strftime()` method to years >= 1900 only.

Changed in version 3.3: In version 3.2, `strftime()` method was restricted to years >= 1000.

3.

Paired with the `strptime()` method, the `%p` directive shapes the output hour field only when the `%I` directive is what parses the hour.

4.

In contrast to the [`time`](https://docs.python.org/3.14/library/time.html#module-time) module, the `datetime` module has no support for leap seconds.

5.

Paired with the `strptime()` method, the `%f` directive takes one through six digits and zero-pads on the right. `%f` extends the C standard's set of format characters (but it is built separately within datetime objects, so it is always on hand).

6.

With a naive object, empty strings stand in for the `%z`, `%:z` and `%Z` format codes.

For an aware object:

`%z`

`utcoffset()` is turned into a string shaped like `±HHMM[SS[.ffffff]]`, in which `HH` is a 2-digit string for the count of UTC offset hours, `MM` is a 2-digit string for the count of UTC offset minutes, `SS` is a 2-digit string for the count of UTC offset seconds and `ffffff` is a 6-digit string for the count of UTC offset microseconds. Where the offset comes out to an exact second count, the `ffffff` piece drops off; where it comes out to an exact minute count, the `ffffff` together with the `SS` piece both drop off. To illustrate, where `utcoffset()` returns `timedelta(hours=-3, minutes=-30)`, `%z` becomes the string `'-0330'`.

Changed in version 3.7: A whole number of minutes no longer bounds the UTC offset.

[Subject index](INDEX.md) · [Previous](strftime-and-strptime-format-codes.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md)
