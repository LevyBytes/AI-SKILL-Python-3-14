# time: `time.strptime()`

time.strptime(*string*[, *format*])

Read a string that represents a time, following a format. What comes back is a `struct_time` of the kind `gmtime()` or `localtime()` returns.

The *format* parameter relies on the same directives that `strftime()` employs; it falls back to `"%a %b %d %H:%M:%S %Y"`, lining up with the formatting `ctime()` returns. Should *string* not parse under *format*, or should leftover data remain after parsing, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised. Whatever cannot be inferred more precisely gets filled in from these defaults: `(1900, 1, 1, 0, 0, 0, 0, 1, -1)`. Both *string* and *format* are required to be strings.

For example:

```python
>>> import time
>>> time.strptime("30 Nov 00", "%d %b %y")
time.struct_time(tm_year=2000, tm_mon=11, tm_mday=30, tm_hour=0, tm_min=0,
                 tm_sec=0, tm_wday=3, tm_yday=335, tm_isdst=-1)

```

How the `%Z` directive is supported rests on the values held in `tzname` together with whether `daylight` is true. For that reason it is platform-specific, the exception being UTC and GMT which are always recognized (and treated as non-daylight savings timezones).

The only directives supported are the ones spelled out in the documentation. Since `strftime()` is built per platform, it can at times present more directives than those listed. `strptime()` however owes nothing to any platform and therefore need not support every available directive that goes undocumented as supported.

[Subject index](INDEX.md) · [Previous](time-strftime.md) · [Continue](time-struct-time-class.md) · [Owning module, declaration or section: time](time-time-access-and-conversions.md) · [Owning module, declaration or section: Functions](time-asctime-to-time-ctime.md)
