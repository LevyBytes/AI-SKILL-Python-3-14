# Python 3.12.0 alpha 1 / library / unicodedata

[gh-96172](https://github.com/python/cpython/issues/96172): A `unicodedata` defect is corrected: `east_asian_width` formerly handed back the incorrect value for unassigned characters, plus for characters still unassigned yet reserved.

[gh-96019](https://github.com/python/cpython/issues/96019): A defect in the `makeunicodedata.py` script is fixed, yielding roughly 13 KiB of saved space within the `unicodedata` module, particularly its character decomposition data.

[gh-96734](https://github.com/python/cpython/issues/96734): The [`unicodedata`](https://docs.python.org/3.14/library/unicodedata.html#module-unicodedata) tables now track Unicode 15.0.0.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
