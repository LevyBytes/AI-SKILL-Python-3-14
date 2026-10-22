# csv: `csv.Dialect`

*class *csv.Dialect

Acting as a container, the `Dialect` class holds, in its attributes, the rules governing doublequotes, whitespace, delimiters, and the like. Since there is no rigorous CSV specification, the CSV output of one application differs in small ways from another's. It is `Dialect` instances that govern the behavior of `reader` and `writer` instances.

Every usable `Dialect` name comes back from `list_dialects()`, and you can attach them to particular `reader` and `writer` classes by way of their initializer (`__init__`) functions, as shown here:

```python
import csv

with open('students.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, dialect='unix')

```

[Subject index](INDEX.md) · [Previous](csv-dictwriter-class.md) · [Continue](csv-excel-class.md) · [Owning module, declaration or section: csv](csv-csv-file-reading-and-writing.md) · [Owning module, declaration or section: Module Contents](csv-reader-to-csv-field-size-limit.md)
