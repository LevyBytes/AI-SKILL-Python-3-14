# datetime`strftime()` and `strptime()` format codes

### `strftime()` and `strptime()` format codes

The format codes these methods take let you parse and format dates:

```python
>>> import datetime as dt
>>> dt.datetime.strptime('31/01/22 23:59:59.999999',
...                      '%d/%m/%y %H:%M:%S.%f')
datetime.datetime(2022, 1, 31, 23, 59, 59, 999999)
>>> _.strftime('%a %d %b %Y, %I:%M%p')
'Mon 31 Jan 2022, 11:59PM'

```

Below is the complete roster of format codes mandated by the 1989 C standard; every one of them functions on any platform offering a standard C implementation.

| Directive | Meaning | Example | Notes |
| --- | --- | --- | --- |
| `%a` | Weekday as locale’s abbreviated name. | Sun, Mon, …, Sat (en_US); So, Mo, …, Sa (de_DE) | (1) |
| `%A` | Weekday as locale’s full name. | Sunday, Monday, …, Saturday (en_US); Sonntag, Montag, …, Samstag (de_DE) | (1) |
| `%w` | Weekday given as a decimal digit running from 0 (Sunday) through 6 (Saturday). | 0, 1, …, 6 |  |
| `%d` | Day of the month as a zero-padded decimal number. | 01, 02, …, 31 | (9) |
| `%b` | Month as locale’s abbreviated name. | Jan, Feb, …, Dec (en_US); Jan, Feb, …, Dez (de_DE) | (1) |
| `%B` | Month as locale’s full name. | January, February, …, December (en_US); Januar, Februar, …, Dezember (de_DE) | (1) |
| `%m` | Month as a zero-padded decimal number. | 01, 02, …, 12 | (9) |
| `%y` | Year without century as a zero-padded decimal number. | 00, 01, …, 99 | (9) |
| `%Y` | Year with century as a decimal number. | 0001, 0002, …, 2013, 2014, …, 9998, 9999 | (2) |
| `%H` | Hour (24-hour clock) as a zero-padded decimal number. | 00, 01, …, 23 | (9) |
| `%I` | Hour (12-hour clock) as a zero-padded decimal number. | 01, 02, …, 12 | (9) |
| `%p` | Locale’s equivalent of either AM or PM. | AM, PM (en_US); am, pm (de_DE) | (1), (3) |
| `%M` | Minute as a zero-padded decimal number. | 00, 01, …, 59 | (9) |
| `%S` | Second as a zero-padded decimal number. | 00, 01, …, 59 | (4), (9) |
| `%f` | Microsecond as a decimal number, zero-padded to 6 digits. | 000000, 000001, …, 999999 | (5) |
| `%z` | UTC offset in the form `±HHMM[SS[.ffffff]]` (empty string if the object is naive). | (empty), +0000, -0400, +1030, +063415, -030712.345216 | (6) |
| `%Z` | Time zone name (empty string if the object is naive). | (empty), UTC, GMT | (6) |
| `%j` | Day of the year as a zero-padded decimal number. | 001, 002, …, 366 | (9) |
| `%U` | The year's week count (taking Sunday for the week's opening day) rendered as a zero-padded decimal. Any days that fall in a fresh year ahead of its first Sunday count as week 0. | 00, 01, …, 53 | (7), (9) |
| `%W` | The year's week count (taking Monday for the week's opening day) rendered as a zero-padded decimal. Any days that fall in a fresh year ahead of its first Monday count as week 0. | 00, 01, …, 53 | (7), (9) |
| `%c` | Locale’s appropriate date and time representation. | Tue Aug 16 21:30:00 1988 (en_US); Di 16 Aug 21:30:00 1988 (de_DE) | (1) |
| `%x` | Locale’s appropriate date representation. | 08/16/88 (None); 08/16/1988 (en_US); 16.08.1988 (de_DE) | (1) |
| `%X` | Locale’s appropriate time representation. | 21:30:00 (en_US); 21:30:00 (de_DE) | (1) |
| `%%` | A literal `'%'` character. | % |  |

For convenience, several extra directives beyond what the C89 standard demands are bundled in too. Each of these parameters maps to an ISO 8601 date value.

| Directive | Meaning | Example | Notes |
| --- | --- | --- | --- |
| `%G` | ISO 8601 year, century included, denoting whichever year holds most of the ISO week (`%V`). | 0001, 0002, …, 2013, 2014, …, 9998, 9999 | (8) |
| `%u` | ISO 8601 weekday as a decimal number where 1 is Monday. | 1, 2, …, 7 |  |
| `%V` | ISO 8601 week rendered as a decimal, with Monday taken as the week's opening day. Week 01 is whichever week holds Jan 4. | 01, 02, …, 53 | (8), (9) |
| `%:z` | UTC offset in the form `±HH:MM[:SS[.ffffff]]` (empty string if the object is naive). | (empty), +00:00, -04:00, +10:30, +06:34:15, -03:07:12.345216 | (6) |

When paired with the `strftime()` method, these might be missing on some platforms. The ISO 8601 year and ISO 8601 week directives cannot stand in for the ordinary year and week-number directives listed above. Should you call `strptime()` with ISO 8601 directives that are incomplete or ambiguous, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) results.

Which format codes are fully supported differs from one platform to the next, since Python defers to the platform C library's `strftime()` function, and such platform-to-platform variation happens often. For the complete roster of format codes your platform backs, look at the *[strftime(3)](https://manpages.debian.org/strftime(3))* documentation. Platforms additionally diverge in the way they treat unsupported format specifiers.

Added in version 3.6: `%G`, `%u` and `%V` were added.

Added in version 3.12: `%:z` was added.

[Subject index](INDEX.md) · [Previous](strftime-and-strptime-behavior.md) · [Continue](technical-detail.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md)
