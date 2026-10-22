# Python 3.8.0 beta 1 / library / csv

[bpo-27497](https://bugs.python.org/issue?@action=redirect&bpo=27497): The [`csv.DictWriter.writeheader()`](https://docs.python.org/3.14/library/csv.html#csv.DictWriter.writeheader) call now passes along whatever the underlying `csv.Writer.writerow()` method returned. Ashish Nitin Patil contributed this patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
