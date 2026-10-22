# calendar.Calendar: Calendar week, month and year iteration

firstweekday

The opening weekday given as an integer (0–6).

You may also write and read this property through `setfirstweekday()` and `getfirstweekday()` respectively.

 getfirstweekday()

Return an [`int`](https://docs.python.org/3.14/library/functions.html#int) for the current first weekday (0–6).

Equivalent to reading the `firstweekday` property.

 setfirstweekday(*firstweekday*)

Set the first weekday to *firstweekday*, supplied as an [`int`](https://docs.python.org/3.14/library/functions.html#int) (0–6).

Equivalent to assigning the `firstweekday` property.

 iterweekdays()

Return an iterator over the weekday numbers applied to a single week. Its first yielded value matches the value held by the `firstweekday` property.

 itermonthdates(*year*, *month*)

Return an iterator covering the month *month* (1–12) within the year *year*. It yields every day (as [`datetime.date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) objects) for that month together with any days falling before the month starts or after it ends that are needed to round out a full week.

 itermonthdays(*year*, *month*)

Return an iterator for the month *month* in the year *year* much like `itermonthdates()`, except it is not bounded by the [`datetime.date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) range. The yielded days are plain day-of-the-month numbers. Where days lie outside the named month, the day number is `0`.

 itermonthdays2(*year*, *month*)

Return an iterator for the month *month* in the year *year* much like `itermonthdates()`, except it is not bounded by the [`datetime.date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) range. The yielded days are tuples pairing a day-of-the-month number with a weekday number.

 itermonthdays3(*year*, *month*)

Return an iterator for the month *month* in the year *year* much like `itermonthdates()`, except it is not bounded by the [`datetime.date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) range. The yielded days are tuples holding a year, a month, and a day-of-the-month number.

Added in version 3.7.

 itermonthdays4(*year*, *month*)

Return an iterator for the month *month* in the year *year* much like `itermonthdates()`, except it is not bounded by the [`datetime.date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) range. The yielded days are tuples holding these four values: a year, a month, a day of the month, plus a day-of-the-week number.

Added in version 3.7.

 monthdatescalendar(*year*, *month*)

Return a list of the weeks within the month *month* of the *year*, given as complete weeks. Each week is a list of seven [`datetime.date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) objects.

 monthdays2calendar(*year*, *month*)

Return a list of the weeks within the month *month* of the *year*, given as complete weeks. Each week is a list of seven tuples pairing day numbers with weekday numbers.

 monthdayscalendar(*year*, *month*)

Return a list of the weeks within the month *month* of the *year*, given as complete weeks. Each week is a list of seven day numbers.

 yeardatescalendar(*year*, *width=3*)

Return the data for the named year laid out for formatting. The result is a list of month rows. Every month row holds up to *width* months (defaulting to 3). Every month spans between 4 and 6 weeks, and every week spans 1–7 days. Days are [`datetime.date`](https://docs.python.org/3.14/library/datetime.html#datetime.date) objects.

 yeardays2calendar(*year*, *width=3*)

Return the data for the named year laid out for formatting (much like `yeardatescalendar()`). Each entry in the week lists is a tuple of a day number and a weekday number. Day numbers that fall outside the month are zero.

 yeardayscalendar(*year*, *width=3*)

Return the data for the named year laid out for formatting (much like `yeardatescalendar()`). Each entry in the week lists is a day number. Day numbers that fall outside the month are zero.

[Subject index](INDEX.md) · [Previous](calendar-calendar-class.md) · [Continue](calendar-textcalendar-class-to-calendar-textcalendar-pryear.md) · [Owning module, declaration or section: calendar](calendar-calendar-class.md) · [Owning module, declaration or section: calendar.Calendar](calendar-calendar-class.md)
