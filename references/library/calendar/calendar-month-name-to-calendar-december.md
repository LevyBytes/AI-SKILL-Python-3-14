# calendar: Localized month names and month-number constants

calendar.month_name

A sequence standing for the months of the year in the active locale. It honors the usual convention that January is month number 1, so its length is 13 and `month_name[0]` is the empty string.

```python
>>> import calendar
>>> list(calendar.month_name)
['', 'January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

```

 calendar.month_abbr

A sequence standing for the shortened months of the year in the active locale. It honors the usual convention that January is month number 1, so its length is 13 and `month_abbr[0]` is the empty string.

```python
>>> import calendar
>>> list(calendar.month_abbr)
['', 'Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

```

 calendar.JANUARY

 calendar.FEBRUARY

 calendar.MARCH

 calendar.APRIL

 calendar.MAY

 calendar.JUNE

 calendar.JULY

 calendar.AUGUST

 calendar.SEPTEMBER

 calendar.OCTOBER

 calendar.NOVEMBER

 calendar.DECEMBER

Aliases for the months of the year, where `JANUARY` is `1` and `DECEMBER` is `12`.

Added in version 3.12.

[Subject index](INDEX.md) · [Previous](calendar-day-class.md) · [Continue](calendar-month-class.md) · [Owning module, declaration or section: calendar](calendar-calendar-class.md)
