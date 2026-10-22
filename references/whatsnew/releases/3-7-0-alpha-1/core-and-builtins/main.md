# Python 3.7.0 alpha 1 / core and builtins / main

[bpo-29723](https://bugs.python.org/issue?@action=redirect&bpo=29723): The `sys.path[0]` initialization adjustment from [bpo-29139](https://bugs.python.org/issue?@action=redirect&bpo=29139) introduced a regression by exposing an inconsistency in how sys.path gets set up when running `__main__` out of a zipfile, directory, or other import source. The interpreter now uniformly refrains from ever appending the import location's parent directory onto `sys.path`, and it guarantees that no other `sys.path` entries are accidentally altered while inserting the import location given on the command line.

[Subject index](INDEX.md) · [Release version, date and status](../release-overview/overview.md)
