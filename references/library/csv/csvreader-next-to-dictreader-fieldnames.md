# csv - Reader Objects

### Reader Objects

The public methods carried by reader objects, which means `DictReader` instances along with whatever the `reader()` function gives back, are:

 csvreader.__next__()

Hand back the reader's iterable's next row, parsed under the active `Dialect`, as a list where the object came from `reader()` or as a dict where it is a `DictReader` instance. The customary way to invoke this is `next(reader)`.

The public attributes that reader objects expose are:

 csvreader.dialect

A read-only account of which dialect the parser is currently applying.

 csvreader.line_num

How many lines have been consumed from the source iterator. That figure differs from the count of records handed back, since a single record may stretch over several lines.

The public attribute that DictReader objects expose is:

 DictReader.fieldnames

When it wasn't handed in as a parameter at object-creation time, this attribute gets set the first time you read it or as soon as the opening record is pulled from the file.

[Subject index](INDEX.md) · [Previous](dialect-delimiter-to-dialect-strict.md) · [Continue](csvwriter-writerow-to-dictwriter-writeheader.md) · [Owning module, declaration or section: csv](csv-csv-file-reading-and-writing.md)
