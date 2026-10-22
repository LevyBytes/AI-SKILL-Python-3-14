# datetime objects C API: Date/time and timezone constructors with field access

[PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDateTime_FromDateAndTime(int year, int month, int day, int hour, int minute, int second, int usecond)

*Return value: New reference.*

Produce a [`datetime.datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) object built from the given year, month, day, hour, minute, second and microsecond.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDateTime_FromDateAndTimeAndFold(int year, int month, int day, int hour, int minute, int second, int usecond, int fold)

*Return value: New reference.*

Produce a [`datetime.datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) object assembled from the given year, month, day, hour, minute, second, microsecond and fold.

Added in version 3.6.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyTime_FromTime(int hour, int minute, int second, int usecond)

*Return value: New reference.*

Produce a [`datetime.time`](https://docs.python.org/3.14/library/datetime.html#datetime.time) object set to the given hour, minute, second and microsecond.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyTime_FromTimeAndFold(int hour, int minute, int second, int usecond, int fold)

*Return value: New reference.*

Produce a [`datetime.time`](https://docs.python.org/3.14/library/datetime.html#datetime.time) object built from the given hour, minute, second, microsecond and fold.

Added in version 3.6.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDelta_FromDSU(int days, int seconds, int useconds)

*Return value: New reference.*

Produce a [`datetime.timedelta`](https://docs.python.org/3.14/library/datetime.html#datetime.timedelta) object that stands for the supplied count of days, seconds and microseconds. The values are normalized so that the final microseconds and seconds fall within the ranges spelled out for `datetime.timedelta` objects.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyTimeZone_FromOffset([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *offset)

*Return value: New reference.*

Produce a [`datetime.timezone`](https://docs.python.org/3.14/library/datetime.html#datetime.timezone) object carrying an unnamed fixed offset that the *offset* argument supplies.

Added in version 3.7.

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyTimeZone_FromOffsetAndName([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *offset, [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *name)

*Return value: New reference.*

Produce a [`datetime.timezone`](https://docs.python.org/3.14/library/datetime.html#datetime.timezone) object carrying a fixed offset that the *offset* argument supplies, together with the tzname *name*.

Added in version 3.7.

Macros that pull individual fields out of date objects. Whatever you pass has to be a `PyDateTime_Date` instance, subclasses (`PyDateTime_DateTime` among them) included. That argument cannot be `NULL`, and no type checking takes place:

 int PyDateTime_GET_YEAR(PyDateTime_Date *o)

Return the year, as a positive int.

 int PyDateTime_GET_MONTH(PyDateTime_Date *o)

Return the month, as an int from 1 through 12.

 int PyDateTime_GET_DAY(PyDateTime_Date *o)

Return the day, as an int from 1 through 31.

Macros that pull individual fields out of datetime objects. Whatever you pass has to be a `PyDateTime_DateTime` instance, subclasses included. That argument cannot be `NULL`, and no type checking takes place:

 int PyDateTime_DATE_GET_HOUR(PyDateTime_DateTime *o)

Return the hour, as an int from 0 through 23.

 int PyDateTime_DATE_GET_MINUTE(PyDateTime_DateTime *o)

Return the minute, as an int from 0 through 59.

 int PyDateTime_DATE_GET_SECOND(PyDateTime_DateTime *o)

Return the second, as an int from 0 through 59.

 int PyDateTime_DATE_GET_MICROSECOND(PyDateTime_DateTime *o)

Return the microsecond, as an int from 0 through 999999.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pydatetime-import.md) · [Owning structure and shared ABI conditions](pydatetime-delta-to-pydate-fromdate.md) · [Following source contract](pydatetime-date-get-fold-to-pydate-fromtimestamp.md)
