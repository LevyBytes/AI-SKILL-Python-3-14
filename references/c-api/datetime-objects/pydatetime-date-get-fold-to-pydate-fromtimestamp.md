# datetime objects C API: Time/fold fields, durations and timestamp constructors

int PyDateTime_DATE_GET_FOLD(PyDateTime_DateTime *o)

Return the fold, as an int from 0 through 1.

Added in version 3.6.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDateTime_DATE_GET_TZINFO(PyDateTime_DateTime *o)

Return the tzinfo (which may be `None`).

Added in version 3.10.

Macros that pull individual fields out of time objects. Whatever you pass has to be a `PyDateTime_Time` instance, subclasses included. That argument cannot be `NULL`, and no type checking takes place:

 int PyDateTime_TIME_GET_HOUR(PyDateTime_Time *o)

Return the hour, as an int from 0 through 23.

 int PyDateTime_TIME_GET_MINUTE(PyDateTime_Time *o)

Return the minute, as an int from 0 through 59.

 int PyDateTime_TIME_GET_SECOND(PyDateTime_Time *o)

Return the second, as an int from 0 through 59.

 int PyDateTime_TIME_GET_MICROSECOND(PyDateTime_Time *o)

Return the microsecond, as an int from 0 through 999999.

 int PyDateTime_TIME_GET_FOLD(PyDateTime_Time *o)

Return the fold, as an int from 0 through 1.

Added in version 3.6.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDateTime_TIME_GET_TZINFO(PyDateTime_Time *o)

Return the tzinfo (which may be `None`).

Added in version 3.10.

Macros that pull individual fields out of time delta objects. Whatever you pass has to be a `PyDateTime_Delta` instance, subclasses included. That argument cannot be `NULL`, and no type checking takes place:

 int PyDateTime_DELTA_GET_DAYS(PyDateTime_Delta *o)

Return the number of days, as an int from -999999999 to 999999999.

Added in version 3.3.

 int PyDateTime_DELTA_GET_SECONDS(PyDateTime_Delta *o)

Return the number of seconds, as an int from 0 through 86399.

Added in version 3.3.

 int PyDateTime_DELTA_GET_MICROSECONDS(PyDateTime_Delta *o)

Return the number of microseconds, as an int from 0 through 999999.

Added in version 3.3.

Macros for the convenience of modules implementing the DB API:

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDateTime_FromTimestamp([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *args)

*Return value: New reference.*

Build a fresh [`datetime.datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) object and hand it back, taking an argument tuple of the kind you'd feed to [`datetime.datetime.fromtimestamp()`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime.fromtimestamp).

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDate_FromTimestamp([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *args)

*Return value: New reference.*

Build a fresh [`datetime.date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) object and hand it back, taking an argument tuple of the kind you'd feed to [`datetime.date.fromtimestamp()`](https://docs.python.org/3.14/library/datetime.html#datetime.date.fromtimestamp).

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pydatetime-import.md) · [Owning structure and shared ABI conditions](pydatetime-delta-to-pydate-fromdate.md) · [Previous source contract](pydatetime-fromdateandtime-to-pydatetime-date-get-microsecond.md) · [Following source contract](pydatetime-capsule-name.md)
