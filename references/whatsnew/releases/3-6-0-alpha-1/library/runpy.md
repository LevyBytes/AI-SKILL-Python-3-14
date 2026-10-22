# Python 3.6.0 alpha 1 / library / runpy

[bpo-19771](https://bugs.python.org/issue?@action=redirect&bpo=19771): Likewise within runpy plus the "-m" option, the unrelated note "... is a package and cannot be directly executed" is suppressed whenever the package itself could not be initialized at all (for instance because of a bad `*.pyc` file).

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
