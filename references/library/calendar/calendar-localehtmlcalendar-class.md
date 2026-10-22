# calendar: `calendar.LocaleHTMLCalendar`

*class *calendar.LocaleHTMLCalendar(*firstweekday=0*, *locale=None*)

You may hand this subclass of `HTMLCalendar` a locale name in its constructor, and it then returns month and weekday names in that locale.

Note

The constructor along with the `formatweekday()` and `formatmonthname()` methods of these two classes briefly switch the `LC_TIME` locale over to the supplied *locale*. Since the active locale is a process-wide setting, these are not thread-safe.

For plain text calendars this module supplies the following functions.

[Subject index](INDEX.md) · [Previous](calendar-localetextcalendar-class.md) · [Continue](calendar-setfirstweekday-to-calendar-day-abbr.md) · [Owning module, declaration or section: calendar](calendar-calendar-class.md)
