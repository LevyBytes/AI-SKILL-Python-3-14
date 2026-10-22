# csv — Writer Objects

### Writer Objects

The public methods carried by `writer` objects, meaning `DictWriter` instances along with whatever the `writer()` function gives back, are listed below. For `writer` objects a *row* has to be an iterable of strings or numbers, whereas for `DictWriter` objects it is a dictionary mapping fieldnames onto strings or numbers, each first sent through [`str()`](https://docs.python.org/3.14/library/stdtypes.html#str). Keep in mind that complex numbers come out wrapped in parens, which can trip up other programs reading the CSV files, presuming they handle complex numbers in the first place.

 csvwriter.writerow(*row*, */*)

Emit the *row* parameter to the writer's file object, shaped by the active `Dialect`. Whatever the *write* method of the underlying file object returns is passed straight back.

Changed in version 3.5: Arbitrary iterables became supported.

 csvwriter.writerows(*rows*, */*)

Emit every element of *rows*, an iterable of *row* objects of the kind described above, to the writer's file object, shaped by the active dialect.

The public attribute that writer objects expose is:

 csvwriter.dialect

A read-only account of which dialect the writer is currently applying.

The public method that DictWriter objects expose is:

 DictWriter.writeheader()

Emit a header row carrying the field names (the ones given in the constructor) to the writer's file object, shaped by the active dialect. Whatever the internally used `csvwriter.writerow()` call returns is passed straight back.

Added in version 3.2.

Changed in version 3.8: `writeheader()` additionally hands back the value produced by the `csvwriter.writerow()` method it calls internally.

[Subject index](INDEX.md) · [Previous](csvreader-next-to-dictreader-fieldnames.md) · [Continue](examples.md) · [Owning module, declaration or section: csv](csv-csv-file-reading-and-writing.md)
