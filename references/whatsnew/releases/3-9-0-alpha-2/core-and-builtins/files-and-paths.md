# Python 3.9.0 alpha 2 / core and builtins / files and paths

[bpo-20443](https://bugs.python.org/issue?@action=redirect&bpo=20443): Under Python 3.9.0a1, sys.argv[0] became an absolute path whenever a filename was given on the command line. That behavior is reverted, since the majority of users expect sys.argv to stay untouched.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
