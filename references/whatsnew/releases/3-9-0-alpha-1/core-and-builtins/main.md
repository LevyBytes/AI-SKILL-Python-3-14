# Python 3.9.0 alpha 1 / core and builtins / main

[bpo-20443](https://bugs.python.org/issue?@action=redirect&bpo=20443): Python now resolves the absolute path of the script filename given on the command line (for instance, ?python3 script.py?): the __file__ attribute belonging to the __main__ module and sys.path[0] turn into an absolute path instead of a relative one.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
