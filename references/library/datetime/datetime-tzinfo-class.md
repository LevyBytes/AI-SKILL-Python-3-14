# datetime: `datetime.tzinfo`

*class *datetime.tzinfo

A time zone information object’s abstract base class. The `datetime` and `time` classes draw on these to supply a customizable sense of time adjustment (for instance, covering a time zone and/or daylight saving time).

### `tzinfo` objects

 *class *datetime.tzinfo

This is an [abstract base class](https://docs.python.org/3.14/glossary.html#term-abstract-base-class), which means the class is not meant to be instantiated on its own. Define a subclass of `tzinfo` to record details about one particular time zone.

An instance of (a concrete subclass of) `tzinfo` may be handed to the constructors for `datetime` and `time` objects. Those objects regard their attributes as expressed in local time, and the `tzinfo` object provides methods that expose the offset of local time from UTC, the time zone's name, and the DST offset, each one tied to a date or time object passed to them.

You have to derive a concrete subclass and supply (at minimum) implementations of the standard `tzinfo` methods that the `datetime` methods you rely on require. The `datetime` module ships `timezone`, a plain concrete subclass of `tzinfo` able to represent any zone whose offset from UTC stays fixed — UTC on its own, say, or the North American EST and EDT zones.

Special requirement for pickling: A `tzinfo` subclass has to own an [`__init__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__init__) method that works when called with no arguments; otherwise it can be pickled but maybe not unpickled afterward. This is a technical requirement that may be relaxed in the future.

A concrete subclass of `tzinfo` may have to implement the methods below. Precisely which ones are required hinges on how the aware `datetime` objects get used. When unsure, just implement them all.

[Subject index](INDEX.md) · [Previous](datetime-timedelta-class.md) · [Continue](datetime-timezone-class.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Owning module, declaration or section: Available types](datetime-date-class.md) · [Previous](examples-of-usage-time.md) · [Continue](tzinfo-utcoffset-to-tzinfo-tzname.md)
