# Python 3.5.2 release candidate 1 / library / runpy

[bpo-19771](https://bugs.python.org/issue?@action=redirect&bpo=19771): Within runpy and the "-m" path as well, the unhelpful "... is a package and cannot be directly executed" notice is suppressed whenever the package never managed to initialize (for instance, owing to a corrupt `*.pyc` file).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
