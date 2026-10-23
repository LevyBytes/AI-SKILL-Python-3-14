# What's New In Python 3.6 / datetime - datetime

### datetime

Both the [`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) and [`time`](https://docs.python.org/3.14/library/datetime.html#datetime.time) classes gained the new [`fold`](https://docs.python.org/3.14/library/datetime.html#datetime.time.fold) attribute that resolves ambiguity in local time where needed. A great many functions inside the [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime) have been revised so they handle local time disambiguation. Consult the Local Time Disambiguation section for further detail. (Contributed by Alexander Belopolsky in [bpo-24773](https://bugs.python.org/issue?@action=redirect&bpo=24773).)

The [`datetime.strftime()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.strftime) plus [`date.strftime()`](https://docs.python.org/3.14/library/datetime.html#datetime.date.strftime) methods now handle the ISO 8601 date directives `%G`, `%u` and `%V`. (Contributed by Ashley Anderson in [bpo-12006](https://bugs.python.org/issue?@action=redirect&bpo=12006).)

The [`datetime.isoformat()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.isoformat) function has gained an optional *timespec* argument naming how many extra components of the time value to bring along. (Contributed by Alessandro Cucci and Alexander Belopolsky in [bpo-19475](https://bugs.python.org/issue?@action=redirect&bpo=19475).)

The [`datetime.combine()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.combine) now takes an optional *tzinfo* argument. (Contributed by Alexander Belopolsky in [bpo-27661](https://bugs.python.org/issue?@action=redirect&bpo=27661).)

[Subject index](INDEX.md) · [Previous source section](contextlib.md) · [Next source section](decimal.md) · [Release/subject declaration](summary-release-highlights.md)
