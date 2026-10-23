# What’s New in Python 2.3 / PEP 305: Comma-separated Files - csv

### PEP 305: Comma-separated Files

A format commonly used to dump data out of databases and spreadsheets is the comma-separated file. Python 2.3 brings in a parser for these files.

On first inspection the comma-separated format looks misleadingly easy:

```python
Costs,150,200,3.95

```

Grab a line, call `line.split(',')` — what's hard about that? But mix in string data that may itself hold commas and the picture grows messier:

```python
"Costs",150,200,3.95,"Includes taxes, shipping, and sundry items"

```

You could parse this with one big ugly regular expression, but reaching for the new [`csv`](https://docs.python.org/3.14/library/csv.html#module-csv) package makes it far easier:

```python
import csv

input = open('datafile', 'rb')
reader = csv.reader(input)
for line in reader:
    print line

```

You can hand [`reader()`](https://docs.python.org/3.14/library/csv.html#csv.reader) a variety of options. The field separator isn't restricted to a comma and may be set to any character, and the same goes for the quoting and line-ending characters.

You can also define and register assorted dialects of comma-separated files; right now there are two, both employed by Microsoft Excel. A distinct [`csv.writer`](https://docs.python.org/3.14/library/csv.html#csv.writer) class produces comma-separated files out of a sequence of tuples or lists, putting quotes around strings that include the delimiter.

See also

[**PEP 305**](https://peps.python.org/pep-0305/) - CSV File API

Authored and built by the following contributors: Kevin Altis, Dave Cole, Andrew McNamara, Skip Montanaro, Cliff Wells.

[Subject index](INDEX.md) · [Previous source section](pep-302-new-import-hooks.md) · [Next source section](pep-307-pickle-enhancements.md) · [Release/subject declaration](standard-set-type.md)
