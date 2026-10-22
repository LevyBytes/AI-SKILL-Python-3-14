# csv — Dialects and Formatting Parameters

### Dialects and Formatting Parameters

So that stating the layout of input and output records is less of a burden, related formatting settings are bundled together as dialects. Each dialect is a subclass of the `Dialect` class, its assorted attributes spelling out the CSV file's layout. While building `reader` or `writer` objects, the programmer can pass either a string or a `Dialect` subclass as the dialect argument. On top of, or in lieu of, the *dialect* parameter, the programmer may also set individual formatting settings, whose names match the attributes listed below for the `Dialect` class.

The attributes a dialect understands are these:

 Dialect.delimiter

A single-character string that marks the boundary between fields. Its default value is `','`.

 Dialect.doublequote

Governs the way a *quotechar* that turns up within a field is itself quoted. Set to [`True`](https://docs.python.org/3.14/library/constants.html#True), the character gets doubled; set to [`False`](https://docs.python.org/3.14/library/constants.html#False), the *escapechar* is placed ahead of the *quotechar*. Its default value is `True`.

During writing, should *doublequote* be [`False`](https://docs.python.org/3.14/library/constants.html#False) with no *escapechar* configured, encountering a *quotechar* inside a field triggers an `Error`.

 Dialect.escapechar

A single-character string the writer applies to escape any character that needs escaping:

>
- whenever *quoting* equals `QUOTE_NONE`, escaping covers the *delimiter*, the *quotechar*, `'\r'`, `'\n'`, plus every character held in *lineterminator*;

- escaping applies to the *quotechar* when *doublequote* equals [`False`](https://docs.python.org/3.14/library/constants.html#False);

- the *escapechar* itself.

During reading, the *escapechar* strips whatever special meaning the next character would carry. Its default is [`None`](https://docs.python.org/3.14/library/constants.html#None), which switches escaping off.

Changed in version 3.11: Supplying an empty *escapechar* is no longer permitted.

 Dialect.lineterminator

The string that the `writer` appends to end each line it emits. Its default value is `'\r\n'`.

Note

By design, the `reader` always treats either `'\r'` or `'\n'` as end-of-line and pays no attention to *lineterminator*. That may not always remain the case.

 Dialect.quotechar

A single-character string for quoting fields that hold special characters, such as the *delimiter* or the *quotechar*, or that contain new-line characters (`'\r'`, `'\n'`, or anything within *lineterminator*). Its default value is `'"'`. You can assign it `None` to keep `'"'` from being escaped when *quoting* equals `QUOTE_NONE`.

Changed in version 3.11: Supplying an empty *quotechar* is no longer permitted.

 Dialect.quoting

Decides the points at which the writer emits quotes and the reader expects them. It accepts any of the `QUOTE_*` constants, falling back to `QUOTE_MINIMAL` when *quotechar* isn't `None`, and to `QUOTE_NONE` in the remaining case.

 Dialect.skipinitialspace

Set to [`True`](https://docs.python.org/3.14/library/constants.html#True), any spaces sitting right after the *delimiter* get skipped. Its default is [`False`](https://docs.python.org/3.14/library/constants.html#False). Pairing `delimiter=' '` together with `skipinitialspace=True` rules out unquoted empty fields.

 Dialect.strict

Set to `True`, malformed CSV input causes the `Error` exception to be raised. Its default is `False`.

[Subject index](INDEX.md) · [Previous](csv-quote-all-to-csv-error.md) · [Continue](csvreader-next-to-dictreader-fieldnames.md) · [Owning module, declaration or section: csv](csv-csv-file-reading-and-writing.md)
