# Python 3.7.0 beta 1 / library / datetime

[bpo-32404](https://bugs.python.org/issue?@action=redirect&bpo=32404): Correct a bug in which [`datetime.datetime.fromtimestamp()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.fromtimestamp) skipped calling __new__ within [`datetime.datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) subclasses.

[bpo-32403](https://bugs.python.org/issue?@action=redirect&bpo=32403): The alternate constructors for [`datetime.date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) plus [`datetime.datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) run faster now.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
