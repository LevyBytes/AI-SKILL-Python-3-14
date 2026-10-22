# Python 3.9.0 alpha 3 / library / bz2

[bpo-39357](https://bugs.python.org/issue?@action=redirect&bpo=39357): The *buffering* parameter was dropped from [`bz2.BZ2File`](https://docs.python.org/3.14/library/bz2.html#bz2.BZ2File). It had been ignored since Python 3.0 and supplying it raised [`DeprecationWarning`](https://docs.python.org/3.14/library/exceptions.html#DeprecationWarning). To govern how a file opens, hand in an already-open file object. The *compresslevel* parameter is now keyword-only.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
