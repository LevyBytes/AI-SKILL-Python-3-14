# Python 3.9.0 beta 1 / c api / reset inittab copy null while finalizing stops later interpreter initializations

[bpo-40412](https://bugs.python.org/issue?@action=redirect&bpo=40412): Reset inittab_copy to null while finalizing, which stops later interpreter initializations from crashing when embedded. Gregory Szorc supplied the patch.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
