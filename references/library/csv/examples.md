# csv — Examples

### Examples

Reading a CSV file at its most basic:

```python
import csv
with open('some.csv', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

```

Pulling in a file that uses a different layout:

```python
import csv
with open('passwd', newline='') as f:
    reader = csv.reader(f, delimiter=':', quoting=csv.QUOTE_NONE)
    for row in reader:
        print(row)

```

Here is the matching bare-minimum writing case:

```python
import csv
with open('some.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(someiterable)

```

Because a CSV file is opened for reading through [`open()`](https://docs.python.org/3.14/library/functions.html#open), it is decoded into unicode by default with the system's default encoding (refer to [`locale.getencoding()`](https://docs.python.org/3.14/library/locale.html#locale.getencoding)). Should you want some other encoding for decoding, hand open its `encoding` argument:

```python
import csv
with open('some.csv', newline='', encoding='utf-8') as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

```

Writing in any encoding besides the system default works the same way: pass the encoding argument as you open the output file.

Setting up a fresh dialect:

```python
import csv
csv.register_dialect('unixpwd', delimiter=':', quoting=csv.QUOTE_NONE)
with open('passwd', newline='') as f:
    reader = csv.reader(f, 'unixpwd')

```

A somewhat more sophisticated reader scenario, trapping errors and surfacing them:

```python
import csv, sys
filename = 'some.csv'
with open(filename, newline='') as f:
    reader = csv.reader(f)
    try:
        for row in reader:
            print(row)
    except csv.Error as e:
        sys.exit(f'file {filename}, line {reader.line_num}: {e}')

```

Although parsing strings isn't something the module handles out of the box, it's a simple thing to arrange:

```python
import csv
for row in csv.reader(['one,two,three']):
    print(row)

```

Footnotes

[Subject index](INDEX.md) · [Previous](csvwriter-writerow-to-dictwriter-writeheader.md) · [Owning module, declaration or section: csv](csv-csv-file-reading-and-writing.md)
