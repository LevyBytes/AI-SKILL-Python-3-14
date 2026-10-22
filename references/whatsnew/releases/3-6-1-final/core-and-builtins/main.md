# Python 3.6.1 final / core and builtins / main

[bpo-29723](https://bugs.python.org/issue?@action=redirect&bpo=29723): The `sys.path[0]` initialization change for [bpo-29139](https://bugs.python.org/issue?@action=redirect&bpo=29139) introduced a regression by exposing an inconsistency in the way sys.path gets initialized while running `__main__` out of a zipfile, directory, or some other import location. The interpreter now reliably refuses to ever add the import location's parent directory onto `sys.path`, and makes sure no other `sys.path` entries get changed by accident when it inserts the import location named on the command line.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
