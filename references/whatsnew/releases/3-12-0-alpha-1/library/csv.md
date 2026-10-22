# Python 3.12.0 alpha 1 / library / csv

[gh-92391](https://github.com/python/cpython/issues/92391): Attach [`__class_getitem__()`](https://docs.python.org/3.14/reference/datamodel.html#object.__class_getitem__) to [`csv.DictReader`](https://docs.python.org/3.14/library/csv.html#csv.DictReader) and [`csv.DictWriter`](https://docs.python.org/3.14/library/csv.html#csv.DictWriter) so they can be parameterized while running. Marc Mueller supplied the patch.

[bpo-32547](https://bugs.python.org/issue?@action=redirect&bpo=32547): Should the `fieldnames` argument arrive as an iterator, the constructors for [`DictWriter`](https://docs.python.org/3.14/library/csv.html#csv.DictWriter) and [`DictReader`](https://docs.python.org/3.14/library/csv.html#csv.DictReader) now convert it into a [`list`](https://docs.python.org/3.14/library/stdtypes.html#list).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
