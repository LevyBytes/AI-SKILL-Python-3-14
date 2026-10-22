# calendar: Calendar CLI month selection and formatting options

month

The month of the named `year` whose calendar is printed. Has to be a number between 1 and 12, and is only valid in text mode. Defaults to printing a calendar for the entire year.

*Text-mode options:*

 --width WIDTH, -w WIDTH

The width of the date column measured in terminal columns. The date is printed centred within the column. Any value below 2 is disregarded. Defaults to 2.

 --lines LINES, -l LINES

The line count given to each week measured in terminal rows. The date is printed top-aligned. Any value below 1 is disregarded. Defaults to 1.

 --spacing SPACING, -s SPACING

The gap between months measured in columns. Any value below 2 is disregarded. Defaults to 6.

 --months MONTHS, -m MONTHS

The count of months printed in each row. Defaults to 3.

Changed in version 3.14: Out of the box, the current date is now shown highlighted in color, which you can [control using environment variables](https://docs.python.org/3.14/using/cmdline.html#using-on-controlling-color).

*HTML-mode options:*

 --css CSS, -c CSS

The path to a CSS stylesheet for the calendar to use. It has to be either relative to the generated HTML, or an absolute HTTP or `file:///` URL.

[Subject index](INDEX.md) · [Previous](command-line-usage-year.md) · [Continue](../cgi/cgi-common-gateway-interface-support.md) · [Owning module, declaration or section: calendar](calendar-calendar-class.md) · [Owning module, declaration or section: Command-line usage](command-line-usage-year.md)
