# What’s New In Python 3.8 / datetime — datetime

> (Contributed by Steve Dower in [bpo-36085](https://bugs.python.org/issue?@action=redirect&bpo=36085).)

### datetime

Two fresh alternate constructors, [`datetime.date.fromisocalendar()`](https://docs.python.org/3.14/library/datetime.html#datetime.date.fromisocalendar) and [`datetime.datetime.fromisocalendar()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.fromisocalendar), build [`date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) and [`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) values, in turn, out of an ISO year, week number, and weekday; each one undoes the `isocalendar` method of its respective class.

[Subject index](INDEX.md) · [Previous source section](ctypes.md) · [Next source section](functools.md) · [Release/subject declaration](assignment-expressions.md)
