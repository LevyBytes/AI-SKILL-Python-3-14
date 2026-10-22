# Python 3.11.0 alpha 6 / library / calendar

[bpo-46659](https://bugs.python.org/issue?@action=redirect&bpo=46659): The [`calendar.LocaleTextCalendar`](https://docs.python.org/3.14/library/calendar.html#calendar.LocaleTextCalendar) plus [`calendar.LocaleHTMLCalendar`](https://docs.python.org/3.14/library/calendar.html#calendar.LocaleHTMLCalendar) classes now lean on [`locale.getlocale()`](https://docs.python.org/3.14/library/locale.html#locale.getlocale) rather than [`locale.getdefaultlocale()`](https://docs.python.org/3.14/library/locale.html#locale.getdefaultlocale) whenever no locale gets passed. Victor Stinner wrote the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
