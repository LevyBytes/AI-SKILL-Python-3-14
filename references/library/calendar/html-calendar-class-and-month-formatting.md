# calendar: `calendar.HTMLCalendar`, `formatmonth()`, `formatyear()`, `formatyearpage()`, `formatmonthname()`

*class *calendar.HTMLCalendar(*firstweekday=0*)

Use this class to produce HTML calendars.

`HTMLCalendar` instances have the following methods:

 formatmonth(*theyear*, *themonth*, *withyear=True*)

Return a month's calendar as an HTML table. When *withyear* is true the header carries the year; otherwise only the month name appears.

 formatyear(*theyear*, *width=3*)

Return a year's calendar in HTML-table form. Here *width* (defaulting to 3) sets how many months sit in each row.

 formatyearpage(*theyear*, *width=3*, *css='calendar.css'*, *encoding=None*)

Return a year's calendar as a full HTML page. *width* (defaulting to 3) sets how many months sit in each row. *css* names the cascading style sheet to apply. Pass [`None`](https://docs.python.org/3.14/library/constants.html#None) when no style sheet is wanted. *encoding* names the encoding applied to the output (defaulting to the system default encoding).

 formatmonthname(*theyear*, *themonth*, *withyear=True*)

Return a month name as an HTML table row. When *withyear* is true the row carries the year; otherwise only the month name appears.

`HTMLCalendar` exposes the following attributes that you may override to tailor the CSS classes the calendar applies:

 cssclasses

A list of CSS classes applied to each weekday. The default class list is:

```python
cssclasses = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]

```

extra styles can be appended per day:

```python
cssclasses = ["mon text-bold", "tue", "wed", "thu", "fri", "sat", "sun red"]

```

Keep in mind that this list has to contain seven items.

 cssclass_noday

The CSS class for a weekday that belongs to the previous or upcoming month.

Added in version 3.7.

 cssclasses_weekday_head

A list of CSS classes applied to weekday names in the header row. The default matches `cssclasses`.

Added in version 3.7.

 cssclass_month_head

The month's head CSS class (applied by `formatmonthname()`). Its default value is `"month"`.

Added in version 3.7.

 cssclass_month

The CSS class for the entire month's table (applied by `formatmonth()`). Its default value is `"month"`.

Added in version 3.7.

 cssclass_year

The CSS class for the entire year's table of tables (applied by `formatyear()`). Its default value is `"year"`.

Added in version 3.7.

[Subject index](INDEX.md) · [Previous](calendar-textcalendar-class-to-calendar-textcalendar-pryear.md) · [Continue](calendar-general-calendar-related-functions.md) · [Owning module, declaration or section: calendar](calendar-calendar-class.md)
