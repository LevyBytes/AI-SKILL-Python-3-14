# calendar - General calendar-related functions??

# Calendar, Cgi, Cgitb, Chunk

> Library reference. Reworded prose; identifiers preserved verbatim.

## Overview

Four modules appear on this page. They are, in turn: calendar — General calendar-related functions??; then cgi — Common Gateway Interface support??; followed by cgitb — Traceback manager for CGI scripts??; and finally chunk — Read IFF chunked data??.

## calendar - General calendar-related functions??

cssclass_year_head

The CSS class for the table head spanning the whole year (applied by `formatyear()`). Its default value is `"year"`.

Added in version 3.7.

Keep in mind that even though the class attributes named above use singular forms (e.g. `cssclass_month` `cssclass_noday`), you may swap the lone CSS class for a space separated list of CSS classes, for instance:

```python
"text-bold text-red"

```

What follows is an example of customizing `HTMLCalendar`:

```python
class CustomHTMLCal(calendar.HTMLCalendar):
    cssclasses = [style + " text-nowrap" for style in
                  calendar.HTMLCalendar.cssclasses]
    cssclass_month_head = "text-center month-head"
    cssclass_month = "text-center month"
    cssclass_year = "text-italic lead"

```

[Subject index](INDEX.md) · [Continue](calendar-calendar-class.md) · [Previous](html-calendar-class-and-month-formatting.md) · [Continue](calendar-localetextcalendar-class.md) · [Owning module, declaration or section: calendar](calendar-calendar-class.md) · [Owning module, declaration or section: calendar.HTMLCalendar](html-calendar-class-and-month-formatting.md)
