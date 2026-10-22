# csv: `csv.DictReader`

*class *csv.DictReader(*f*, *fieldnames=None*, *restkey=None*, *restval=None*, *dialect='excel'*, **args*, ***kwds*)

Build an object that behaves much like the ordinary reader, except each row's contents get mapped into a [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict) keyed by whatever the optional *fieldnames* parameter supplies.

A [sequence](https://docs.python.org/3.14/glossary.html#term-sequence) is what the *fieldnames* parameter expects. Leave *fieldnames* out and the entries in the opening row of file *f* serve as the fieldnames, then drop out of the returned rows. Supply *fieldnames* and those names apply while the opening row stays in the returned rows. However the fieldnames end up being chosen, the dictionary keeps them in the order they were given.

When a row carries more fields than there are fieldnames, the surplus data lands in a list filed under the fieldname named by *restkey* (whose default is `None`). When a row that isn't blank carries fewer fields than fieldnames, the gaps are padded out with whatever *restval* holds (its default is also `None`).

Any further optional or keyword arguments get forwarded along to the `reader` instance underneath.

Should the value you hand to *fieldnames* be an iterator, it gets converted into a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list).

Changed in version 3.6: The rows handed back are henceforth of type `OrderedDict`.

Changed in version 3.8: The rows handed back are henceforth of type [`dict`](https://docs.python.org/3.14/library/stdtypes.html#dict).

A brief example of how it is used:

```python
>>> import csv
>>> with open('names.csv', newline='') as csvfile:
...     reader = csv.DictReader(csvfile)
...     for row in reader:
...         print(row['first_name'], row['last_name'])
...
Eric Idle
John Cleese

>>> print(row)
{'first_name': 'John', 'last_name': 'Cleese'}

```

[Subject index](INDEX.md) · [Previous](csv-reader-to-csv-field-size-limit.md) · [Continue](csv-dictwriter-class.md) · [Owning module, declaration or section: csv](csv-csv-file-reading-and-writing.md) · [Owning module, declaration or section: Module Contents](csv-reader-to-csv-field-size-limit.md)
