# Python 3.7.0 alpha 1 / core and builtins / files and paths

[bpo-28746](https://bugs.python.org/issue?@action=redirect&bpo=28746): Repair the set_inheritable() file descriptor method on the platforms that lack the ioctl FIOCLEX and FIONCLEX commands.

[bpo-19398](https://bugs.python.org/issue?@action=redirect&bpo=19398): No extra slash is tacked onto sys.path components anymore should the compile-time PYTHONPATH components be empty.

[bpo-29319](https://bugs.python.org/issue?@action=redirect&bpo=29319): Keep RunMainFromImporter from clobbering sys.path[0].

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
