# datetime: `datetime.time`

*class *datetime.time

An idealized time that does not depend on any specific day, taking each day to hold precisely 24*60*60 seconds. (No concept of “leap seconds” exists here.) Attributes: `hour`, `minute`, `second`, `microsecond`, and `tzinfo`.

### `time` objects

A `time` object stands for a (local) time of day, detached from any specific day, and open to adjustment through a `tzinfo` object.

 *class *datetime.time(*hour=0*, *minute=0*, *second=0*, *microsecond=0*, *tzinfo=None*, ***, *fold=0*)

Every argument is optional. *tzinfo* may be `None`, or an instance of a `tzinfo` subclass. The other arguments have to be integers that fall within these ranges:

- `0 <= hour < 24`,

- `0 <= minute < 60`,

- `0 <= second < 60`,

- `0 <= microsecond < 1000000`,

- `fold in [0, 1]`.

When an argument falls outside those ranges, [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised. Each defaults to 0 apart from *tzinfo*, whose default is `None`.

Class attributes:

[Subject index](INDEX.md) · [Previous](datetime-date-class.md) · [Continue](datetime-datetime-class.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: Available types](datetime-date-class.md) · [Previous](examples-of-usage-datetime-code-example-import-datetime-as-dt.md) · [Continue](time-min-to-time-fold.md)
