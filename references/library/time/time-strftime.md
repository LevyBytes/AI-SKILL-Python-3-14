# time: `time.strftime()`

time.strftime(*format*[, *t*])

Take a tuple or `struct_time` standing for a time of the kind `gmtime()` or `localtime()` produces and turn it into a string as dictated by the *format* argument. When *t* is omitted, what `localtime()` returns for the current time is used. *format* has to be a string. Whenever some field in *t* falls outside the permitted range, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised.

Any slot in the time tuple may legally hold 0; should that normally be illegal, the value is coerced to a correct one.

Inside the *format* string you can embed the directives below. They appear here without the optional field width and precision specification, and in the `strftime()` result they get swapped for the characters indicated:

| Directive | Meaning | Notes |
| --- | --- | --- |
| `%a` | Locale's abbreviated weekday name. |  |
| `%A` | Locale's full weekday name. |  |
| `%b` | Locale's abbreviated month name. |  |
| `%B` | Locale's full month name. |  |
| `%c` | Locale's appropriate date and time representation. |  |
| `%d` | Day of the month as a decimal number [01,31]. |  |
| `%f` | Microseconds as a decimal number[000000,999999]. | (1) |
| `%H` | Hour (24-hour clock) as a decimal number [00,23]. |  |
| `%I` | Hour (12-hour clock) as a decimal number [01,12]. |  |
| `%j` | Day of the year as a decimal number [001,366]. |  |
| `%m` | Month as a decimal number [01,12]. |  |
| `%M` | Minute as a decimal number [00,59]. |  |
| `%p` | Locale's equivalent of either AM or PM. | (2) |
| `%S` | Second as a decimal number [00,61]. | (3) |
| `%U` | The year's week number, counting Sunday as each week's starting day, given as a decimal number [00,53]. Any day in a fresh year that comes ahead of its first Sunday counts as belonging to week 0. | (4) |
| `%u` | The weekday given as a decimal number [1, 7], where Monday counts as 1 and Sunday as 7. |  |
| `%w` | Weekday as a decimal number [0(Sunday),6]. |  |
| `%W` | The year's week number, counting Monday as each week's starting day, given as a decimal number [00,53]. Any day in a fresh year that comes ahead of its first Monday counts as belonging to week 0. | (4) |
| `%x` | Locale's appropriate date representation. |  |
| `%X` | Locale's appropriate time representation. |  |
| `%y` | Year without century as a decimal number [00,99]. |  |
| `%Y` | Year with century as a decimal number. |  |
| `%z` | The time zone offset, written +HHMM or -HHMM to signal a positive or negative gap relative to UTC/GMT; here H stands for decimal hour digits and M for decimal minute digits [-23:59, +23:59]. [1] |  |
| `%Z` | Time zone name (no characters if no time zone exists). Deprecated. [1] |  |
| `%G` | ISO 8601 year (resembles `%Y` yet obeys the conventions of the ISO 8601 calendar year). Its starting point is whichever week holds the calendar year's first Thursday. |  |
| `%V` | ISO 8601 week number (given as a decimal number [01,53]). Whichever week holds that year's first Thursday becomes its opening week. Each week begins on Monday. |  |
| `%%` | A literal `'%'` character. |  |

Notes:

1.

The `%f` format directive belongs to `strptime()` alone, never to `strftime()`. That said, look as well at [`datetime.datetime.strptime()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.strptime) and [`datetime.datetime.strftime()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.strftime) where the `%f` format directive [applies to microseconds](https://docs.python.org/3.14/library/datetime.html#format-codes).

2.

Paired with the `strptime()` function, the `%p` directive shapes the output hour field only when the `%I` directive does the parsing of the hour.

1.

The span genuinely runs from `0` to `61`; the value `60` holds in timestamps that represent [leap seconds](https://en.wikipedia.org/wiki/Leap_second) and the value `61` is kept around for historical reasons.

2.

Paired with the `strptime()` function, `%U` and `%W` factor into calculations only when both the day of the week and the year are given.

Below is an example: a date format that lines up with the one laid out in the [**RFC 5322**](https://datatracker.ietf.org/doc/html/rfc5322.html) Internet email standard. [1]

```python
>>> from time import gmtime, strftime
>>> strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())
'Thu, 28 Jun 2001 14:17:15 +0000'

```

Some platforms may recognize extra directives, though only those listed above carry a meaning fixed by ANSI C. For the complete set of format codes your platform handles, see the *[strftime(3)](https://manpages.debian.org/strftime(3))* documentation.

On certain platforms an optional field width and precision specification can come right after a directive's leading `'%'`, in this order; that too is not portable. Normally the field width is 2, the exception being `%j` where it is 3.

[Subject index](INDEX.md) · [Previous](time-sleep.md) · [Continue](time-strptime.md) · [Owning module, declaration or section: time](time-time-access-and-conversions.md) · [Owning module, declaration or section: Functions](time-asctime-to-time-ctime.md)
