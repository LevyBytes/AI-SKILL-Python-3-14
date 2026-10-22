# csv: `csv.QUOTE_ALL`, `csv.QUOTE_MINIMAL`, `csv.QUOTE_NONNUMERIC`, `csv.QUOTE_NONE`, `csv.QUOTE_NOTNULL`, `csv.QUOTE_STRINGS`, `csv.Error`

csv.QUOTE_ALL

Tells `writer` objects to wrap every field in quotes.

 csv.QUOTE_MINIMAL

Tells `writer` objects to reserve quoting for fields that hold special characters, namely *delimiter*, *quotechar*, `'\r'`, `'\n'`, or anything found within *lineterminator*.

 csv.QUOTE_NONNUMERIC

Tells `writer` objects to put quotes around each field that isn't numeric.

Tells `reader` objects to turn every field that lacks quotes into the [`float`](https://docs.python.org/3.14/library/functions.html#float) type.

Note

A handful of numeric types, among them [`bool`](https://docs.python.org/3.14/library/functions.html#bool), [`Fraction`](https://docs.python.org/3.14/library/fractions.html#fractions.Fraction), and [`IntEnum`](https://docs.python.org/3.14/library/enum.html#enum.IntEnum), render as strings that won't convert into [`float`](https://docs.python.org/3.14/library/functions.html#float). As a result, they can't be read under the `QUOTE_NONNUMERIC` and `QUOTE_STRINGS` modes.

 csv.QUOTE_NONE

Tells `writer` objects to leave fields entirely unquoted. Whenever the active *delimiter*, *quotechar*, *escapechar*, `'\r'`, `'\n'`, or some character belonging to *lineterminator* shows up in the output, the active *escapechar* character is placed in front of it. With no *escapechar* set, the writer raises `Error` the moment it meets a character needing to be escaped. To keep *quotechar* itself from being escaped, set it to `None`.

Tells `reader` objects to treat quote characters as ordinary, applying no special handling.

 csv.QUOTE_NOTNULL

Tells `writer` objects to quote every field whose value isn't `None`. It resembles `QUOTE_ALL`, the difference being that a field holding `None` is written as an empty, unquoted string.

Tells `reader` objects to read an empty, unquoted field as `None`, while behaving like `QUOTE_ALL` in every other respect.

Added in version 3.12.

 csv.QUOTE_STRINGS

Tells `writer` objects to always surround string fields with quotes. It resembles `QUOTE_NONNUMERIC`, the difference being that a field holding `None` is written as an empty, unquoted string.

Tells `reader` objects to read an empty, unquoted string as `None`, while behaving like `QUOTE_NONNUMERIC` in every other respect.

Added in version 3.12.

This exception is provided by the `csv` module:

 *exception *csv.Error

Thrown by any of these functions the moment an error turns up.

[Subject index](INDEX.md) · [Previous](csv-sniffer-class-to-csv-sniffer-has-header.md) · [Continue](dialect-delimiter-to-dialect-strict.md) · [Owning module, declaration or section: csv](csv-csv-file-reading-and-writing.md) · [Owning module, declaration or section: Module Contents](csv-reader-to-csv-field-size-limit.md)
