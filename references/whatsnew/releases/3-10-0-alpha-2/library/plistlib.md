# Python 3.10.0 alpha 2 / library / plistlib

[bpo-42103](https://bugs.python.org/issue?@action=redirect&bpo=42103): Loading a malformed binary Plist file now produces only [`InvalidFileException`](https://docs.python.org/3.14/library/plistlib.html#plistlib.InvalidFileException) and [`RecursionError`](https://docs.python.org/3.14/library/exceptions.html#RecursionError) (whereas ValueError and TypeError could previously surface in certain situations).

[bpo-41491](https://bugs.python.org/issue?@action=redirect&bpo=41491): plistlib: correct the parsing of XML plists that carry hexadecimal integer values

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
