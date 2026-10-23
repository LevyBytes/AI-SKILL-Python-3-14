# What's New In Python 3.6 / PEP 495: Local Time Disambiguation - datetime

### PEP 495: Local Time Disambiguation

Across most places on Earth, local clocks have been and will continue to be turned back at various points. During those turnbacks, windows open in which a local clock reads the very same time twice within one day. Under such conditions, what a local clock shows (or what a Python datetime instance holds) is not enough by itself to pin down one specific instant.

[**PEP 495**](https://peps.python.org/pep-0495/) introduces the fresh *fold* attribute on [`datetime.datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) and [`datetime.time`](https://docs.python.org/3.14/library/datetime.html#datetime.time) instances so the two instants sharing one local time can be told apart:

```python
>>> u0 = datetime(2016, 11, 6, 4, tzinfo=timezone.utc)
>>> for i in range(4):
...     u = u0 + i*HOUR
...     t = u.astimezone(Eastern)
...     print(u.time(), 'UTC =', t.time(), t.tzname(), t.fold)
...
04:00:00 UTC = 00:00:00 EDT 0
05:00:00 UTC = 01:00:00 EDT 0
06:00:00 UTC = 01:00:00 EST 1
07:00:00 UTC = 02:00:00 EST 0

```

The [`fold`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.fold) attribute carries `0` for every instance apart from the one standing for the later (in chronological terms) instant whenever a case is ambiguous.

See also

[**PEP 495**](https://peps.python.org/pep-0495/): Local Time Disambiguation

PEP written by Alexander Belopolsky and Tim Peters, implementation by Alexander Belopolsky.

[Subject index](INDEX.md) · [Previous source section](pep-519-adding-a-file-system-path-protocol.md) · [Next source section](pep-529-change-windows-filesystem-encoding-to-utf-8.md) · [Release/subject declaration](summary-release-highlights.md)
