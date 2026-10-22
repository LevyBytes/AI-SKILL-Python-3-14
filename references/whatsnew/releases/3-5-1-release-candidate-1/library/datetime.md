# Python 3.5.1 release candidate 1 / library / datetime

[bpo-23517](https://bugs.python.org/issue?@action=redirect&bpo=23517): Corrected the rounding inside the fromtimestamp() and utcfromtimestamp() methods of datetime.datetime: microseconds now round half to even (ROUND_HALF_EVEN), with ties landing on the nearest even integer, rather than always rounding down toward minus infinity (ROUND_FLOOR). Sharing the rounding mode with datetime.timedelta matters so that the identity (datetime(1970,1,1) + timedelta(seconds=t)) == datetime.utcfromtimestamp(t) still holds. round(float) relies on that same rounding mode too.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
