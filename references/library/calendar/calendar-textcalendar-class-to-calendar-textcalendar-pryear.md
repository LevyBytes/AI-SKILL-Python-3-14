# calendar: `calendar.TextCalendar`, `formatday()`, `formatweek()`, `formatweekday()`, `formatweekheader()`, `formatmonth()`, `formatmonthname()`, `prmonth()`, `formatyear()`, `pryear()`

*class *calendar.TextCalendar(*firstweekday=0*)

Use this class to produce plain text calendars.

`TextCalendar` instances have the following methods:

 formatday(*theday*, *weekday*, *width*)

Return a string that renders one day formatted to the supplied *width*. When *theday* is `0`, return a run of spaces of that width to depict an empty day. The *weekday* parameter goes unused.

 formatweek(*theweek*, *w=0*)

Return one week as a string carrying no newline. When *w* is supplied, it sets the width of the date columns, which are centered. The result hinges on the first weekday fixed in the constructor or assigned through the `setfirstweekday()` method.

 formatweekday(*weekday*, *width*)

Return a string giving the name of one weekday formatted to the supplied *width*. The *weekday* parameter is an integer denoting the day of the week, where `0` is Monday and `6` is Sunday.

 formatweekheader(*width*)

Return a string holding the header row of weekday names, each formatted to the supplied *width* per column. Those names track the locale settings and are padded out to the named width.

 formatmonth(*theyear*, *themonth*, *w=0*, *l=0*)

Return a month's calendar as a multi-line string. When *w* is supplied, it sets the width of the date columns, which are centered. When *l* is supplied, it sets how many lines each week consumes. The result hinges on the first weekday fixed in the constructor or assigned through the `setfirstweekday()` method.

 formatmonthname(*theyear*, *themonth*, *width=0*, *withyear=True*)

Return a string giving the month's name centered inside the supplied *width*. When *withyear* is `True`, fold the year into the output. The *theyear* and *themonth* parameters name the year and month whose name is to be formatted, respectively.

 prmonth(*theyear*, *themonth*, *w=0*, *l=0*)

Print a month's calendar exactly as `formatmonth()` returns it.

 formatyear(*theyear*, *w=2*, *l=1*, *c=6*, *m=3*)

Return a *m*-column calendar covering a whole year as a multi-line string. The optional parameters *w*, *l*, and *c* govern the date column width, the lines per week, and the count of spaces separating month columns, respectively. The result hinges on the first weekday fixed in the constructor or assigned through the `setfirstweekday()` method. Which year is the earliest one a calendar can be produced for depends on the platform.

 pryear(*theyear*, *w=2*, *l=1*, *c=6*, *m=3*)

Print the whole year's calendar exactly as `formatyear()` returns it.

[Subject index](INDEX.md) · [Previous](calendar-week-month-and-year-iteration.md) · [Continue](html-calendar-class-and-month-formatting.md) · [Owning module, declaration or section: calendar](calendar-calendar-class.md)
