# time: `time.struct_time`

*class *time.struct_time

This is the type of the time value sequence that `gmtime()`, `localtime()`, and `strptime()` give back. It is an object carrying a [named tuple](https://docs.python.org/3.14/glossary.html#term-named-tuple) interface: you can reach its values by index and by attribute name. These values are present:

| Index | Attribute | Values |
| --- | --- | --- |
| 0 | tm_year?? | (for example, 1993) |
| 1 | tm_mon?? | range [1, 12] |
| 2 | tm_mday?? | range [1, 31] |
| 3 | tm_hour?? | range [0, 23] |
| 4 | tm_min?? | range [0, 59] |
| 5 | tm_sec?? | range [0, 61]; see Note (2) in `strftime()` |
| 6 | tm_wday?? | range [0, 6]; Monday is 0 |
| 7 | tm_yday?? | range [1, 366] |
| 8 | tm_isdst?? | 0, 1 or -1; see below |
| N/A | tm_zone?? | abbreviation of timezone name |
| N/A | tm_gmtoff?? | offset east of UTC in seconds |

Keep in mind that, unlike the C structure, the month value spans [1, 12] rather than [0, 11].

Within calls to `mktime()`, `tm_isdst` may be set to 1 while daylight savings time is in effect and to 0 while it is not. Setting it to -1 signals that the state is unknown, and the right one will typically get filled in.

Should a tuple of the wrong length reach a function expecting a `struct_time`, or should it carry elements of the wrong type, a [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) is raised.

[Subject index](INDEX.md) · [Previous](time-strptime.md) · [Continue](functions.md) · [Owning module, declaration or section: time](time-time-access-and-conversions.md) · [Owning module, declaration or section: Functions](time-asctime-to-time-ctime.md)
