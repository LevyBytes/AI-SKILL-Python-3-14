# csv: `csv.reader()`, `csv.writer()`, `csv.register_dialect()`, `csv.unregister_dialect()`, `csv.get_dialect()`, `csv.list_dialects()`, `csv.field_size_limit()`

### Module Contents

These functions are provided by the `csv` module:

 csv.reader(*csvfile*, */*, *dialect='excel'*, ***fmtparams*)

Produce a reader object that steps through lines drawn from the supplied *csvfile*. The csvfile has to be an iterable yielding strings, each conforming to the csv format the reader expects; in practice it is usually a list or a file-like object. Should *csvfile* be a file object, open it with `newline=''`. [1] You may supply an optional *dialect* parameter, which names a bundle of settings tied to one specific CSV dialect; it can be either an instance of some subclass of the `Dialect` class or one of the dialect-name strings that `list_dialects()` hands back. The remaining optional *fmtparams* keyword arguments let you override single formatting settings within the active dialect. The Dialects and Formatting Parameters section covers the dialect and formatting settings in full.

Every row pulled from the csv file comes back to you as a list of strings. Types are not converted on your behalf, the sole exception being when the `QUOTE_NONNUMERIC` format option is in effect, where fields lacking quotes get turned into floats.

A brief example of how it is used:

```python
>>> import csv
>>> with open('eggs.csv', newline='') as csvfile:
...     spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
...     for row in spamreader:
...         print(', '.join(row))
Spam, Spam, Spam, Spam, Spam, Baked Beans
Spam, Lovely Spam, Wonderful Spam

```

 csv.writer(*csvfile*, */*, *dialect='excel'*, ***fmtparams*)

Produce a writer object whose job is to turn the user's data into delimited strings on the file-like object you pass. Any object exposing a [`write()`](https://docs.python.org/3.14/library/io.html#io.TextIOBase.write) method qualifies as *csvfile*. When *csvfile* is a file object, open it using `newline=''` [1]. You may hand in an optional *dialect* parameter naming a bundle of settings bound to a particular CSV dialect; it is either an instance of some subclass of the `Dialect` class or one of the dialect-name strings produced by `list_dialects()`. The remaining optional *fmtparams* keyword arguments let you override individual formatting settings in the active dialect. Full coverage of dialects and formatting settings lives in the Dialects and Formatting Parameters section. So that bridging to modules built on the DB API stays as painless as possible, the value [`None`](https://docs.python.org/3.14/library/constants.html#None) gets emitted as an empty string. That conversion can't be undone, but it does simplify writing SQL NULL values out to CSV files without first massaging whatever a `cursor.fetch*` call hands back. Everything else that isn't already a string is run through [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str) ahead of being written.

A brief example of how it is used:

```python
import csv
with open('eggs.csv', 'w', newline='') as csvfile:
    spamwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    spamwriter.writerow(['Spam'] * 5 + ['Baked Beans'])
    spamwriter.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

```

 csv.register_dialect(*name*, */*, *dialect='excel'*, ***fmtparams*)

Bind *dialect* to *name*, where *name* has to be a string. You can describe the dialect by handing in a sub-class of `Dialect`, by supplying *fmtparams* keyword arguments, or by doing both at once, in which case the keyword arguments take precedence over the dialect's own settings. The Dialects and Formatting Parameters section documents dialects and formatting settings completely.

 csv.unregister_dialect(*name*)

Drop whatever dialect *name* points to out of the dialect registry. Should *name* not correspond to any registered dialect, an `Error` is raised.

 csv.get_dialect(*name*)

Hand back whatever dialect is bound to *name*. Should *name* match no registered dialect, an `Error` is raised. What you get back from this function is an immutable `Dialect`.

 csv.list_dialects()

Hand back the names of every dialect currently registered.

 csv.field_size_limit()

 csv.field_size_limit(*new_limit*)

Gives back the largest field size the parser presently permits. When *new_limit* is supplied, that value takes over as the limit.

These classes are provided by the `csv` module:

[Subject index](INDEX.md) · [Previous](csv-csv-file-reading-and-writing.md) · [Continue](csv-dictreader-class.md) · [Owning module, declaration or section: csv](csv-csv-file-reading-and-writing.md)
