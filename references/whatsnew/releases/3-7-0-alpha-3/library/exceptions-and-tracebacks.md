# Python 3.7.0 alpha 3 / library / exceptions and tracebacks

[bpo-12382](https://bugs.python.org/issue?@action=redirect&bpo=12382): When it fails to open or create an MSI file, `msilib.OpenDatabase()` now raises a clearer exception message. William Tisäter provided the initial patch.

[bpo-28292](https://bugs.python.org/issue?@action=redirect&bpo=28292): Calendar.itermonthdates() will from now on reliably raise an exception once a date lands outside the 0001-01-01 through 9999-12-31 range. For applications unable to cope with such exceptions, two new methods, itermonthdays3() and itermonthdays4(), are introduced. These return tuples and are free of the range limit that datetime.date imposes.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
