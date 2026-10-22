# time — Timezone Constants

### Timezone Constants

 time.altzone

How far the local DST timezone sits from UTC, measured in seconds to the west, provided one has been defined. The figure goes negative when the local DST timezone lies east of UTC (as happens in Western Europe, the UK included). Consult it only when `daylight` is nonzero. See note below.

 time.daylight

Holds a nonzero value whenever a DST timezone has been defined. See note below.

 time.timezone

How far the local (non-DST) timezone sits from UTC, given in seconds to the west (a negative figure across most of Western Europe, positive in the US, and zero in the UK). See note below.

 time.tzname

A two-element tuple of strings: the first names the local non-DST timezone and the second names the local DST timezone. When no DST timezone exists, the second string ought to be ignored. See note below.

Note

Each of the Timezone constants listed above (`altzone`, `daylight`, `timezone`, and `tzname`) takes its value from whatever timezone rules were in force when the module loaded or when `tzset()` last ran, so it can be wrong for moments in the past. The advice is to read timezone details from the `tm_gmtoff` and `tm_zone` fields that `localtime()` returns.

See also

Module [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime)

A more object-oriented way of working with dates and times.

Module [`locale`](https://docs.python.org/3.14/library/locale.html#module-locale)

Services for internationalization. Whatever locale is set will sway how numerous format specifiers in `strftime()` and `strptime()` are read.

Module [`calendar`](https://docs.python.org/3.14/library/calendar.html#module-calendar)

Assorted calendar-oriented functions. [`timegm()`](https://docs.python.org/3.14/library/calendar.html#calendar.timegm) undoes what `gmtime()` from this very module does.

Footnotes

[Subject index](INDEX.md) · [Previous](time-clock-uptime-to-time-clock-realtime.md) · [Owning module, declaration or section: time](time-time-access-and-conversions.md)
