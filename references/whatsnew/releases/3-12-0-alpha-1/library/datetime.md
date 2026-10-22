# Python 3.12.0 alpha 1 / library / datetime

[gh-69142](https://github.com/python/cpython/issues/69142): A `%:z` strftime format code is added (it yields a tzoffset using colons for separators); refer to [strftime() and strptime() behavior](https://docs.python.org/3.14/library/datetime.html#strftime-strptime-behavior).

[gh-91581](https://github.com/python/cpython/issues/91581): Strip out an unhandled error path in the C implementation of calls to [`datetime.fromtimestamp`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.fromtimestamp) that omit a time zone (that is, deriving local time from an epoch timestamp). Users should notice nothing beyond a possibly clearer error message when this is called with timestamps falling on 10000-01-01 in local time. Paul Ganssle supplied the patch.

[gh-91581](https://github.com/python/cpython/issues/91581): In the pure Python implementation, [`utcfromtimestamp()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.utcfromtimestamp) no longer bothers resolving `fold`, given that the fold can never be 1 in UTC. Besides shaving a little time off the usual case, this likewise wards off certain errors when a timestamp lands near [`datetime.min`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.min). Paul Ganssle supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
