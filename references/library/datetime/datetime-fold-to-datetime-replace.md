# datetime: `datetime.fold`, `datetime.date()`, `datetime.time()`, `datetime.timetz()`, `datetime.replace()`

datetime.fold

In `[0, 1]`. Serves to tell apart wall times within a repeated interval. (Such a repeated interval shows up when clocks get turned back as daylight saving time ends, or when the current zone’s UTC offset is reduced for political reasons.) Across two moments sharing a single wall time representation, the values 0 and 1 stand for the earlier and the later one respectively.

Added in version 3.6.

Supported operations:

| Operation | Result |
| --- | --- |
| `datetime2 = datetime1 + timedelta` | (1) |
| `datetime2 = datetime1 - timedelta` | (2) |
| `timedelta = datetime1 - datetime2` | (3) |
| `datetime1 == datetime2` `datetime1 != datetime2` | Equality comparison. (4) |
| `datetime1 < datetime2` `datetime1 > datetime2` `datetime1 <= datetime2` `datetime1 >= datetime2` | Order comparison. (5) |

1.

`datetime2` sits a span of `timedelta` away from `datetime1`, shifted ahead in time when `timedelta.days > 0`, or behind when `timedelta.days < 0`. The outcome keeps the same `tzinfo` attribute as the source datetime, and afterward `datetime2 - datetime1 == timedelta`. [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError) gets raised should `datetime2.year` end up below `MINYEAR` or above `MAXYEAR`. Keep in mind that the operation performs no time zone adjustment, even when the input happens to be an aware object.

2.

Works out the `datetime2` for which `datetime2 + timedelta == datetime1`. As with addition, the outcome keeps the same `tzinfo` attribute as the source datetime, and the operation performs no time zone adjustment, even when the input happens to be aware.

3.

Subtracting one `datetime` from another `datetime` is only defined when both operands are naive, or when both are aware. Where one is aware while the other is naive, [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError) gets raised.

When both are naive, or both are aware while sharing the same `tzinfo` attribute, the `tzinfo` attributes get disregarded, and the outcome is a `timedelta` object `t` for which `datetime2 + t == datetime1`. No time zone adjustments are done in this case.

When both are aware while holding different `tzinfo` attributes, `a-b` behaves as though `a` and `b` had first been turned into naive UTC datetimes. The outcome is `(a.replace(tzinfo=None) - a.utcoffset()) - (b.replace(tzinfo=None) - b.utcoffset())` apart from the fact that the implementation never overflows.

4.

`datetime` objects count as equal when they stand for the same date and time, with the time zone factored in.

Naive and aware `datetime` objects are never equal.

When both comparands are aware while sharing the same `tzinfo` attribute, the `tzinfo` and `fold` attributes get disregarded and the base datetimes get compared. When both comparands are aware while holding different `tzinfo` attributes, the comparison behaves as though the comparands had first been turned into UTC datetimes, save that the implementation never overflows. A `datetime` instance sitting in a repeated interval is never equal to a `datetime` instance belonging to another time zone.

5.

*datetime1* counts as less than *datetime2* when *datetime1* comes ahead of *datetime2* in time, with the time zone factored in.

Order comparison between naive and aware `datetime` objects raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

When both comparands are aware while sharing the same `tzinfo` attribute, the `tzinfo` and `fold` attributes get disregarded and the base datetimes get compared. When both comparands are aware while holding different `tzinfo` attributes, the comparison behaves as though the comparands had first been turned into UTC datetimes, apart from the fact that the implementation never overflows.

Changed in version 3.3: Checking an aware `datetime` instance against a naive one for equality no longer raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

Changed in version 3.13: When a `datetime` object is compared against an instance of the `date` subclass that is itself not a `datetime` subclass, that instance is no longer reduced to `date` (dropping the time part along with the time zone). You can alter this default behavior by overriding the special comparison methods within subclasses.

Instance methods:

 datetime.date()

Return `date` object with same year, month and day.

 datetime.time()

Return `time` object carrying the matching hour, minute, second, microsecond and fold. Its `tzinfo` is `None`. See also method `timetz()`.

Changed in version 3.6: The fold value gets carried over into the `time` object that is returned.

 datetime.timetz()

Return `time` object carrying the matching hour, minute, second, microsecond, fold, and tzinfo attributes. See also method [`time()`](https://docs.python.org/3.14/library/time.html#module-time).

Changed in version 3.6: The fold value gets carried over into the `time` object that is returned.

 datetime.replace(*year=self.year*, *month=self.month*, *day=self.day*, *hour=self.hour*, *minute=self.minute*, *second=self.second*, *microsecond=self.microsecond*, *tzinfo=self.tzinfo*, ***, *fold=0*)

Return a fresh `datetime` object carrying the same attributes, except for the parameters you name, which get updated. Note that passing `tzinfo=None` lets you build a naive datetime out of an aware one while leaving the date and time data unconverted.

`datetime` objects are also supported by generic function [`copy.replace()`](https://docs.python.org/3.14/library/copy.html#copy.replace).

Changed in version 3.6: Added the *fold* parameter.

[Subject index](INDEX.md) · [Previous](datetime-min-to-datetime-tzinfo.md) · [Continue](datetime-astimezone-to-datetime-timestamp.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: `datetime` objects](datetime-datetime-class.md)
