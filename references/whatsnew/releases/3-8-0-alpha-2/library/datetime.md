# Python 3.8.0 alpha 2 / library / datetime

[bpo-32417](https://bugs.python.org/issue?@action=redirect&bpo=32417): Arithmetic carried out between [`datetime.datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) subclasses and [`datetime.timedelta`](https://docs.python.org/3.14/library/datetime.html#datetime.timedelta) now yields an object whose type matches the `datetime.datetime` subclass. Consequently, [`datetime.datetime.astimezone()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.astimezone) plus alternate constructors such as [`datetime.datetime.now()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.now) and `datetime.fromtimestamp()` invoked with a `tz` argument now *also* keep their subclass.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
