# csv: `csv.DictWriter`

*class *csv.DictWriter(*f*, *fieldnames*, *restval=''*, *extrasaction='raise'*, *dialect='excel'*, **args*, ***kwds*)

Build an object that acts like the ordinary writer but projects dictionaries onto the output rows. A [`sequence`](https://docs.python.org/3.14/library/collections.abc.html#module-collections.abc) of keys is what the *fieldnames* parameter holds; it fixes the order in which the dictionary's values handed to the `writerow()` method get written out to file *f*. Where the dictionary lacks a key that appears in *fieldnames*, the optional *restval* parameter says what gets written in its place. Conversely, if the dictionary handed to `writerow()` carries a key that isn't among *fieldnames*, the optional *extrasaction* parameter dictates the response. With it left at `'raise'`, its default, a [`ValueError`](https://docs.python.org/3.14/library/exceptions.html#ValueError) is raised; set to `'ignore'`, the surplus dictionary entries are simply skipped. Whatever other optional or keyword arguments you pass flow through to the `writer` instance underneath.

Be aware that, in contrast to the `DictReader` class, the `DictWriter` class treats its *fieldnames* parameter as mandatory rather than optional.

Should the value you hand to *fieldnames* be an iterator, it gets converted into a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list).

A brief example of how it is used:

```python
import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})

```

[Subject index](INDEX.md) · [Previous](csv-dictreader-class.md) · [Continue](csv-dialect-class.md) · [Owning module, declaration or section: csv](csv-csv-file-reading-and-writing.md) · [Owning module, declaration or section: Module Contents](csv-reader-to-csv-field-size-limit.md)
