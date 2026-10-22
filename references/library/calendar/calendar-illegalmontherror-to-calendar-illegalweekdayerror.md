# calendar: `calendar.IllegalMonthError`, `calendar.IllegalWeekdayError`

*exception *calendar.IllegalMonthError(*month*)

A subclass of [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) and [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError), raised when the supplied month number falls outside the range 1-12 (inclusive).

Changed in version 3.12: `IllegalMonthError` now counts as a subclass of [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) too. Fresh code should steer clear of catching [`IndexError`](https://docs.python.org/3.14/library/exceptions.html#IndexError).

 month

The invalid month number.

 *exception *calendar.IllegalWeekdayError(*weekday*)

A subclass of [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError), raised when the supplied weekday number falls outside the range 0-6 (inclusive).

 weekday

The invalid weekday number.

See also

Module [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime)

Object-oriented interface to dates and times offering functionality akin to the [`time`](https://docs.python.org/3.14/library/time.html#module-time) module.

Module [`time`](https://docs.python.org/3.14/library/time.html#module-time)

Low-level time related functions.

[Subject index](INDEX.md) · [Previous](calendar-month-class.md) · [Continue](command-line-usage-year.md) · [Owning module, declaration or section: calendar](calendar-calendar-class.md)
