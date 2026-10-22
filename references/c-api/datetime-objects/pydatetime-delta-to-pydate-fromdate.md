# datetime objects C API: Date/time object types, checks and date construction

type PyDateTime_Delta

This subtype of [`PyObject`](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) represents the difference between two datetime values.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyDateTime_DateType

A [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) instance standing for the Python date type; over on the Python side it is one and the same object as [`datetime.date`](https://docs.python.org/3.14/library/datetime.html#datetime.date).

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyDateTime_DateTimeType

A [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) instance corresponding to the Python datetime type; from Python it is identical to the [`datetime.datetime`](https://docs.python.org/3.14/library/datetime.html#datetime.datetime) object.

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyDateTime_TimeType

A [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) instance that stands in for the Python time type; within Python it refers to the very same object as [`datetime.time`](https://docs.python.org/3.14/library/datetime.html#datetime.time).

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyDateTime_DeltaType

A [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) instance for the Python type that captures the gap between two datetime values; on the Python side it coincides exactly with [`datetime.timedelta`](https://docs.python.org/3.14/library/datetime.html#datetime.timedelta).

 [PyTypeObject](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) PyDateTime_TZInfoType

A [`PyTypeObject`](https://docs.python.org/3.14/c-api/type.html#c.PyTypeObject) instance representing the Python time zone info type; viewed from Python it is the same object as [`datetime.tzinfo`](https://docs.python.org/3.14/library/datetime.html#datetime.tzinfo).

Macro for access to the UTC singleton:

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDateTime_TimeZone_UTC

Returns the time zone singleton representing UTC, the same object as [`datetime.timezone.utc`](https://docs.python.org/3.14/library/datetime.html#datetime.timezone.utc).

Added in version 3.7.

Type-check macros:

 int PyDate_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob)

Yields true when *ob* has type `PyDateTime_DateType` or descends from `PyDateTime_DateType`. Here *ob* may not be `NULL`. The call never fails.

 int PyDate_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob)

Yields true only when *ob* is precisely of type `PyDateTime_DateType`. Here *ob* may not be `NULL`. The call never fails.

 int PyDateTime_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob)

Returns a true result when *ob* either is `PyDateTime_DateTimeType` or inherits from `PyDateTime_DateTimeType`. A `NULL` value for *ob* is not allowed. Success is guaranteed every time.

 int PyDateTime_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob)

Returns a true result when *ob* is exactly `PyDateTime_DateTimeType`. A `NULL` value for *ob* is not allowed. Success is guaranteed every time.

 int PyTime_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob)

Gives back true if *ob* is of the `PyDateTime_TimeType` type or any subtype of `PyDateTime_TimeType`. Passing `NULL` for *ob* is forbidden. This routine cannot fail.

 int PyTime_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob)

Gives back true if *ob* is strictly of the `PyDateTime_TimeType` type. Passing `NULL` for *ob* is forbidden. This routine cannot fail.

 int PyDelta_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob)

A true result comes back when *ob* carries the `PyDateTime_DeltaType` type or a subtype of `PyDateTime_DeltaType`. The *ob* argument must never be `NULL`. There is no failure path.

 int PyDelta_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob)

A true result comes back when *ob* carries exactly the `PyDateTime_DeltaType` type. The *ob* argument must never be `NULL`. There is no failure path.

 int PyTZInfo_Check([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob)

Evaluates to true should *ob* be of the `PyDateTime_TZInfoType` type or a subtype of `PyDateTime_TZInfoType`. You must not supply `NULL` as *ob*. The function is infallible.

 int PyTZInfo_CheckExact([PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *ob)

Evaluates to true should *ob* be exactly of the `PyDateTime_TZInfoType` type. You must not supply `NULL` as *ob*. The function is infallible.

Macros to create objects:

 [PyObject](https://docs.python.org/3.14/c-api/structures.html#c.PyObject) *PyDate_FromDate(int year, int month, int day)

*Return value: New reference.*

Produce a [`datetime.date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) object set to the given year, month and day.

[Subject index](INDEX.md) · [Owning C API section and shared conditions](pydatetime-import.md) · [Previous source contract](pydatetime-time.md) · [Following source contract](pydatetime-fromdateandtime-to-pydatetime-date-get-microsecond.md)
