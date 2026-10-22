# datetime — `datetime` — Basic date and time types

### `datetime` — Basic date and time types

**Source code:** [Lib/datetime.py](https://github.com/python/cpython/tree/3.14/Lib/datetime.py)

---

Classes for working with dates and times are provided by the `datetime` module.

Although arithmetic on dates and times works, the design emphasizes pulling attributes efficiently so they can be reformatted and adjusted.

Tip

Skip to the format codes.

See also

Module [`calendar`](https://docs.python.org/3.14/library/calendar.html#module-calendar)

General calendar related functions.

Module [`time`](https://docs.python.org/3.14/library/time.html#module-time)

Time access and conversions.

Module [`zoneinfo`](https://docs.python.org/3.14/library/zoneinfo.html#module-zoneinfo)

Concrete time zones representing the IANA time zone database.

Package [dateutil](https://dateutil.readthedocs.io/en/stable/)

Third-party library with expanded time zone and parsing support.

Package [DateType](https://pypi.org/project/DateType/)

A third-party library that adds separate static types so that, for instance, [static type checkers](https://docs.python.org/3.14/glossary.html#term-static-type-checker) can tell naive datetimes apart from aware ones.

[Subject index](INDEX.md) · [Continue](aware-and-naive-objects.md)
