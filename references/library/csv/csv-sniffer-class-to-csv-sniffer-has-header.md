# csv / Module Contents: `csv.Sniffer`, `sniff()`, `has_header()`

*class *csv.Sniffer

Figuring out the format of a given CSV file is the job of the `Sniffer` class.

Two methods are offered by the `Sniffer` class:

 sniff(*sample*, *delimiters=None*)

Examine the supplied *sample* and hand back a `Dialect` subclass that mirrors the settings it detected. Where the optional *delimiters* parameter is supplied, it is read as a string listing the delimiter characters that may be considered valid.

 has_header(*sample*)

Examine the sample text, taken to be CSV-formatted, and hand back [`True`](https://docs.python.org/3.14/library/constants.html#True) whenever the opening row looks like a run of column headers. Going column by column, the guess as to whether the sample carries a header rests on one of two main tests:

- across the rows from the second onward, the values are numeric

- across the rows from the second onward, the values are strings and at least one of them has a length unlike that of the column's candidate header.

The check looks at twenty-one rows following the header; when over half of the columns plus rows satisfy the tests, [`True`](https://docs.python.org/3.14/library/constants.html#True) comes back.

Note

Bear in mind that this method is only a crude heuristic, so it can misfire in either direction.

Here is the `Sniffer` put to work:

```python
with open('example.csv', newline='') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect)
    # ... process CSV file contents here ...

```

These constants are provided by the `csv` module:

[Subject index](INDEX.md) · [Previous](csv-unix-dialect-class.md) · [Continue](csv-quote-all-to-csv-error.md) · [Owning module, declaration or section: csv](csv-csv-file-reading-and-writing.md) · [Owning module, declaration or section: Module Contents](csv-reader-to-csv-field-size-limit.md)
