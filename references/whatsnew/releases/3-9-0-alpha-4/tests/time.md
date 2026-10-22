# Python 3.9.0 alpha 4 / tests / time

[bpo-39502](https://bugs.python.org/issue?@action=redirect&bpo=39502): Skip test_zipfile.test_add_file_after_2107() whenever [`time.localtime()`](https://docs.python.org/3.14/library/time.html#time.localtime) raises [`OverflowError`](https://docs.python.org/3.14/library/exceptions.html#OverflowError). That occurs on AIX 6.1, for instance.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
