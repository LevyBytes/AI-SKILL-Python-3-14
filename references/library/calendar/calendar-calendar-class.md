# calendar: `calendar.Calendar`

### `calendar` — General calendar-related functions

**Source code:** [Lib/calendar.py](https://github.com/python/cpython/tree/3.14/Lib/calendar.py)

---

With this module you can emit calendars in the style of the Unix **cal** program, plus it ships extra helper functions tied to the calendar. The default layout treats Monday as the opening day of the week and Sunday as the closing one (following the European convention). Call `setfirstweekday()` to switch the opening day to Sunday (6) or to any weekday you prefer. Any parameters that denote dates are supplied as integers. For functionality that overlaps, consult the [`datetime`](https://docs.python.org/3.14/library/datetime.html#module-datetime) and [`time`](https://docs.python.org/3.14/library/time.html#module-time) modules as well.

Every function and class declared here relies on an idealized calendar — namely today's Gregorian calendar projected without limit in both directions. That corresponds to the "proleptic Gregorian" calendar as defined in "Calendrical Calculations" by Dershowitz and Reingold, the volume in which it serves as the foundation calendar for every computation. Years that are zero or negative follow the rules laid out by the ISO 8601 standard. Thus year 0 stands for 1 BC, year -1 for 2 BC, and the pattern continues.

 *class *calendar.Calendar(*firstweekday=0*)

Builds a `Calendar` object. *firstweekday* is an integer that names the opening day of the week. `MONDAY` is `0` (the default), `SUNDAY` is `6`.

A `Calendar` object exposes several methods for arranging the calendar data ahead of formatting. The class performs no formatting on its own — that responsibility falls to subclasses.

`Calendar` instances have the following methods and attributes:

[Subject index](INDEX.md) · [Previous](calendar-general-calendar-related-functions.md) · [Continue](calendar-week-month-and-year-iteration.md)
