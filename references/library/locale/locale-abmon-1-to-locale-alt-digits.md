# locale: Abbreviated months, numeric symbols and era formatting

locale.ABMON_1

 locale.ABMON_2

 locale.ABMON_3

 locale.ABMON_4

 locale.ABMON_5

 locale.ABMON_6

 locale.ABMON_7

 locale.ABMON_8

 locale.ABMON_9

 locale.ABMON_10

 locale.ABMON_11

 locale.ABMON_12

Get the abbreviated name of the n-th month.

 locale.RADIXCHAR

Get the radix character (decimal dot, decimal comma, etc.).

 locale.THOUSEP

Get the separator character for thousands (groups of three digits).

 locale.YESEXPR

Get a regular expression, for use with the regex function, that recognizes an affirmative reply to a yes/no question.

 locale.NOEXPR

Get a regular expression, for use with the `regex(3)` function, that recognizes a negative reply to a yes/no question.

Note

The regular expressions behind `YESEXPR` and `NOEXPR` adopt syntax fit for the C library's `regex` function, which may diverge from the syntax that [`re`](https://docs.python.org/3.14/library/re.html#module-re) uses.

 locale.CRNCYSTR

Get the currency symbol, with "-" in front when the symbol belongs before the value, "+" in front when it belongs after the value, or "." in front when it ought to take the place of the radix character.

 locale.ERA

Get a string describing the way a locale counts and shows years for each era.

This value goes undefined in most locales. The Japanese locale is one example that does define it. In Japan, the traditional way of writing dates carries the name of the era matching the reign of the emperor of the day.

You normally should not need to use this value directly. Placing the `E` modifier inside their format strings makes the [`time.strftime()`](https://docs.python.org/3.14/library/time.html#time.strftime) function draw on this information. As for the format of the returned string, *The Open Group Base Specifications Issue 8* lays it out in paragraph [7.3.5.2 LC_TIME C-Language Access](https://pubs.opengroup.org/onlinepubs/9799919799/basedefs/V1_chap07.html#tag_07_03_05_02).

 locale.ERA_D_T_FMT

Get a format string for [`time.strftime()`](https://docs.python.org/3.14/library/time.html#time.strftime) so as to render date and time the locale-specific, era-based way.

 locale.ERA_D_FMT

Get a format string for [`time.strftime()`](https://docs.python.org/3.14/library/time.html#time.strftime) so as to render a date the locale-specific, era-based way.

 locale.ERA_T_FMT

Get a format string for [`time.strftime()`](https://docs.python.org/3.14/library/time.html#time.strftime) so as to render a time the locale-specific, era-based way.

 locale.ALT_DIGITS

Get a string made of as many as 100 semicolon-separated symbols that render the values 0 to 99 the locale-specific way. Across most locales this is an empty string.

Where locales differ and the resulting string is non-ASCII, the function temporarily switches the `LC_CTYPE` locale over to the locale of whichever category determines the requested value (`LC_TIME`, `LC_NUMERIC`, `LC_MONETARY` or `LC_MESSAGES`). Other threads feel this temporary change.

Changed in version 3.14: Under certain conditions the function now temporarily switches the `LC_CTYPE` locale.

[Subject index](INDEX.md) · [Previous](locale-day-1-to-locale-mon-12.md) · [Continue](locale-getdefaultlocale-to-locale-currency.md) · [Owning module, declaration or section: locale](locale-error-to-locale-setlocale.md)
