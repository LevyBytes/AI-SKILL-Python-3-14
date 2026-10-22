# datetime — `strftime()` and `strptime()` behavior

### `strftime()` and `strptime()` behavior

Every `date`, `datetime`, and `time` object offers a `strftime(format)` method that builds a string rendering the time as directed by an explicit format string.

Going the other way, the `date.strptime()`, `datetime.strptime()` and [`time.strptime()`](https://docs.python.org/3.14/library/time.html#time.strptime) class methods build an object out of a string that represents the time together with a matching format string.

Here is a high-level side-by-side of `strftime()` against `strptime()`:

|  | `strftime` | `strptime` |
| --- | --- | --- |
| Usage | Convert object to a string according to a given format | Parse a string into an object given a corresponding format |
| Type of method | Instance method | Class method |
| Signature | `strftime(format)` | `strptime(date_string, format)` |

>

[Subject index](INDEX.md) · [Previous](timezone-utcoffset-to-timezone-utc.md) · [Continue](strftime-and-strptime-format-codes.md) · [Owning module, declaration or section: datetime](datetime-basic-date-and-time-types.md)
