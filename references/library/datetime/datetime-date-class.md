# datetime: `datetime.date`

### Available types

 *class *datetime.date

An idealized naive date, on the assumption that the present Gregorian calendar has always applied and always will. Attributes: `year`, `month`, and `day`.

### `date` objects

Within an idealized calendar — the present Gregorian calendar projected without limit in both directions — a `date` object stands for a date (year, month and day).

Day number 1 is January 1 of year 1, day number 2 is January 2 of year 1, continuing onward. [2]

 *class *datetime.date(*year*, *month*, *day*)

Every argument is mandatory. Each must be an integer falling within these ranges:

- `MINYEAR <= year <= MAXYEAR`

- `1 <= month <= 12`

- `1 <= day <= number of days in the given month and year`

Supplying an argument beyond those ranges causes [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) to be raised.

Other constructors, all class methods:

[Subject index](INDEX.md) · [Previous](datetime-minyear-to-datetime-utc.md) · [Continue](datetime-time-class.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md) · [Previous](examples-of-usage-timedelta.md) · [Continue](date-objects.md)
