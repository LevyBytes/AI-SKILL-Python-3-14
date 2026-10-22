# datetime: `time.min`, `time.max`, `time.resolution`, `time.hour`, `time.minute`, `time.second`, `time.microsecond`, `time.tzinfo`, `time.fold`

time.min

The earliest representable `time`, `time(0, 0, 0, 0)`.

 time.max

The latest representable `time`, `time(23, 59, 59, 999999)`.

 time.resolution

The smallest gap possible between two unequal `time` objects, `timedelta(microseconds=1)`, though bear in mind that arithmetic on `time` objects is not supported.

Instance attributes (read-only):

 time.hour

In `range(24)`.

 time.minute

In `range(60)`.

 time.second

In `range(60)`.

 time.microsecond

In `range(1000000)`.

 time.tzinfo

Whatever object was handed in as the tzinfo argument to the `time` constructor, or `None` when nothing was handed in.

 time.fold

In `[0, 1]`. Serves to tell apart wall times across a repeated interval. (Such a repeated interval shows up when clocks fall back as daylight saving time ends or when a zone's UTC offset is lowered for political reasons.) The values 0 and 1 stand, in order, for the earlier and the later of the two instants that share one wall time representation.

Added in version 3.6.

`time` objects allow equality and order comparisons, where `a` counts as less than `b` whenever `a` comes before `b` in time.

Naive and aware `time` objects are never equal. An order comparison between a naive and an aware `time` object raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

When both operands are aware and carry the same `tzinfo` attribute, the `tzinfo` and `fold` attributes are disregarded and the underlying times get compared. When both operands are aware yet carry differing `tzinfo` attributes, they are first brought into line by subtracting their UTC offsets (gathered from `self.utcoffset()`).

Changed in version 3.3: Testing an aware `time` instance against a naive one for equality no longer raises [`TypeError`](https://docs.python.org/3.14/library/exceptions.html#TypeError).

Within Boolean contexts, a `time` object is always treated as true.

Changed in version 3.5: Prior to Python 3.5, a `time` object counted as false when it stood for midnight in UTC. That behavior was judged obscure and error-prone and has been dropped in Python 3.5. See [bpo-13936](https://bugs.python.org/issue?@action=redirect&bpo=13936) for more information.

Other constructors:

[Subject index](INDEX.md) · [Previous](datetime-time-class.md) · [Continue](time-replace.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: datetime.time](datetime-time-class.md) · [Owning module, declaration or section: `time` objects](datetime-time-class.md)
