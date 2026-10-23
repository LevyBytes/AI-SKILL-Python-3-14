# What's New In Python 3.3 / datetime - datetime

### datetime

- Checking a naive [`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) against an aware one for equality now yields [`False`](https://docs.python.org/3.14/library/constants.html#False) rather than throwing [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) ([bpo-15006](https://bugs.python.org/issue?@action=redirect&bpo=15006)).

- A new [`datetime.datetime.timestamp()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.timestamp) method hands back the POSIX timestamp that matches the [`datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) instance.

- Formatting of years below 1000 is now handled by the [`datetime.datetime.strftime()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.strftime) method.

- Calling the [`datetime.datetime.astimezone()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.astimezone) method with no arguments is now permitted, turning a datetime instance into the system timezone.

[Subject index](INDEX.md) · [Previous source section](curses.md) · [Next source section](decimal.md) · [Release/subject declaration](summary-release-highlights.md)
