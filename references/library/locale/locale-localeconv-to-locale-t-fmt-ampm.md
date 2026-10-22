# locale: `locale.localeconv()`, `locale.nl_langinfo()`, `locale.CODESET`, `locale.D_T_FMT`, `locale.D_FMT`, `locale.T_FMT`, `locale.T_FMT_AMPM`

locale.localeconv()

Returns the local conventions database in the shape of a dictionary. The strings below serve as that dictionary's keys:

| Category | Key | Meaning |
| --- | --- | --- |
| `LC_NUMERIC` | `'decimal_point'` | Decimal point character. |
|  | `'grouping'` | Sequence of numbers naming the relative positions at which the `'thousands_sep'` is expected. Where `CHAR_MAX` ends the sequence, grouping stops there. Where a `0` ends the sequence, the final group size repeats. |
|  | `'thousands_sep'` | Character used between groups. |
| `LC_MONETARY` | `'int_curr_symbol'` | International currency symbol. |
|  | `'currency_symbol'` | Local currency symbol. |
|  | `'p_cs_precedes/n_cs_precedes'` | Whether the value is preceded by the currency symbol (for positive resp. negative values). |
|  | `'p_sep_by_space/n_sep_by_space'` | Whether a space divides the currency symbol from the value (for positive resp. negative values). |
|  | `'mon_decimal_point'` | Decimal point applied to monetary values. |
|  | `'frac_digits'` | Count of fractional digits in local formatting of monetary values. |
|  | `'int_frac_digits'` | Count of fractional digits in international formatting of monetary values. |
|  | `'mon_thousands_sep'` | Group separator applied to monetary values. |
|  | `'mon_grouping'` | Counterpart of `'grouping'`, applied to monetary values. |
|  | `'positive_sign'` | Symbol that marks a positive monetary value. |
|  | `'negative_sign'` | Symbol that marks a negative monetary value. |
|  | `'p_sign_posn/n_sign_posn'` | Where the sign sits (for positive resp. negative values), see below. |

Any numeric value may be set to `CHAR_MAX`, signaling that this locale specifies no value for it.

The possible values for `'p_sign_posn'` and `'n_sign_posn'` are given below.

| Value | Explanation |
| --- | --- |
| `0` | Parentheses enclose both currency and value. |
| `1` | The sign belongs ahead of the value and currency symbol. |
| `2` | The sign belongs after the value and currency symbol. |
| `3` | The sign belongs directly ahead of the value. |
| `4` | The sign belongs directly after the value. |
| `CHAR_MAX` | This locale specifies nothing. |

Where locales differ and numeric or monetary strings are non-ASCII, the function temporarily switches the `LC_CTYPE` locale over to the `LC_NUMERIC` locale or the `LC_MONETARY` locale. Other threads feel this temporary change.

Changed in version 3.7: Under certain conditions the function now temporarily switches the `LC_CTYPE` locale over to the `LC_NUMERIC` locale.

 locale.nl_langinfo(*option*)

Return some locale-specific information as a string. Not every system offers this function, and the set of possible options may likewise differ from one platform to the next. The possible argument values are numbers, and the locale module makes symbolic constants available for them.

The `nl_langinfo()` function accepts one of the following keys. Most of the descriptions are drawn from the matching description in the GNU C library.

 locale.CODESET

Get a string giving the name of the character encoding that the selected locale uses.

 locale.D_T_FMT

Get a string usable as a format string for [`time.strftime()`](https://docs.python.org/3.14/library/time.html#time.strftime) so as to render date and time the locale-specific way.

 locale.D_FMT

Get a string usable as a format string for [`time.strftime()`](https://docs.python.org/3.14/library/time.html#time.strftime) so as to render a date the locale-specific way.

 locale.T_FMT

Get a string usable as a format string for [`time.strftime()`](https://docs.python.org/3.14/library/time.html#time.strftime) so as to render a time the locale-specific way.

 locale.T_FMT_AMPM

Get a format string that [`time.strftime()`](https://docs.python.org/3.14/library/time.html#time.strftime) uses to render time in am/pm form.

[Subject index](INDEX.md) · [Previous](locale-error-to-locale-setlocale.md) · [Continue](locale-day-1-to-locale-mon-12.md) · [Owning module, declaration or section: locale](locale-error-to-locale-setlocale.md)
