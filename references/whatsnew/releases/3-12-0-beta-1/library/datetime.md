# Python 3.12.0 beta 1 / library / datetime

[gh-103857](https://github.com/python/cpython/issues/103857): Marked [`datetime.datetime.utcnow()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.utcnow) along with [`datetime.datetime.utcfromtimestamp()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.utcfromtimestamp) as deprecated. Paul Ganssle supplied this patch.

[gh-83861](https://github.com/python/cpython/issues/83861): Correct what datetime.astimezone returns when it runs on a naive datetime instance representing local time that falls within a timezone transition gap. Here PEP 495 demands that fold=1 instances yield earlier times than fold=0 ones.

[gh-90750](https://github.com/python/cpython/issues/90750): The [`datetime.datetime.strptime()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.strptime) implementation now relies on [`datetime.datetime.fromisocalendar()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.fromisocalendar), so only well-formed ISO dates ought to be accepted from here on. Paul Ganssle supplied the patch.

[gh-84976](https://github.com/python/cpython/issues/84976): Establish a new `Lib/_pydatetime.py` file holding the Python flavour of the `datetime` module, and have `datetime` pull in that new library's contents solely when the C implementation is absent. As things stand, the entire Python implementation is built and then discarded if the C implementation is unavailable, which needlessly slows `import datetime`.

[gh-103857](https://github.com/python/cpython/issues/103857): Point the stracktrace of datetime deprecations at the calling line instead.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
