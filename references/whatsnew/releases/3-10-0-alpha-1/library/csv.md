# Python 3.10.0 alpha 1 / library / csv

[bpo-26407](https://bugs.python.org/issue?@action=redirect&bpo=26407): When calling the `__iter__` method, any unexpected errors are no longer hidden behind `TypeError` inside [`csv.reader()`](https://docs.python.org/3.14/library/csv.html#csv.reader), `csv.writer.writerow()`, and `csv.writer.writerows()`.

[bpo-40876](https://bugs.python.org/issue?@action=redirect&bpo=40876): Make the error message clearer inside the [`csv`](https://docs.python.org/3.14/library/csv.html#module-csv) module.

[bpo-12178](https://bugs.python.org/issue?@action=redirect&bpo=12178): [`csv.writer()`](https://docs.python.org/3.14/library/csv.html#csv.writer) now escapes *escapechar* properly whenever the input itself contains *escapechar*. Patch by Catalin Iacob, Berker Peksag, and Itay Elbirt.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
