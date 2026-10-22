# Python 3.11.0 alpha 6 / library / binary

[bpo-14156](https://bugs.python.org/issue?@action=redirect&bpo=14156): argparse.FileType now accepts an argument of ?-? in binary mode, handing back the .buffer attribute of sys.stdin/sys.stdout as fits. Modes that include ?x? and ?a? behave the same as ?w? once the argument is ?-?. Josh Rosenberg contributed the patch

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
