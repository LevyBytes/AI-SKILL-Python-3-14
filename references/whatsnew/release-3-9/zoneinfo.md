# What's New In Python 3.9 / zoneinfo - datetime, zoneinfo

### New Modules

### zoneinfo

The [`zoneinfo`](https://docs.python.org/3.14/library/zoneinfo.html#module-zoneinfo) module delivers IANA time zone database support into the standard library. It contributes [`zoneinfo.ZoneInfo`](https://docs.python.org/3.14/library/zoneinfo.html#zoneinfo.ZoneInfo), a concrete [`datetime.tzinfo`](https://docs.python.org/3.14/library/datetime.html#datetime.tzinfo) implementation that draws on the platform's time zone data.

Example:

```python
>>> from zoneinfo import ZoneInfo
>>> import datetime as dt

>>> # Daylight saving time
>>> when = dt.datetime(2020, 10, 31, 12, tzinfo=ZoneInfo("America/Los_Angeles"))
>>> print(when)
2020-10-31 12:00:00-07:00
>>> when.tzname()
'PDT'

>>> # Standard time
>>> when += dt.timedelta(days=7)
>>> print(when)
2020-11-07 12:00:00-08:00
>>> print(when.tzname())
PST

```

For systems lacking the bundled IANA database, the [tzdata](https://pypi.org/project/tzdata/) module serves as a fallback data source; the CPython core team maintains it and publishes it on PyPI as a first-party package.

See also

[**PEP 615**](https://peps.python.org/pep-0615/) ? Support for the IANA Time Zone Database in the Standard Library

PEP written and implemented by Paul Ganssle

[Subject index](INDEX.md) · [Previous source section](other-language-changes.md) · [Next source section](graphlib.md) · [Release/subject declaration](summary-release-highlights.md)
