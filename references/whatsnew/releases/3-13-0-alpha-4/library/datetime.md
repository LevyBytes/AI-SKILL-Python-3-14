# Python 3.13.0 alpha 4 / library / datetime

[gh-49766](https://github.com/python/cpython/issues/49766): Repair the [`date`](https://docs.python.org/3.14/library/datetime.html#datetime.date)-[`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) comparison. The dedicated comparison hooks such as `__eq__` plus `__lt__` will now hand back [`NotImplemented`](https://docs.python.org/3.14/library/constants.html#NotImplemented) whenever one operand is `date` while the other is `datetime`, rather than discarding the time component and the time zone or bluntly declaring "not equal" or throwing [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError). This renders comparisons between `date` and `datetime` subclasses more symmetric and lets a subclass alter the default by overriding those special comparison hooks.

[gh-112451](https://github.com/python/cpython/issues/112451): Forbid subclassing of the pure-Python [`datetime.timezone`](https://docs.python.org/3.14/library/datetime.html#datetime.timezone). That aligns with how the C-extension implementation works. Mariusz Felisiak wrote the patch.

[gh-89039](https://github.com/python/cpython/issues/89039): Whenever replace() runs on a subclass of datetime, date or time, invoke the derived constructor as intended. Formerly only the base class constructor ran.

Additionally, take care to forward non-zero fold values while building subclasses across the various methods. Formerly fold went quietly ignored.

[gh-112919](https://github.com/python/cpython/issues/112919): Accelerate [`datetime.datetime.replace()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.replace), [`datetime.date.replace()`](https://docs.python.org/3.14/library/datetime.html#datetime.date.replace) and [`datetime.time.replace()`](https://docs.python.org/3.14/library/datetime.html#datetime.time.replace).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
