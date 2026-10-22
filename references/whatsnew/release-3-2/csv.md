# What's New In Python 3.2 / csv — csv

### csv

A new dialect named [`unix_dialect`](https://docs.python.org/3.14/library/csv.html#csv.unix_dialect) is now provided by the [`csv`](https://docs.python.org/3.14/library/csv.html#module-csv) module; it quotes every field and follows the classic Unix convention of using `'\n'` for line termination. Under registration this dialect goes by the name `unix`.

A method called [`writeheader()`](https://docs.python.org/3.14/library/csv.html#csv.DictWriter.writeheader) was added to [`csv.DictWriter`](https://docs.python.org/3.14/library/csv.html#csv.DictWriter) for emitting an opening row that records the field names:

```python
>>> import csv, sys
>>> w = csv.DictWriter(sys.stdout, ['name', 'dept'], dialect='unix')
>>> w.writeheader()
"name","dept"
>>> w.writerows([
...     {'name': 'tom', 'dept': 'accounting'},
...     {'name': 'susan', 'dept': 'Salesl'}])
"tom","accounting"
"susan","sales"

```

(Jay Talbot proposed the new dialect in [bpo-5975](https://bugs.python.org/issue?@action=redirect&bpo=5975); Ed Abraham proposed the fresh method in [bpo-1537721](https://bugs.python.org/issue?@action=redirect&bpo=1537721).)

[Subject index](INDEX.md) · [Previous source section](logging.md) · [Next source section](contextlib.md) · [Release/subject declaration](pep-384-defining-a-stable-abi.md)
